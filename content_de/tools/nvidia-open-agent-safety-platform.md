---
title: NVIDIA Open Agent Safety Platform
name: NVIDIA Open Agent Safety Platform
subtitle: Open-Source-Sicherheitsschicht, die problematische KI-Agenten in Millisekunden isolieren kann
slug: nvidia-open-agent-safety-platform
description: NVIDIAs Open Agent Safety Platform kombiniert OpenShell, eine offene Laufzeitumgebung zur Abschirmung von Agenten, mit Sentry. Diese Überwachungsebene läuft getrennt vom Agentenrechner auf
  BlueField-DPUs und kann einen Agenten isolieren.
website: https://developer.nvidia.com/
company: nvidia
logo_url: ''
category: cybersecurity
category_name: Cybersicherheit
price: Free
featured: false
rank: 5
alternatives:
- lakera
- patronus-ai
- giskard
- nightfall
date: '2026-09-28'
tags:
- ai_powered
- intelligent
- platform
- tool
- service
- solution
- saas
- online
i18n_source: '9264e993765c'
---

Die Plattform reagiert auf ein Sicherheitsrisiko: Autonome Agenten, die Befehle ausführen und auf Daten zugreifen können, brauchen Grenzen, die ein kompromittierter Agent nicht selbst ausschalten kann. OpenShell ist eine quelloffene Laufzeitumgebung, die jedem Agenten eine eigene Sandbox mit richtlinienbasierten Berechtigungen zuweist. Ein Prüfer stellt sicher, dass gewährte Rechte nicht ungewollt kombiniert werden können.

Sentry setzt Kontrollen außerhalb des Agentenrechners durch. Es läuft auf BlueField-Datenverarbeitungseinheiten, die vom Host getrennt sind, und kann so das Verhalten beobachten und einen Agenten schnell isolieren, selbst wenn der Host kompromittiert wurde. NVIDIA beschreibt die Lösung als Referenzdesign; zahlreiche Partner integrieren die Komponenten.

Die Software ist quelloffen, die Hardwarekomponente erfordert NVIDIA-Infrastruktur. Eine konsistente Berechtigungsprüfung beweist nicht, dass ein Agent in jeder Hinsicht sicher ist; die Aktionen der Agenten müssen weiterhin geprüft werden. Alternativen sind Sandbox-Werkzeuge wie E2B und Daytona, Sandbox-Lösungen von Anthropic und OpenAI sowie auf Agentensicherheit spezialisierte Start-ups. NVIDIAs Plattform eignet sich für Organisationen, die Agenten mit starker Isolation einsetzen.
