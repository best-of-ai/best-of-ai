---
title: 'Herdr'
name: 'Herdr'
subtitle: 'Quelloffene Desktop-App, die Coding-Agenten im Hintergrund weiterlaufen lässt'
slug: 'herdr'
description: 'Herdr ist eine native Open-Source-Desktop-App, mit der Terminals und Coding-Agenten wie Claude Code oder Codex zentral laufen. Die Laufzeitumgebung herdr-core hält Sitzungen auch beim Schließen oder Aktualisieren der App am Laufen.'
website: 'https://herdr.dev/'
company: 'herdr'
logo_url: ''
category: 'devtools'
category_name: 'DevTools'
price: 'Free'
featured: false
rank: 5
alternatives:
  - warp
  - claude-code
  - cursor
  - cline
date: '2026-10-29'
tags: [developer_tools, terminal, coding_agents, open_source, desktop_app, multiplexer, agent_management, productivity, cross_platform, automation]
i18n_source: '3491a22de0f6'
---

Herdr verwaltet die vielen Agentensitzungen, die Entwickler zunehmend starten. Statt zahlreicher Terminalfenster bündelt es Agenten in einer Oberfläche mit Tabs und zeigt – sofern der Agent Statusmeldungen liefert –, ob er arbeitet, fertig ist oder Eingaben benötigt. Unterstützt wird jeder Agent, der in einem Terminal läuft.

Die zentrale Designentscheidung ist herdr-core, ein kleiner Server auf dem eigenen Rechner, der Sitzungen ausführt. Die App ist nur die Oberfläche; ihr Beenden oder Aktualisieren stoppt die Agenten nicht. Eine Terminalversion von Herdr, das ursprüngliche Programm, besteht als separates Programm mit eigenem Server weiter.

Herdr ist unter Apache 2.0 kostenlos und quelloffen und läuft auf macOS, Linux und Windows. Die Desktop-App ist neu, daher sind Änderungen zu erwarten. Bei einem Neustart des Rechners oder Ende des Core-Prozesses enden laufende Programme. Alternativen sind tmux, Zellij, Warp, Conductor und in Agentenwerkzeuge eingebaute Terminal-Multiplexer. Herdr eignet sich für Entwickler, die viele Coding-Agenten parallel einsetzen.
