---
title: Cloudflare Kitesurf
name: Cloudflare Kitesurf
subtitle: Cloudbrowser für KI-Agenten statt für Menschen
slug: cloudflare-kitesurf
description: Kitesurf ist ein von Cloudflare entwickelter Browser, den KI-Agenten steuern. Er läuft auf Cloudflare Workers
  und entfernt Bestandteile gewöhnlicher Browser, die Agenten nicht benötigen, etwa Tabs und Erweiterungen.
website: https://kitesurf.cloudflare.app/
company: cloudflare
logo_url: ''
category: devtools
category_name: Entwicklertools
price: Free
featured: false
rank: 5
alternatives:
- browserbase
- multion
- e2b-ai
- firecrawl
- openai-operator
date: '2026-08-07'
tags:
- developer_tools
- code_generation
- infrastructure
- deployment
- development
- devops
- ci_cd
- cloud
- api
- free_tier
- cloud_based
- machine_learning
i18n_source: '8918f291d1e6'
---

Kitesurf denkt den Browser für Software neu. Die meisten Automatisierungswerkzeuge steuern einen vollständigen Desktopbrowser, der ressourcenintensiv und für Menschen entwickelt ist. Kitesurf ist ein schlanker Browser, der auf der Workers-Plattform von Cloudflare läuft. Agenten können Seiten öffnen, lesen, anklicken und Texte eingeben, ohne eine vollständige Chrome-Instanz zu betreiben.

Kitesurf funktioniert mit vorhandenen Werkzeugen. Clients für Puppeteer, Playwright oder das Model Context Protocol können sich mit kleinen Änderungen über den Browserdienst von Cloudflare verbinden. Jede Seite wird als nicht vertrauenswürdig behandelt und jede Sitzung startet frisch – ein für Agentensicherheit geeigneter Ansatz. Laut Cloudflare benötigt das Tool in Tests weniger Speicher als Chromium.

Kitesurf befindet sich in der Beta und hat Einschränkungen. Es eignet sich nicht für Videowiedergabe, WebGL, lange angemeldete Sitzungen oder Websites, die echte Browser-Fingerabdrücke prüfen. Dafür bleibt der Standardbrowserdienst von Cloudflare die passende Option. Alternativen sind Browserbase, Browserless, Steel und selbst gehostetes Playwright. Kitesurf eignet sich für Entwickler:innen, die Agenten zum Lesen und Bedienen des Webs in großem Maßstab bauen.
