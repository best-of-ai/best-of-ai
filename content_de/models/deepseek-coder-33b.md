---
title: 'DeepSeek-Coder-33B'
name: 'DeepSeek-Coder-33B'
slug: 'deepseek-coder-33b'
subtitle: 'Früheres Programmier-Flaggschiffmodell von DeepSeek vor DeepSeek-Coder-V2'
description: 'Früheres Programmier-Flaggschiffmodell von DeepSeek vor DeepSeek-Coder-V2'
company: 'deepseek'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-Coder'
price: 'Free'
rank: 6
release_date: '2023-11-02'
param_count: '33B'
context_window_tokens: 16384
modality: [text, code]
open_weight: true
license: 'DeepSeek License'
api_available: true
humaneval_score: 79.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-07-16'
tags: [code, open-weight, api, legacy]
i18n_source: 'e1d443d0e69c'
---

DeepSeek-Coder-33B ist ein Programmiermodell, das DeepSeek im November 2023 veröffentlichte, bevor das Unternehmen durch spätere Schlussfolgerungsmodelle bekannt wurde. Es wurde von Grund auf mit zwei Billionen Tokens trainiert, überwiegend Code und natürlicher Sprache. Das Kontextfenster umfasst 16.000 Tokens; projektbezogenes Training ermöglicht Schlussfolgerungen über mehrere Dateien statt einzelner Ausschnitte. Die instruktionsoptimierte Variante erzielte bei HumanEval 79,3 Prozent pass@1 und lag damit vor den meisten damaligen offenen Code-Modellen sowie nahe an GPT-3.5. Sie unterstützt Fill-in-the-Middle-Vervollständigung für Code-Editoren und zahlreiche Programmiersprachen. DeepSeek-Coder-V2 mit größerem MoE-Modell und Kontextfenster hat sie inzwischen abgelöst. Die 33B-Variante bleibt für selbst gehosteten Betrieb auf Hugging Face verfügbar.
