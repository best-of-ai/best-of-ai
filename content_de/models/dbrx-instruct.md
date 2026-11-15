---
title: 'DBRX Instruct'
name: 'DBRX Instruct'
slug: 'dbrx-instruct'
subtitle: 'Instruction-tuned Variante des offenen DBRX-Modells von Databricks'
description: 'Instruction-tuned Variante des offenen DBRX-Modells von Databricks'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 4
release_date: '2024-03-27'
param_count: '132B (36B active)'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Databricks Open Model License'
api_available: true
mmlu_score: 73.7
humaneval_score: 70.1
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Databricks']
date: '2026-07-16'
tags: [llm, open-weight, instruction-tuned, self-hosted]
extra_model_types: ['Code']
i18n_source: '2f1996df20fb'
---
DBRX Instruct ist die feinabgestimmte, chatfertige Version von DBRX, die Databricks im März 2024 zusammen mit dem DBRX-Basismodell veröffentlichte. Es verwendet eine fein aufgelöste Mixture-of-Experts-Architektur mit insgesamt 132 Milliarden Parametern, von denen pro Token nur 36 Milliarden aktiv sind. Trainiert wurde es mit zwölf Billionen Tokens aus Text und Code. Databricks stimmte das Modell gezielt auf das Befolgen von Anweisungen und Gespräche über mehrere Dialogrunden ab. Bei der Veröffentlichung meldete das Unternehmen, dass es GPT-3.5 bei MMLU (73,7 gegenüber 70,0 Prozent) und HumanEval (70,1 gegenüber 48,1 Prozent) übertraf. Das Modell unterstützt ein Kontextfenster von 32.000 Tokens und wird unter der Databricks Open Model License bereitgestellt, die kommerzielle Nutzung mit Einschränkungen für sehr große Bereitstellungen erlaubt. Unternehmen können es über die Plattform von Databricks verwenden oder die Gewichte von Hugging Face selbst hosten.
