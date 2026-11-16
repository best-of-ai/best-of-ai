---
title: 'Codestral Mamba'
name: 'Codestral Mamba'
slug: 'codestral-mamba'
subtitle: 'Programmiermodell von Mistral auf Basis der Mamba-Zustandsraumarchitektur statt eines Transformers'
description: 'Programmiermodell von Mistral auf Basis der Mamba-Zustandsraumarchitektur statt eines Transformers'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral-mamba/'
price: 'Free'
rank: 6
release_date: '2024-07-16'
param_count: '7B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.25
output_price_usd_per_m: 0.25
api_available: true
humaneval_score: 75.0
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, api]
i18n_source: '071ce3f5be62'
---

Codestral Mamba ist ein Codegenerierungsmodell von Mistral AI aus dem Juli 2024. Besonders ist seine Architektur: Statt der Transformer-Architektur, die fast alle anderen Programmiermodelle verwenden, basiert es auf Mamba, einem Zustandsraummodell. Zustandsraummodelle verarbeiten Sequenzen mit linearer statt quadratischer Skalierung zur Sequenzlänge. Dadurch nimmt die Inferenzgeschwindigkeit bei wachsendem Kontext weniger stark ab. Mistral stattete das Modell mit rund sieben Milliarden Parametern und einem Kontextfenster von 256.000 Tokens aus. Das Unternehmen berichtete, dass der Abruf von Informationen aus dem Kontext selbst bei dieser Länge zuverlässig funktioniert.

Bei HumanEval erreicht Codestral Mamba etwa 75 Prozent pass@1 und kann damit mit deutlich größeren transformerbasierten Code-Modellen mithalten. Es steht unter Apache 2.0. Die Gewichte lassen sich kostenlos herunterladen, feinabstimmen und kommerziell einsetzen. Über die Mistral-API kostet es 0,25 US-Dollar pro Million Ein- und Ausgabetokens. Mistral präsentierte es als Machbarkeitsnachweis dafür, dass Zustandsraumarchitekturen bei realen Programmieraufgaben mit Transformern konkurrieren und bei langen Kontexten – etwa der Analyse großer Repositorys – schnellere und günstigere Inferenz bieten können.
