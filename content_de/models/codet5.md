---
title: 'CodeT5+'
name: 'CodeT5+'
slug: 'codet5'
subtitle: 'Open-Weight-Encoder-Decoder-Modellfamilie für Code von Salesforce.'
description: 'Open-Weight-Encoder-Decoder-Modellfamilie für Code von Salesforce.'
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeT5'
price: 'Free'
rank: 3
release_date: '2023-05-13'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
humaneval_score: 30.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '20777365e144'
---

CodeT5+ ist eine Familie offener Code-Modelle von Salesforce Research, die im Mai 2023 als Weiterentwicklung des ursprünglichen Encoder-Decoder-Modells CodeT5 erschien. Die Größen reichen von 220 Millionen bis zu 16 Milliarden Parametern. Das Modell kann als reiner Encoder, reiner Decoder oder vollständiger Encoder-Decoder laufen und deckt dadurch Aufgaben zum Codeverständnis wie Fehlererkennung sowie Codegenerierung wie Vervollständigung und Text-zu-Code-Synthese ab. Das Training kombiniert Span-Denoising, kausales Sprachmodellieren, kontrastives Lernen und Text-Code-Abgleich. Laut Salesforce verschafft dies dem Modell bei Retrieval-Augmented Generation Vorteile gegenüber ähnlich großen Code-Modellen mit reinem Decoder. Die 16B-Variante erzielt bei HumanEval rund 30,9 Prozent pass@1; eine instruktionsoptimierte Version desselben Checkpoints kommt auf über 35 Prozent und schlägt OpenAIs älteres Code-Cushman-001 im selben Benchmark. Die Gewichte stehen unter BSD-3-Clause-Lizenz auf Hugging Face bereit. CodeT5+ war eine der ersten vollständig offenen Alternativen zu proprietären Code-Modellen der Codex-Ära.
