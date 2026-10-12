---
layout: page
title: "Open source and self-hosting"
breadcrumb_title: "Open source"
subtitle: "All the code under the Apache 2.0 licence: host OptimCE yourself, connect it to your tools, or let us host it."
description: "OptimCE is open source energy community software under the Apache 2.0 licence: free self-hosting, a REST API, NATS events and four languages."
lang: en
ref: product-open-source
permalink: /en/features/open-source/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Is OptimCE really open source?"
    a: "Yes. All the code is published under the Apache 2.0 licence, in the optimce GitHub organisation: no cut-down edition, no proprietary core. The hosted version and the version you install yourself give access to the same features."
  - q: "Can I use OptimCE in a professional setting?"
    a: "Yes. The Apache 2.0 licence lets you use, modify and redistribute the software, including in a professional setting, provided you keep the licence and copyright notices."
  - q: "What is the difference between OptimCE Cloud and self-hosting?"
    a: "Who hosts the application. OptimCE Cloud runs on our servers, with no installation and no maintenance, and it is free during the alpha. When you self-host, OptimCE runs on your infrastructure, free of charge and without restriction, but you handle hosting, updates and availability."
  - q: "How do I connect OptimCE to my other tools?"
    a: "Through its events or its API. An event-driven architecture (NATS) lets you plug in third-party tools, such as an energy management system, and a REST API lets you integrate OptimCE into your own tools."
---

An energy community entrusts its software with its list of members, their meters, its invoices
and its filings with the regulator. It needs to be able to keep that software if the vendor
changes course, to choose where it is hosted and to connect it to its other tools. OptimCE is open
source software: all its code is published under the Apache 2.0 licence, and the same application
runs on our servers or on yours.

## How OptimCE handles it

### All the code, under the Apache 2.0 licence

There is no cut-down edition and no proprietary core: all of OptimCE's code is published under the
Apache 2.0 licence, in the [optimce](https://github.com/optimce) GitHub organisation. The licence
lets you use, modify and redistribute the software, including in a professional setting. In
return, it asks you to keep the licence and copyright notices, and to flag the files you have
modified.

For a community, this means it is tied to no one: if OptimCE Cloud no longer suits it, it can run
the same application elsewhere.

### On our servers or on yours

The same software can be used in two ways.

- **OptimCE Cloud** is the hosted version, at app.optimce.be: nothing to install, nothing to
  maintain. It is free throughout the alpha phase.
- **Self-hosting** puts OptimCE on your own infrastructure, free of charge and without
  restriction, for good. The installation guide covers deploying the full stack locally with
  Docker Compose.

Both routes give access to the same features. The choice depends mostly on who you are: a
community that simply wants the tool has nothing to install, while a technical team can host the
platform, keep full control of the data or contribute to the code. What is free, and for how long,
is set out on the [pricing]({{ "pricing" | ref_url }}) page.

### One installation, several communities

A single OptimCE installation runs several energy communities. An account can belong to several
communities and switch between them in “My communities”. An organisation that supports
several projects, or that chooses to host OptimCE for others, therefore does not need a separate
installation for each community.

### Connecting your tools

An event-driven architecture (NATS) lets you plug third-party tools into OptimCE, such as an
energy management system. A REST API lets you integrate it into your own tools. A tool the
community already uses can thus exchange data with OptimCE instead of having it typed in again,
at the cost of some integration work.

### An interface in four languages

The interface is available in French, English, Dutch and German, which matters in a country with
three official languages. The emails sent by the platform come in the same four languages.

### Contributing

The installation guide is also meant for teams that want to contribute to the code: the full stack
runs locally with Docker Compose. Translations of the interface are proposed collaboratively on
[Weblate](https://hosted.weblate.org/engage/optimce/), without touching the code.

## What it does not do

**No service guarantee when self-hosting.** On your own servers, you handle hosting, updates and
availability yourself: no service guarantee is provided on that route.

**The installation guide describes a development stack.** Its databases are not persistent: data
resets when the containers restart. For a deployment meant to last, you need to set up persistent
volumes and a backup strategy yourself.

**Open source does not do the work for you.** Hosting software that handles members' data takes
someone to administer it. Without that person, OptimCE Cloud remains the simplest route.

## Frequently asked questions {#faq}

### Is OptimCE really open source?

Yes. All the code is published under the Apache 2.0 licence, in the optimce GitHub organisation:
no cut-down edition, no proprietary core. The hosted version and the version you install yourself
give access to the same features.

### Can I use OptimCE in a professional setting?

Yes. The Apache 2.0 licence lets you use, modify and redistribute the software, including in a
professional setting, provided you keep the licence and copyright notices.

### What is the difference between OptimCE Cloud and self-hosting?

Who hosts the application. OptimCE Cloud runs on our servers, with no installation and no
maintenance, and it is free during the alpha. When you self-host, OptimCE runs on your
infrastructure, free of charge and without restriction, but you handle hosting, updates and
availability.

### How do I connect OptimCE to my other tools?

Through its events or its API. An event-driven architecture (NATS) lets you plug in third-party
tools, such as an energy management system, and a REST API lets you integrate OptimCE into your
own tools.

## Further reading

- [Install OptimCE: quick start guide]({{ "quick-start-guide" | ref_url }}): the prerequisites,
  cloning the repository and the first run, step by step.
- [OptimCE pricing]({{ "pricing" | ref_url }}): what is free today, and what could change.
- [Energy community management software]({{ "features" | ref_url }}): everything OptimCE does
  today.

{% include product-cta.html page_key="open-source" guide="getting-started" title="Try OptimCE without installing anything" %}
