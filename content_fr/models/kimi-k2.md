---
title: 'Kimi K2'
name: 'Kimi K2'
slug: 'kimi-k2'
subtitle: "Modèle de base à poids ouverts d'origine de la génération K2 chez Moonshot"
description: "Modèle de base à poids ouverts d'origine de la génération K2 chez Moonshot"
company: 'moonshot-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 7
release_date: '2025-07-11'
param_count: '1T (32B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.2
api_available: true
humaneval_score: 85.0
lmarena_score: 1340
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: '611eb2c97d06'
---

Kimi K2 est le modèle de base d'origine de la génération K2 chez Moonshot AI, sorti en juillet 2025 comme l'un des plus grands modèles de langage à poids ouverts disponibles alors. Il utilise un mélange d'experts d'environ 1 billion de paramètres au total et 32 milliards actifs par token, et il prend en charge une fenêtre de contexte de 128 000 tokens. Moonshot l'a construit autour d'usages agentiques, comme les appels d'outils et l'exécution de tâches en plusieurs étapes, plutôt que le chat pur. Sur des benchmarks de code comme MultiPL-E, la variante multilingue de HumanEval, il se plaçait près des meilleurs modèles fermés de cet été-là. Les poids sont sous une licence MIT modifiée, donc les entreprises peuvent le télécharger, l'ajuster par fine-tuning et l'auto-héberger au lieu de passer par l'API de Moonshot. Il est devenu la base sur laquelle se sont appuyées les sorties suivantes de Moonshot, dont K2.5, K2.6 et K2.7 Code.
