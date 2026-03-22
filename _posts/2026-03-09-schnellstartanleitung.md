---
layout: post
title: "Schnellstartanleitung für OptimCE"
date: 2026-03-09 14:00:00 +0100
author: "OptimCE-Team"
excerpt: "Erfahren Sie, wie Sie OptimCE in wenigen Schritten installieren und konfigurieren, um Ihre Energiegemeinschaft zu verwalten."
categories: [tutorials]
lang: de
ref: quick-start-guide
permalink: /de/aktuelles/2026/03/09/schnellstartanleitung/
---

Diese Anleitung führt Sie durch die Installation und Erstkonfiguration von OptimCE. In wenigen Schritten sind Sie bereit, Ihre Energiegemeinschaft zu verwalten.

## Voraussetzungen

Stellen Sie vor dem Start sicher, dass folgende Software auf Ihrem Rechner installiert ist:

- **Node.js** (Version 18 oder höher)
- **Angular CLI** für das Frontend
- **Python 3.10+** für das analytische Backend (FastAPI)
- **PostgreSQL** als Datenbank
- **Docker** (optional, aber empfohlen zur Vereinfachung des Deployments)

## Installation

Klonen Sie das Haupt-Repository von GitHub und installieren Sie die Abhängigkeiten für jede Komponente. Das Projekt ist in mehrere unabhängige Module gegliedert: das Angular-Frontend, das Haupt-Backend in Node.js/TypeScript und das analytische Backend in FastAPI.

## Erstkonfiguration

Nach Abschluss der Installation müssen Sie die Umgebungsvariablen für jede Komponente konfigurieren: Datenbankverbindung, Authentifizierungsparameter und Konfiguration des Nachrichtensystems.

## Erstellen Sie Ihre erste Gemeinschaft

Melden Sie sich nach dem Deployment in der Administrationsoberfläche an, um Ihre erste Energiegemeinschaft zu erstellen. Anschließend können Sie Mitglieder hinzufügen, deren Zähler konfigurieren und Verteilungsschlüssel für die Energieverteilung festlegen.

## Nächste Schritte

Lesen Sie die vollständige Dokumentation auf GitHub, um erweiterte Funktionen zu entdecken: Integration externer Module, Multi-Tenant-Konfiguration und Anpassung der Benutzeroberfläche.
