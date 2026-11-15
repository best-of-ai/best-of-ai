---
title: 'Code Llama'
name: 'Code Llama'
slug: 'code-llama'
subtitle: 'Programmierspezialisierte Llama-Variante von Meta mit offenen Gewichten'
description: 'Programmierspezialisierte Llama-Variante von Meta mit offenen Gewichten'
company: 'meta-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://ai.meta.com/blog/code-llama-large-language-model-coding/'
price: 'Free'
rank: 6
release_date: '2023-08-24'
param_count: '34B'
context_window_tokens: 100000
modality: [text, code]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
humaneval_score: 53.7
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: 'f77a90c92a53'
---

Code Llama ist Metas auf Programmierung ausgerichtete Variante von Llama 2 und erschien im August 2023. Es wurde auf Grundlage der Llama-2-Gewichte mit zusätzlichen codeintensiven Daten trainiert. Zum Start gab es drei Größen – 7, 13 und 34 Milliarden Parameter – jeweils als Basismodell, auf Python spezialisierte Variante und instruktionsoptimierte Version für Programmierhilfe im Chat. Später ergänzte Meta eine Variante mit 70 Milliarden Parametern. Eine wichtige Änderung gegenüber Llama 2 war die Erweiterung des Kontextfensters von 4.096 auf bis zu 100.000 Tokens durch Anpassungen an den RoPE-Positions-Embeddings. Dadurch eignete sich das Modell besser dazu, lange Dateien oder ganze Codebasen in einem Durchgang zu lesen und zu bearbeiten.

Im HumanEval-Benchmark erreichte das Modell mit 34 Milliarden Parametern 53,7 Prozent pass@1 und lag bei Veröffentlichung ungefähr auf dem Niveau von GPT-3.5, aber deutlich hinter GPT-4. Code Llama steht unter derselben Llama-2-Community-Lizenz wie das Basismodell. Sie erlaubt den meisten Unternehmen die kommerzielle Nutzung; die Gewichte können kostenlos von Hugging Face heruntergeladen werden. Als eines der ersten weithin eingesetzten offenen Programmiermodelle setzte es einen Maßstab, an dem spätere Modelle wie Codestral und DeepSeek Coder gemessen wurden.
