---
title: 'Devstral'
name: 'Devstral'
slug: 'devstral'
subtitle: 'Offenes Modell von Mistral für agentische Programmierung und das Erkunden von Codebasen'
description: 'Offenes Modell von Mistral für agentische Programmierung und das Erkunden von Codebasen'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/devstral/'
price: 'Free'
rank: 6
release_date: '2025-05-21'
param_count: '24B'
context_window_tokens: 128000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0.3
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, agentic, api]
i18n_source: '10cd7f3fca31'
---

Devstral ist ein Code-Modell mit 24 Milliarden Parametern, das Mistral AI am 21. Mai 2025 gemeinsam mit All Hands AI veröffentlichte, dem Team hinter dem OpenHands-Agentenframework. Anders als die meisten Code-Modelle, die vor allem auf Autovervollständigung oder Codegenerierung in einem Schritt abgestimmt sind, wurde Devstral speziell für agentisches Programmieren trainiert: Es erkundet Codebasen über mehrere Dateien hinweg, nutzt Werkzeuge und erledigt mehrstufige Softwareentwicklungsaufgaben. Bei SWE-bench Verified erzielte es 46,8 Prozent und übertraf damit alle offenen Modelle, die bei der Veröffentlichung verfügbar waren, sowie einige größere proprietäre Modelle.

Mistral veröffentlichte die Gewichte unter Apache 2.0. Das Modell ist klein genug, um auf einer einzelnen leistungsstarken Consumer-GPU zu laufen, und wurde dadurch zu einer beliebten Basis für lokal ausgeführte Programmieragenten. Später folgten Devstral Small 1.1 und das größere Devstral 2 mit weiter verbesserten SWE-bench-Werten. Das ursprüngliche Devstral bleibt als eines der ersten offenen Modelle bemerkenswert, das eigens für agentische Softwareentwicklung statt allgemeine Codevervollständigung gebaut wurde.
