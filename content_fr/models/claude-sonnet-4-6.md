---
title: 'Claude Sonnet 4.6'
name: 'Claude Sonnet 4.6'
slug: 'claude-sonnet-4-6'
subtitle: 'Le modèle Sonnet par défaut d''Anthropic, fait pour approcher les résultats de classe Opus à un cinquième du prix'
description: 'Le modèle Sonnet par défaut d''Anthropic, fait pour approcher les résultats de classe Opus à un cinquième du prix'
company: 'anthropic'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.anthropic.com/news/claude-sonnet-4-6'
price: 'Paid'
rank: 9
release_date: '2026-02-17'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 3
output_price_usd_per_m: 15
api_available: true
lmarena_score: 1380
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'Google Vertex AI', 'API']
date: '2026-07-25'
tags: [llm, reasoning, frontier-model, api, agentic]
extra_model_types: ['Code']
i18n_source: '1c6e036cc247'
---

Claude Sonnet 4.6 est sorti le 17 février 2026 et est devenu le modèle par défaut de claude.ai et de Claude Cowork, le produit d'espace de travail d'Anthropic. Il égale la fenêtre de contexte de 1 million de tokens d'Opus 4.6 et la limite de sortie de 128 000 tokens, au tarif de 3 $ par million de tokens d'entrée et 15 $ par million de tokens de sortie, environ un cinquième du tarif d'Opus 4.6. Sur SWE-bench Verified, il a obtenu 79,6 %, à quelques points du modèle Opus malgré l'écart de prix. Il a aussi affiché 59,1 % à Terminal-Bench 2.0 et 72,5 % à OSWorld-Verified, des benchmarks qui testent des tâches agentiques de terminal et de computer use. Anthropic y a intégré des chaînes de raisonnement étendu qui peuvent aller jusqu'à 100 étapes, pour les développeurs qui veulent la fiabilité du niveau Opus sans en payer le tarif.
