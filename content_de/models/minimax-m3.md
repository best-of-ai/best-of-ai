---
title: 'MiniMax M3'
name: 'MiniMax M3'
slug: 'minimax-m3'
subtitle: 'Erstes offenes Modell mit führender Programmierung, einem Kontextfenster von einer Million Tokens und nativer Multimodalität'
description: 'Erstes offenes Modell mit führender Programmierung, einem Kontextfenster von einer Million Tokens und nativer Multimodalität'
company: 'minimax-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.minimaxi.com/'
price: 'Free'
rank: 8
release_date: '2026-06-01'
param_count: '428B (23B active)'
context_window_tokens: 1000000
modality: [text, image, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 1.2
api_available: true
lmarena_score: 1340
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, long-context, coding]
extra_model_types: ['Code']
i18n_source: 'b89f089ecadf'
---

MiniMax M3 ist ein Mixture-of-Experts-Modell mit offenen Gewichten, das MiniMax im Juni 2026 veröffentlichte. Die Gewichte waren spätestens am 7. Juni auf Hugging Face verfügbar. Das Modell verfügt über rund 428 Milliarden Parameter, von denen pro Token etwa 23 Milliarden aktiv sind; sie verteilen sich auf 256 fein abgestimmte Experten. MiniMax bezeichnet es als erstes Modell mit offenen Gewichten, das Programmierfähigkeiten auf Spitzenniveau, ein Kontextfenster von einer Million Tokens und native multimodale Eingaben für Text, Bilder und Videos vereint. Das Labor berichtet von Ergebnissen von 59 Prozent bei SWE-Bench Pro und 66 Prozent bei Terminal-Bench 2.1. Diese Benchmarks prüfen lang laufende Programmier- und Agentenaufgaben statt einzelner Fragen.

Die Architektur soll Inferenz mit langem Kontext kostengünstig halten: Laut MiniMax macht die Rechenleistung pro Token bei einer Million Tokens nur einen Bruchteil des Werts der vorherigen Generation aus; sowohl Vorverarbeitung als auch Decodierung sind um ein Mehrfaches schneller. Das Modell steht unter Apache 2.0. Über die MiniMax-API kostet es 0,30 US-Dollar pro Million Eingabetokens und 1,20 US-Dollar pro Million Ausgabetokens. Damit positioniert MiniMax es als kostengünstige offene Alternative zu geschlossenen Spitzenmodellen für Programmierung – für Entwicklerinnen und Entwickler, die autonome Coding-Agenten und Werkzeuge für große Codebasen bauen.
