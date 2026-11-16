---
title: Cloudflare AI Gateway
name: Cloudflare AI Gateway
subtitle: Beobachtbarkeit, Kontrollen und Multi-Provider-Routing für KI-Anwendungen
slug: cloudflare-ai-gateway
description: Cloudflare AI Gateway sitzt zwischen einer Anwendung und KI-Modellanbietern. Analysen, Protokolle, Caching, Ratenbegrenzungen,
  Wiederholungen und Modell-Fallbacks helfen Entwickler:innen, Nutzung zu beobachten und Kosten zu steuern.
website: https://developers.cloudflare.com/ai-gateway/
company: cloudflare
logo_url: ''
category: devtools
category_name: Entwicklertools
price: Freemium
featured: false
rank: 5
alternatives:
- portkey
- litellm
- helicone
- langfuse
- openrouter
- vercel-ai-platform
- eden-ai
date: '2026-07-17'
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
- cloud_based
- analytics
- model_based
i18n_source: '76831d31774b'
---

AI Gateway ist ein Proxy für Aufrufe von Sprachmodellen. Entwickler:innen richten Anfragen ihrer App an eine Cloudflare-Adresse statt direkt an den Anbieter. Das Gateway leitet sie weiter und protokolliert den Ablauf. Ein Dashboard zeigt Anfragen, Tokens, Kosten und Fehler über Anbieter wie OpenAI, Anthropic und Google hinweg.

Zusätzliche Kontrollfunktionen umfassen Caching, das gespeicherte Antworten auf wiederholte Anfragen zurückgibt und so Kosten und Zeit spart, sowie Ratenbegrenzungen zum Schutz des Budgets. Wiederholungen und Fallbacks wechseln bei einem Ausfall zu einem anderen Modell. Protokolle helfen beim Debuggen von Prompts; Schutzregeln und Schlüsselverwaltung unterstützen die Sicherheit.

Die Kernfunktionen sind in Cloudflare-Tarifen enthalten, viele davon kostenlos, teils mit Speicherlimits für Protokolle. AI Gateway eignet sich für Produktivsysteme, die mehrere Modelle aufrufen. Alternativen sind Portkey, LiteLLM, Helicone, OpenRouter und Kong AI Gateway. Cloudflare AI Gateway eignet sich für Entwickler:innen, die Datenverkehr zu Modellen nachvollziehen und steuern möchten.
