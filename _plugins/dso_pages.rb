# frozen_string_literal: true

require "csv"
require "date"
require "digest"
require "json"
require "set"

# GRD tool ("Quel est mon GRD ?"): turns the belgian-dso-map release copied in
# _data/dso/ (by scripts/sync_dso.py) into
#   - assets/data/dso-<version>.json, the compact file the lookup page fetches
#     (assets/js/dso-lookup-core.js reads it with indexFromJson);
#   - the table data of the municipality pages (ref tool-dso-list);
#   - the sitemap date of those pages.
# Called by the build orchestrator (_plugins/site_graph.rb) right after the
# glossary pages, so the pages it touches go through every later step.
#
# When it raises a BuildError:
#   - the data are checked on every build that has them (integrity against
#     SHA256SUMS, headers, versions, keys, operators, notes, URLs, dates,
#     meta.yml), because the JSON file is published whatever pages exist;
#   - the presentation checks (front-matter dates, grd_tool i18n labels) run
#     only for the tool pages that exist. The site therefore builds before the
#     pages are written, and with the French pages alone while translations are
#     pending: a warning names the missing languages, and scripts/check_site.py
#     fails on hreflang until they exist;
#   - without _data/dso/ the step does nothing, unless a tool page exists.
# On a draft release, notes without their nl/de/en text fall back to fr with
# a warning; on a published release they are an error.
#
# Dates (scripts/dso_dates.py computes the same values; keep both equal):
#   data_date   max of: changed_at of every dso_lookup row; of the operators
#               and notes the rows reference (plus the dataset-<region>- notes
#               of the regions present); of every sources row (the table page
#               lists them); meta.yml removed_max
#   table page  max(its front-matter last_modified_at, DSO_TEMPLATE_REVISION,
#               data_date)
#   tool page   its front matter only
#   tools hub   max(own front matter, children's front matter), in the Hubs
#               step of site_graph.rb, from the fm_last_modified_at set here
# Every value is a date, rendered as 00:00 Europe/Brussels. Nothing else is
# read: no clock, no file dates, no version control, so two builds of the same
# files give the same sitemap. scripts/check_dso_dates.py greps this file for
# any call that could read one.
module OptimCE
  module DsoPages
    # Bump to the day of a change to the table page's template or to its
    # grd_tool strings: the table page's lastmod follows it.
    DSO_TEMPLATE_REVISION = "2026-10-18"

    LANGS = %w[fr en de nl].freeze
    REGIONS = %w[BRU VLA WAL].freeze
    REGION_REGULATOR = { "BRU" => "BE-BRU-BRUGEL", "VLA" => "BE-VLA-VREG", "WAL" => "BE-WAL-CWAPE" }.freeze
    # INS prefix => [region, ISO 3166-2 province]; Brussels has no province.
    INS_PREFIXES = [
      ["21", "BRU", ""], ["23", "VLA", "BE-VBR"], ["24", "VLA", "BE-VBR"], ["25", "WAL", "BE-WBR"],
      ["1", "VLA", "BE-VAN"], ["3", "VLA", "BE-VWV"], ["4", "VLA", "BE-VOV"], ["5", "WAL", "BE-WHT"],
      ["6", "WAL", "BE-WLG"], ["7", "VLA", "BE-VLI"], ["8", "WAL", "BE-WLX"], ["9", "WAL", "BE-WNA"],
    ].freeze
    FLAGS = %w[transition operator_differs to_confirm propane_note].freeze
    GAS_STATUSES = %w[designated none foreign].freeze
    KINDS = %w[grd gas_foreign grtl].freeze
    ROLES = %w[R M C X].freeze
    BOOLEANS = %w[true false].freeze

    LIST_REF = "tool-dso-list"
    TOOL_REF = "tool-dso"
    HUB_REF = "tools"
    HUB_PARENT = "tools"
    JSON_DIR = "assets/data"

    SUMS = "SHA256SUMS"
    META = "meta.yml"
    RELEASE_FILES = %w[dso_lookup.csv operators.csv notes.csv sources.csv vectors.csv
                       CHANGES.md release.json ATTRIBUTION.md].freeze
    OPTIONAL_FILES = %w[REPORT.md].freeze
    DATE_COLUMNS = %w[first_seen changed_at data_version].freeze
    HEADERS = {
      "dso_lookup.csv" => %w[postcode ins commune_fr commune_nl commune_de region province section_key
                             section_fr section_nl section_de elec_operator elec_designated gas_status
                             gas_operator flags note_key source_ids valid_from] + DATE_COLUMNS,
      "operators.csv" => %w[id kind name legal_name region elec gas website regulator tariffs_url
                            lookup replaced_by] + DATE_COLUMNS,
      "notes.csv" => %w[key fr nl de en] + DATE_COLUMNS,
      "sources.csv" => %w[id role publisher title url retrieved_at sha256 license note] + DATE_COLUMNS,
      "vectors.csv" => %w[name kind postcode ins section_key post_name ean expect_status expect_key
                          expect_elec expect_gas_status expect_gas expect_flags],
    }.freeze
    VERSIONED = %w[dso_lookup.csv operators.csv notes.csv sources.csv].freeze
    ATTRIBUTION_COLUMNS = %w[elec_operator elec_designated gas_status gas_operator flags note_key
                             source_ids valid_from].freeze

    # The browser file: one array per row, without postcode (the key) or the
    # commune columns (in "communes"); see assets/js/dso-lookup-core.js.
    JSON_COLS = %w[ins section_key section_fr section_nl section_de elec_operator elec_designated
                   gas_status gas_operator flags note_key valid_from].freeze
    JSON_COMMUNE_COLS = %w[commune_fr commune_nl commune_de region province].freeze
    JSON_OPERATOR_KEYS = %w[name legal_name kind region website tariffs_url regulator].freeze

    POSTCODE_RE = /\A[0-9]{4}\z/
    INS_RE = /\A[1-9][0-9]{4}\z/
    DATE_RE = /\A[0-9]{4}-[0-9]{2}-[0-9]{2}\z/
    VERSION_RE = /\A([0-9]{4})\.(0[1-9]|1[0-2])\.(0|[1-9][0-9]*)(-draft)?\z/
    SUMS_LINE_RE = /\A([0-9a-f]{64})  ([A-Za-z0-9._-]+)\z/
    # URL rules of the data contract (belgian-dso-map validate.py, schema.URL_RE),
    # also checked by scripts/dso_data.py at sync time: a sources.csv url is
    # http or https (some publishers have no https), an operator's website and
    # tariffs_url are https or empty. Never stricter than the contract, or a
    # valid release passes the sync and then fails the build.
    HTTPS_RE = %r{\Ahttps://[^[:space:]]+\z}
    HTTP_URL_RE = %r{\Ahttps?://[^[:space:]]+\z}
    CHANGES_TITLE = "# Changes"
    CHANGES_HEADING_RE = /\A## ([0-9]{4}\.[0-9]{2}\.[0-9]+) — ([0-9]{4}-[0-9]{2}-[0-9]{2})\z/
    CHANGES_ENTRY_RE = /\A- (added|changed|removed) (dso_lookup|operators|notes|sources) ([^[:space:]\u001c-\u001f]+)( — .*)?\z/
    CHANGES_SPECIAL = ["- initial release", "- no changes"].freeze
    DATASET_NOTE_RE = /\Adataset-(bru|vla|wal)-/
    BOM = "\xEF\xBB\xBF".b

    def self.apply(site)
      pages = tool_pages(site)
      pages.each { |page| record_front_matter(site, page) }
      data = site.data["dso"]
      if data.nil? || data.empty?
        needy = pages.select { |p| [LIST_REF, TOOL_REF].include?(p.data["ref"]) }
        unless needy.empty?
          raise BuildError, "#{needy.first.relative_path}: no GRD data in _data/dso " \
                            "(run python scripts/sync_dso.py)"
        end
        return
      end

      dir = File.join(site.source, site.config["data_dir"] || "_data", "dso")
      set = Dataset.new(dir, data)
      json_url = write_json(site, set)
      site.data["dso_json_url"] = json_url
      meta = set.public_meta

      pages.each do |page|
        case page.data["ref"]
        when TOOL_REF
          page.data["dso_json_url"] = json_url
          page.data["dso_meta"] = meta
        when LIST_REF
          attach_table(site, page, set, meta)
        end
      end
      warn_incomplete(pages)
    end

    # --- pages -----------------------------------------------------------------

    def self.tool_pages(site)
      site.pages.select do |page|
        [LIST_REF, TOOL_REF, HUB_REF].include?(page.data["ref"]) || page.data["breadcrumb_parent"] == HUB_PARENT
      end
    end

    # Language implied by the URL prefix, as I18nMetadata decides it (it runs
    # after this step, so page.data["lang"] may still be the site default).
    def self.lang_of(site, page)
      url = page.url.to_s
      (site.config["languages"] || []).each do |entry|
        prefix = entry["prefix"].to_s
        next if prefix.empty?
        return entry["code"] if url.start_with?("#{prefix}/")
      end
      "fr"
    end

    # Front-matter date of a tools page, kept as fm_last_modified_at: the hub
    # is dated from it (never from the table page's data-driven value), and
    # scripts/dso_dates.py reads the same line from the file.
    def self.record_front_matter(site, page)
      lang = lang_of(site, page)
      raise BuildError, "#{page.relative_path}: tools page in an unknown language #{lang}" unless LANGS.include?(lang)
      raise BuildError, "#{page.relative_path}: a tools page needs a permalink" if page.data["permalink"].to_s.empty?

      value = page.data["last_modified_at"]
      day = if value.is_a?(Date) && !value.is_a?(DateTime)
              value
            elsif value.is_a?(String) && value.match?(DATE_RE)
              begin
                Date.iso8601(value)
              rescue Date::Error
                nil
              end
            end
      unless day
        raise BuildError, "#{page.relative_path}: last_modified_at must be a date (YYYY-MM-DD), " \
                          "got #{value.inspect}"
      end

      page.data["fm_last_modified_at"] = day
    end

    def self.warn_incomplete(pages)
      pages.group_by { |p| p.data["ref"] }.each do |ref, group|
        next unless [LIST_REF, TOOL_REF, HUB_REF].include?(ref)

        missing = LANGS - group.map { |p| lang_of(p.site, p) }
        next if missing.empty?

        Jekyll.logger.warn "DsoPages:", "ref #{ref} has no #{missing.join(", ")} page yet " \
                                        "(hreflang stays incomplete)"
      end
    end

    def self.write_json(site, set)
      page = Jekyll::PageWithoutAFile.new(site, site.source, JSON_DIR, "dso-#{set.version}.json")
      page.content = "#{JSON.generate(set.browser_payload)}\n"
      page.data["layout"] = nil
      page.data["render_with_liquid"] = false
      page.data["sitemap"] = false
      site.pages << page
      "/#{JSON_DIR}/dso-#{set.version}.json"
    end

    def self.attach_table(site, page, set, meta)
      lang = lang_of(site, page)
      labels = site.data.dig("i18n", lang, "grd_tool")
      problems = set.label_problems(labels, lang)
      unless problems.empty?
        raise BuildError, "#{page.relative_path}: _data/i18n/#{lang}.yml grd_tool lacks " \
                          "labels:\n  - #{problems.first(30).join("\n  - ")}"
      end

      page.data["dso_table"] = set.table(lang, labels)
      page.data["dso_sources"] = set.sources_for_page
      page.data["dso_attribution"] = set.attribution
      page.data["dso_data_date"] = set.data_date
      page.data["dso_version"] = set.version
      page.data["dso_meta"] = meta
      day = [page.data["fm_last_modified_at"].iso8601, DSO_TEMPLATE_REVISION, set.data_date].max
      page.data["last_modified_at"] = Dates.to_time(Date.iso8601(day))
    end

    # --- names -----------------------------------------------------------------

    # Name rule of assets/js/dso-lookup-core.js (localName): an empty nl or de
    # name is the fr one; English uses the official name of the region (nl in
    # Flanders, fr in Wallonia, "fr / nl" in Brussels).
    def self.local_name(names, lang, region)
      fr = names["fr"].to_s
      nl = names["nl"].to_s.empty? ? fr : names["nl"].to_s
      de = names["de"].to_s.empty? ? fr : names["de"].to_s
      case lang
      when "nl" then nl
      when "de" then de
      when "en"
        case region
        when "VLA" then nl
        when "BRU" then fr == nl ? fr : "#{fr} / #{nl}"
        else fr
        end
      else fr
      end
    end

    # Accent-folded sort key: NFKD, drop marks, lower case, keep [a-z0-9].
    def self.fold(text)
      text.to_s.unicode_normalize(:nfkd).gsub(/\p{M}/, "").downcase.gsub(/[^a-z0-9]/, "")
    end

    # --- the data --------------------------------------------------------------

    # _data/dso/ read twice: Jekyll's own read (site.data["dso"]) must equal a
    # strict read of the exact bytes that SHA256SUMS covers.
    class Dataset
      attr_reader :version, :date, :draft, :rows, :operators, :notes, :sources, :attribution,
                  :data_date, :meta

      def initialize(dir, data)
        @dir = dir
        @problems = []
        @warnings = []
        load(data)
        fail_if_problems
        validate
        fail_if_problems
        @warnings.uniq.each { |w| Jekyll.logger.warn "DsoPages:", w }
        @data_date = compute_data_date
      end

      def public_meta
        { "version" => @version, "date" => @date, "draft" => @draft, "data_date" => @data_date }
      end

      # --- loading -------------------------------------------------------------

      def load(data)
        raw = read_files
        return if raw.nil?

        @tables = {}
        HEADERS.each do |name, header|
          rows = parse_csv(raw[name], name, header)
          next if rows.nil?

          key = File.basename(name, ".csv")
          jekyll_rows = Array(data[key]).map { |row| row.transform_values { |v| v.to_s } }
          if jekyll_rows != rows
            @problems << "#{name}: Jekyll's data reader does not read it like a strict CSV parser " \
                         "(csv_reader settings?)"
          end
          @tables[name] = rows
        end
        @release = parse_release(raw["release.json"])
        @meta = data["meta"]
        @attribution = raw["ATTRIBUTION.md"]
        @changes = parse_changes(raw["CHANGES.md"])
        @lookup_sha256 = Digest::SHA256.hexdigest(raw["dso_lookup.csv"])
      end

      def read_files
        missing = (RELEASE_FILES + [SUMS, META]).reject { |name| File.file?(File.join(@dir, name)) }
        unless missing.empty?
          @problems << "missing #{missing.join(", ")} (run python scripts/sync_dso.py)"
          return nil
        end

        bytes = {}
        Dir.children(@dir).sort.each do |name|
          path = File.join(@dir, name)
          unless File.file?(path)
            @problems << "#{name}: unexpected entry (not a regular file)"
            next
          end
          bytes[name] = File.binread(path)
        end
        check_sums(bytes)
        text = {}
        (RELEASE_FILES + [SUMS, META]).each do |name|
          value = decode(bytes[name], name)
          text[name] = value if value
        end
        @problems.empty? ? text : nil
      end

      def decode(data, name)
        return nil if data.nil?

        if data.start_with?(BOM)
          @problems << "#{name}: starts with a UTF-8 BOM"
        elsif data.include?("\r")
          @problems << "#{name}: contains a CR (line endings must be LF; see .gitattributes)"
        elsif !data.empty? && !data.end_with?("\n")
          @problems << "#{name}: does not end with a newline"
        else
          value = data.dup.force_encoding(Encoding::UTF_8)
          return value if value.valid_encoding?

          @problems << "#{name}: not valid UTF-8"
        end
        nil
      end

      # Every file present (other than SHA256SUMS and meta.yml) is listed and
      # matches; every listed name is a release file; REPORT.md is optional.
      def check_sums(bytes)
        sums = {}
        names = []
        text = decode(bytes[SUMS], SUMS)
        return if text.nil?

        text.split("\n").each_with_index do |line, i|
          match = SUMS_LINE_RE.match(line)
          unless match
            @problems << "#{SUMS}: line #{i + 1} is not '<sha256>  <name>'"
            next
          end
          @problems << "#{SUMS}: #{match[2]} is listed twice" if sums.key?(match[2])
          sums[match[2]] = match[1]
          names << match[2]
        end
        @problems << "#{SUMS}: names are not sorted" unless names == names.sort
        sums.each_key do |name|
          @problems << "#{SUMS} lists #{name}, which is not a release file" unless (RELEASE_FILES + OPTIONAL_FILES).include?(name)
        end
        RELEASE_FILES.each { |name| @problems << "#{SUMS} does not list #{name}" unless sums.key?(name) }
        bytes.each do |name, data|
          next if [SUMS, META].include?(name)

          if !sums.key?(name)
            @problems << "#{name} is present but not listed in #{SUMS}"
          elsif Digest::SHA256.hexdigest(data) != sums[name]
            @problems << "#{name}: sha256 does not match #{SUMS} (line endings changed?)"
          end
        end
      end

      def parse_csv(text, name, header)
        return nil if text.nil?

        parsed = CSV.parse(text)
        if parsed.first != header
          @problems << "#{name}: header is #{parsed.first.to_a.join(",")}, expected #{header.join(",")}"
          return nil
        end
        parsed.drop(1).each_with_index.filter_map do |cells, i|
          if cells.size != header.size
            @problems << "#{name}: line #{i + 2}: #{cells.size} fields, expected #{header.size}"
            next
          end
          header.zip(cells.map(&:to_s)).to_h
        end
      rescue CSV::MalformedCSVError => e
        @problems << "#{name}: #{e.message}"
        nil
      end

      def parse_release(text)
        value = JSON.parse(text.to_s)
        unless value.is_a?(Hash) && %w[version date previous counts].all? { |k| value.key?(k) }
          @problems << "release.json: needs version, date, previous and counts"
          return nil
        end
        value
      rescue JSON::ParserError => e
        @problems << "release.json: not JSON (#{e.message})"
        nil
      end

      # Port of belgian-dso-map changes.parse_changes(): [[version, date, entries]], newest first.
      def parse_changes(text)
        return [] if text.nil?

        lines = text.split("\n")
        unless lines.first == CHANGES_TITLE
          @problems << "CHANGES.md: line 1 is not #{CHANGES_TITLE.inspect}"
          return []
        end
        sections = []
        lines.drop(1).each_with_index do |line, i|
          next if line.empty?

          if (heading = CHANGES_HEADING_RE.match(line))
            sections << [heading[1], heading[2], []]
          elsif CHANGES_ENTRY_RE.match?(line) || CHANGES_SPECIAL.include?(line)
            if sections.empty?
              @problems << "CHANGES.md: line #{i + 2}: entry before any version heading"
            else
              sections.last[2] << line
            end
          else
            @problems << "CHANGES.md: line #{i + 2}: not a heading or an entry"
          end
        end
        sections.each do |version, day, entries|
          @problems << "CHANGES.md: #{version}: no entries" if entries.empty?
          @problems << "CHANGES.md: #{version}: invalid date #{day}" unless DsoPages.valid_date?(day)
          @problems << "CHANGES.md: #{version}: not YYYY.MM.N" unless VERSION_RE.match?(version) && !version.end_with?("-draft")
        end
        sections.each_cons(2) do |newer, older|
          next unless VERSION_RE.match?(newer[0]) && VERSION_RE.match?(older[0])

          unless (DsoPages.version_key(newer[0]) <=> DsoPages.version_key(older[0])).positive?
            @problems << "CHANGES.md: #{newer[0]}: versions must be newest first"
          end
          @problems << "CHANGES.md: #{newer[0]}: dated before #{older[0]}" if newer[1] < older[1]
        end
        sections
      end

      def fail_if_problems
        return if @problems.empty?

        shown = @problems.first(30)
        more = @problems.size > shown.size ? "\n  … and #{@problems.size - shown.size} more" : ""
        raise BuildError, "_data/dso breaks the data contract (#{@problems.size} problem(s); " \
                          "re-run python scripts/sync_dso.py):\n  - #{shown.join("\n  - ")}#{more}"
      end

      # --- validation ----------------------------------------------------------

      def validate
        validate_release
        return unless @problems.empty?

        @rows = @tables["dso_lookup.csv"]
        @operators = @tables["operators.csv"].to_h { |op| [op["id"], op] }
        @notes = @tables["notes.csv"].to_h { |note| [note["key"], note] }
        @sources = @tables["sources.csv"]
        @problems << "operators.csv: duplicate id" if @operators.size != @tables["operators.csv"].size
        @problems << "notes.csv: duplicate key" if @notes.size != @tables["notes.csv"].size
        validate_versions_and_dates
        validate_operators
        validate_notes
        validate_sources
        validate_rows
        validate_counts_and_meta
      end

      def validate_release
        @version = @release["version"].to_s
        @date = @release["date"].to_s
        @problems << "release.json: version #{@version.inspect} is not YYYY.MM.N[-draft]" unless VERSION_RE.match?(@version)
        @problems << "release.json: date #{@date.inspect} is not a date" unless DsoPages.valid_date?(@date)
        previous = @release["previous"]
        unless previous == "" || (previous.is_a?(String) && VERSION_RE.match?(previous))
          @problems << "release.json: previous #{previous.inspect}"
        end
        @draft = @version.end_with?("-draft")
        newest = @changes.first
        base = @version.delete_suffix("-draft")
        if newest.nil?
          @problems << "CHANGES.md: no version heading"
        elsif newest[0] != base || newest[1] != @date
          @problems << "CHANGES.md: newest heading #{newest[0]} #{newest[1]} is not #{base} #{@date}"
        end
      end

      def validate_versions_and_dates
        VERSIONED.each do |name|
          @tables[name].each_with_index do |row, i|
            where = "#{name}: line #{i + 2}"
            @problems << "#{where}: data_version #{row["data_version"]} is not #{@version}" if row["data_version"] != @version
            first_seen = row["first_seen"]
            changed_at = row["changed_at"]
            unless DsoPages.valid_date?(first_seen) && DsoPages.valid_date?(changed_at)
              @problems << "#{where}: first_seen/changed_at is not a date"
              next
            end
            @problems << "#{where}: first_seen after changed_at" if first_seen > changed_at
            @problems << "#{where}: changed_at #{changed_at} is after the version date #{@date}" if changed_at > @date
          end
        end
      end

      def validate_operators
        @tables["operators.csv"].each do |op|
          id = op["id"]
          @problems << "operators.csv: #{id}: kind #{op["kind"]}" unless KINDS.include?(op["kind"])
          @problems << "operators.csv: #{id}: no name" if op["name"].empty?
          @problems << "operators.csv: #{id}: region #{op["region"]}" unless REGIONS.include?(op["region"])
          %w[elec gas lookup].each do |flag|
            @problems << "operators.csv: #{id}: #{flag} is not true/false" unless BOOLEANS.include?(op[flag])
          end
          %w[website tariffs_url].each do |column|
            next if op[column].empty? || HTTPS_RE.match?(op[column])

            @problems << "operators.csv: #{id}: #{column} is not an https URL (nor empty)"
          end
          @problems << "operators.csv: #{id}: regulator #{op["regulator"]}" unless REGION_REGULATOR.value?(op["regulator"])
          unless op["replaced_by"].empty? || @operators.key?(op["replaced_by"])
            @problems << "operators.csv: #{id}: replaced_by #{op["replaced_by"]} is unknown"
          end
        end
      end

      def validate_notes
        keys = @tables["notes.csv"].map { |n| n["key"] }
        @problems << "notes.csv: not sorted by key" unless keys == keys.sort
        @notes.each do |key, note|
          @problems << "notes.csv: #{key}: no fr text" if note["fr"].empty?
          %w[nl de en].each do |lang|
            next unless note[lang].empty?

            if @draft
              @warnings << "draft data: note #{key} has no #{lang} text yet (the fr text is shown)"
              note[lang] = note["fr"]
            else
              @problems << "notes.csv: #{key}: no #{lang} text"
            end
          end
        end
      end

      def validate_sources
        ids = @sources.map { |s| s["id"] }
        @problems << "sources.csv: duplicate or unsorted id" unless ids == ids.uniq.sort
        @sources.each do |source|
          id = source["id"]
          @problems << "sources.csv: #{id}: role #{source["role"]}" unless ROLES.include?(source["role"])
          @problems << "sources.csv: #{id}: url is not an http(s) URL" unless HTTP_URL_RE.match?(source["url"])
          retrieved = source["retrieved_at"]
          unless DsoPages.valid_date?(retrieved) && retrieved <= @date
            @problems << "sources.csv: #{id}: retrieved_at #{retrieved} is not a date on or before #{@date}"
          end
        end
      end

      def validate_rows
        keys = @rows.map { |r| [r["postcode"], r["ins"], r["section_key"]] }
        @problems << "dso_lookup.csv: rows are not sorted by (postcode, ins, section_key)" unless keys == keys.sort
        @problems << "dso_lookup.csv: duplicate (postcode, ins, section_key)" unless keys.uniq.size == keys.size
        source_ids = @sources.map { |s| s["id"] }.to_set
        @rows.each_with_index do |row, i|
          validate_row(row, "dso_lookup.csv: line #{i + 2}", source_ids)
        end
        validate_consistency
      end

      def validate_row(row, where, source_ids)
        @problems << "#{where}: postcode #{row["postcode"].inspect}" unless POSTCODE_RE.match?(row["postcode"])
        @problems << "#{where}: ins #{row["ins"].inspect}" unless INS_RE.match?(row["ins"])
        geography = INS_PREFIXES.find { |prefix, _, _| row["ins"].start_with?(prefix) }
        if geography.nil? || geography[1] != row["region"] || geography[2] != row["province"]
          @problems << "#{where}: region/province #{row["region"]}/#{row["province"]} do not match INS #{row["ins"]}"
        end
        @problems << "#{where}: no commune_fr" if row["commune_fr"].empty?
        if row["section_key"].empty?
          @problems << "#{where}: section names without section_key" unless (row["section_fr"] + row["section_nl"] + row["section_de"]).empty?
        elsif row["section_fr"].empty?
          @problems << "#{where}: section #{row["section_key"]} has no section_fr"
        end
        validate_operator_use(row, where)
        flags = row["flags"].empty? ? [] : row["flags"].split("|")
        unless flags.uniq == flags && (flags - FLAGS).empty? && flags == FLAGS.select { |f| flags.include?(f) }
          @problems << "#{where}: flags #{row["flags"].inspect} (known flags, canonical order)"
        end
        if flags.include?("operator_differs") != (row["elec_operator"] != row["elec_designated"])
          @problems << "#{where}: operator_differs must be set exactly when the operator is not the designated DSO"
        end
        unless row["note_key"].empty? || @notes.key?(row["note_key"])
          @problems << "#{where}: note_key #{row["note_key"]} is not in notes.csv"
        end
        row["source_ids"].split("|").each do |id|
          @problems << "#{where}: source #{id} is not in sources.csv" unless source_ids.include?(id)
        end
        valid_from = row["valid_from"]
        unless valid_from.empty? || (DsoPages.valid_date?(valid_from) && valid_from <= @date)
          @problems << "#{where}: valid_from #{valid_from} is not a date on or before #{@date}"
        end
      end

      def validate_operator_use(row, where)
        elec = @operators[row["elec_operator"]]
        if elec.nil? || elec["kind"] != "grd" || elec["elec"] != "true" || elec["lookup"] != "true" || !elec["replaced_by"].empty?
          @problems << "#{where}: elec_operator #{row["elec_operator"]} is not an active electricity DSO"
        end
        designated = @operators[row["elec_designated"]]
        if designated.nil? || designated["kind"] != "grd" || designated["elec"] != "true"
          @problems << "#{where}: elec_designated #{row["elec_designated"]} is not an electricity DSO"
        end
        status = row["gas_status"]
        gas = @operators[row["gas_operator"]]
        case status
        when "none"
          @problems << "#{where}: gas_status none with a gas_operator" unless row["gas_operator"].empty?
        when "designated", "foreign"
          kind = status == "designated" ? "grd" : "gas_foreign"
          if gas.nil? || gas["kind"] != kind || gas["gas"] != "true" || gas["lookup"] != "true" || !gas["replaced_by"].empty?
            @problems << "#{where}: gas_operator #{row["gas_operator"].inspect} is not an active #{kind} gas operator"
          end
        else
          @problems << "#{where}: gas_status #{status.inspect}"
        end
      end

      # One commune, one set of names; one section (or a commune without
      # sections), one attribution: the table groups rely on it.
      def validate_consistency
        @rows.group_by { |r| r["ins"] }.each do |ins, rows|
          communes = rows.map { |r| r.values_at("commune_fr", "commune_nl", "commune_de", "region", "province") }.uniq
          @problems << "dso_lookup.csv: INS #{ins} has different names or region across rows" if communes.size > 1
          sectioned = rows.map { |r| !r["section_key"].empty? }.uniq
          @problems << "dso_lookup.csv: INS #{ins} mixes section rows and whole-commune rows" if sectioned.size > 1
          rows.group_by { |r| r["section_key"] }.each do |key, unit|
            values = unit.map { |r| r.values_at("section_fr", "section_nl", "section_de", *ATTRIBUTION_COLUMNS) }.uniq
            next if values.size == 1

            @problems << "dso_lookup.csv: INS #{ins} #{key.empty? ? "(whole commune)" : key} has different attributions across postcodes"
          end
        end
      end

      def validate_counts_and_meta
        counts = computed_counts
        @problems << "release.json: counts #{@release["counts"]} != files #{counts}" if @release["counts"] != counts
        meta = @meta
        unless meta.is_a?(Hash)
          @problems << "meta.yml is not a mapping"
          return
        end
        expected = { "version" => @version, "date" => @date, "draft" => @draft,
                     "dso_lookup_sha256" => @lookup_sha256, "counts" => @release["counts"] }
        expected.each do |key, value|
          @problems << "meta.yml: #{key} is #{meta[key].inspect}, expected #{value.inspect}" if meta[key] != value
        end
        removed_max = meta["removed_max"]
        unless removed_max == "" || (removed_max.is_a?(String) && DsoPages.valid_date?(removed_max) && removed_max <= @date)
          @problems << "meta.yml: removed_max #{removed_max.inspect} is not empty or a date on or before #{@date}"
          return
        end
        removal_dates.each do |day|
          @problems << "meta.yml: removed_max #{removed_max.inspect} is before a removal of #{day}" if day > removed_max
        end
      end

      def computed_counts
        by_region = REGIONS.to_h { |r| [r, Set.new] }
        @rows.each { |row| (by_region[row["region"]] ||= Set.new) << row["ins"] }
        {
          "communes" => @rows.map { |r| r["ins"] }.uniq.size,
          "communes_by_region" => by_region.transform_values(&:size),
          "postcodes" => @rows.map { |r| r["postcode"] }.uniq.size,
          "rows" => @rows.size,
          "sections" => @rows.reject { |r| r["section_key"].empty? }.map { |r| [r["ins"], r["section_key"]] }.uniq.size,
          "operators" => @tables["operators.csv"].size,
          "notes" => @tables["notes.csv"].size,
          "sources" => @sources.size,
        }
      end

      def removal_dates
        @changes.select { |_, _, entries| entries.any? { |e| e.start_with?("- removed ") } }.map { |_, day, _| day }
      end

      # --- outputs -------------------------------------------------------------

      def compute_data_date
        stamps = @rows.map { |r| r["changed_at"] }
        ids = @rows.flat_map { |r| r.values_at("elec_operator", "elec_designated", "gas_operator") }.reject(&:empty?).to_set
        stamps += @operators.values.select { |op| ids.include?(op["id"]) }.map { |op| op["changed_at"] }
        regions = @rows.map { |r| r["region"] }.to_set
        keys = @rows.map { |r| r["note_key"] }.reject(&:empty?).to_set
        @notes.each_value do |note|
          stamps << note["changed_at"] if keys.include?(note["key"]) || regions.include?(DsoPages.dataset_region(note["key"]))
        end
        stamps += @sources.map { |s| s["changed_at"] }
        stamps << @meta["removed_max"] unless @meta["removed_max"].to_s.empty?
        stamps.max
      end

      def browser_payload
        postcodes = {}
        @rows.each do |row|
          (postcodes[row["postcode"]] ||= []) << row.values_at(*JSON_COLS)
        end
        communes = {}
        @rows.sort_by { |r| r["ins"] }.each do |row|
          communes[row["ins"]] ||= row.values_at(*JSON_COMMUNE_COLS)
        end
        {
          "format" => 1,
          "meta" => public_meta,
          "cols" => JSON_COLS,
          "commune_cols" => JSON_COMMUNE_COLS,
          "postcodes" => postcodes,
          "communes" => communes,
          "operators" => @operators.transform_values { |op| op.slice(*JSON_OPERATOR_KEYS) },
          "notes" => @notes.transform_values { |note| note.slice("fr", "nl", "de", "en") },
        }
      end

      def sources_for_page
        @sources.map { |s| s.slice("id", "role", "publisher", "title", "url", "retrieved_at", "license", "note") }
      end

      def label_problems(labels, lang)
        return ["grd_tool is missing"] unless labels.is_a?(Hash)

        problems = []
        regions = @rows.map { |r| r["region"] }.uniq
        regions.each do |region|
          problems << "regions.#{region}" if labels.dig("regions", region).to_s.empty?
          code = REGION_REGULATOR[region]
          problems << "regulators.#{code}.name" if labels.dig("regulators", code, "name").to_s.empty?
          url = labels.dig("regulators", code, "url").to_s
          problems << "regulators.#{code}.url must be https" unless url.empty? || HTTPS_RE.match?(url)
        end
        @rows.map { |r| r["province"] }.uniq.reject(&:empty?).each do |code|
          problems << "provinces.#{code}" if labels.dig("provinces", code).to_s.empty?
        end
        @rows.flat_map { |r| r["flags"].split("|") }.uniq.each do |flag|
          problems << "flags.#{flag}" if labels.dig("flags", flag).to_s.empty?
        end
        problems.map { |p| "#{lang}: grd_tool.#{p}" }
      end

      def table(lang, labels)
        by_ins = @rows.group_by { |r| r["ins"] }
        REGIONS.filter_map do |region|
          communes = by_ins.select { |_, rows| rows.first["region"] == region }
          next if communes.empty?

          provinces = communes.group_by { |_, rows| rows.first["province"] }.map do |code, list|
            entries = list.map { |ins, rows| commune_entry(ins, rows, lang, labels) }
            {
              "code" => code,
              "name" => code.empty? ? nil : labels.dig("provinces", code),
              "communes" => entries.sort_by { |c| [DsoPages.fold(c["name"]), c["ins"]] },
            }
          end
          regulator = REGION_REGULATOR[region]
          {
            "code" => region,
            "name" => labels.dig("regions", region),
            "regulator" => { "code" => regulator, "name" => labels.dig("regulators", regulator, "name"),
                             "url" => labels.dig("regulators", regulator, "url") },
            "notes" => dataset_notes(region, lang),
            "communes_count" => communes.size,
            "provinces" => provinces.sort_by { |p| [DsoPages.fold(p["name"].to_s), p["code"]] },
          }
        end
      end

      def dataset_notes(region, lang)
        @notes.keys.sort.select { |key| DsoPages.dataset_region(key) == region }
              .map { |key| { "key" => key, "text" => @notes[key][lang] } }
      end

      def commune_entry(ins, rows, lang, labels)
        first = rows.first
        region = first["region"]
        names = { "fr" => first["commune_fr"], "nl" => first["commune_nl"], "de" => first["commune_de"] }
        sections = rows.reject { |r| r["section_key"].empty? }.uniq { |r| r["section_key"] }
        section_name = lambda do |row|
          DsoPages.local_name({ "fr" => row["section_fr"], "nl" => row["section_nl"], "de" => row["section_de"] },
                              lang, region)
        end
        units = sections.empty? ? [first] : sections.sort_by { |r| [DsoPages.fold(section_name.call(r)), r["section_key"]] }
        flags = FLAGS.select { |flag| units.any? { |u| u["flags"].split("|").include?(flag) } }
        note_keys = units.map { |u| u["note_key"] }.reject(&:empty?).uniq
        {
          "ins" => ins,
          "anchor" => "ins-#{ins}",
          "name" => DsoPages.local_name(names, lang, region),
          "names" => names,
          "postcodes" => rows.map { |r| r["postcode"] }.uniq.sort,
          "has_sections" => !sections.empty?,
          "elec" => groups(units, %w[elec_operator elec_designated], section_name) { |unit|
            { "operator" => operator_entry(unit["elec_operator"]),
              "designated" => operator_entry(unit["elec_designated"]),
              "operator_differs" => unit["elec_operator"] != unit["elec_designated"] }
          },
          "gas" => groups(units, %w[gas_status gas_operator], section_name) { |unit|
            { "status" => unit["gas_status"],
              "operator" => unit["gas_operator"].empty? ? nil : operator_entry(unit["gas_operator"]) }
          },
          "flags" => flags.map { |flag| { "code" => flag, "label" => labels.dig("flags", flag) } },
          "notes" => note_keys.map { |key| { "key" => key, "text" => @notes[key][lang] } },
          "valid_from" => units.map { |u| u["valid_from"] }.reject(&:empty?).uniq.sort,
        }
      end

      # Units with the same answer share one entry: "sections" names them, and
      # is empty when the entry covers the whole commune ("all" is then true).
      def groups(units, columns, section_name)
        units.group_by { |u| u.values_at(*columns) }.map do |_, members|
          all = members.size == units.size
          yield(members.first).merge(
            "all" => all,
            "sections" => all || members.first["section_key"].empty? ? [] : members.map { |m| section_name.call(m) }
          )
        end
      end

      def operator_entry(id)
        op = @operators[id]
        { "id" => id, "name" => op["name"], "legal_name" => op["legal_name"], "website" => op["website"] }
      end
    end

    def self.valid_date?(value)
      return false unless value.is_a?(String) && DATE_RE.match?(value)

      Date.iso8601(value)
      true
    rescue Date::Error
      false
    end

    def self.version_key(version)
      match = VERSION_RE.match(version)
      [match[1].to_i, match[2].to_i, match[3].to_i, match[4] ? 0 : 1]
    end

    def self.dataset_region(key)
      match = DATASET_NOTE_RE.match(key.to_s)
      match && match[1].upcase
    end
  end
end
