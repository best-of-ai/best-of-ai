---
title: 'Arctic'
name: 'Arctic'
slug: 'arctic'
subtitle: 'Das offene Unternehmensmodell von Snowflake, optimiert für SQL und RAG'
description: 'Das offene Unternehmensmodell von Snowflake, optimiert für SQL und RAG'
company: 'snowflake-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.snowflake.com/en/blog/arctic-open-efficient-foundation-language-models-snowflake/'
price: 'Free'
rank: 4
release_date: '2024-04-24'
param_count: '480B (17B active)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Snowflake Cortex']
date: '2026-07-16'
tags: [llm, open-weight, enterprise, self-hosted]
i18n_source: '083cf9082048'
---
Arctic ist ein großes Sprachmodell, das Snowflake im April 2024 veröffentlichte. Es wurde für Unternehmensaufgaben wie SQL-Generierung, Programmierung und das Befolgen von Anweisungen statt für allgemeine Chats entwickelt. Das Modell verwendet eine Mixture-of-Experts-Architektur mit insgesamt 480 Milliarden Parametern in 128 Experten, von denen pro Token nur etwa 17 Milliarden aktiv sind. Dadurch bleiben die Inferenzkosten im Vergleich zu dichten Modellen ähnlicher Größe niedrig. Snowflake veröffentlichte sowohl Basis- als auch Instruct-Checkpoints unter Apache 2.0. Die Gewichte lassen sich dadurch selbst hosten oder über Snowflake Cortex ausführen. Auf dem Spider-Text-zu-SQL-Benchmark erreichte es etwa 79 Prozent Genauigkeit. Snowflake positionierte es als Möglichkeit, leistungsfähige offene Modelle in Data Warehouses einzusetzen, ohne Abfragen an eine Drittanbieter-API zu senden. Das Modell nimmt ein kürzeres Kontextfenster von 4K Tokens und schwächere allgemeine Chatfähigkeiten zugunsten starker Leistung bei den eng umrissenen Unternehmensaufgaben in Kauf, für die es entwickelt wurde.
