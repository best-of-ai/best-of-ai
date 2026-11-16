---
title: 'Claude Opus 4.5'
name: 'Claude Opus 4.5'
slug: 'claude-opus-4-5'
subtitle: 'Le modèle de niveau Opus d''Anthropic qui a baissé les tarifs des deux tiers tout en menant SWE-bench'
description: 'Le modèle de niveau Opus d''Anthropic qui a baissé les tarifs des deux tiers tout en menant SWE-bench'
company: 'anthropic'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.anthropic.com/news/claude-opus-4-5'
price: 'Paid'
rank: 9
release_date: '2025-11-24'
param_count: 'Undisclosed'
context_window_tokens: 200000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 5
output_price_usd_per_m: 25
api_available: true
lmarena_score: 1390
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'Google Vertex AI', 'API']
date: '2026-07-25'
tags: [llm, reasoning, frontier-model, api, coding]
extra_model_types: ['Code']
i18n_source: '2e664c1bdf44'
---

Claude Opus 4.5 est le modèle de niveau Opus qu'Anthropic a publié le 24 novembre 2025, et le changement principal était le prix : les tokens d'entrée sont passés à 5 $ par million et ceux de sortie à 25 $ par million, une baisse des deux tiers par rapport au tarif de 15 $ / 75 $ d'Opus 4.1. Au lancement, il a obtenu 80,9 % à SWE-bench Verified, devant les 76,2 % de Gemini 3 Pro et les 77,9 % de GPT-5.1 Codex Max sur le même benchmark. Anthropic a ajouté un paramètre « effort », qui permet de monter ou de baisser la profondeur de raisonnement à chaque requête. Il a gardé la fenêtre de contexte de 200 000 tokens et la prise en charge des images des Opus précédents, et il est sorti avec une série de mises à jour de Claude Code, visant des sessions de programmation autonomes plus longues. Anthropic l'a suivi d'Opus 4.6 en février 2026 et d'Opus 4.7 en avril, chacun au même tarif de 5 $ / 25 $, en poussant encore les scores de code.
