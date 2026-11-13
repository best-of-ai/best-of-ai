---
title: 'GLM-4.6'
name: 'GLM-4.6'
slug: 'glm-4-6'
subtitle: "Le modèle à poids ouverts bon marché de Zhipu, pour le code au quotidien"
description: "Le modèle à poids ouverts bon marché de Zhipu, pour le code au quotidien"
company: 'zhipu-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2025-09-30'
param_count: '355B (MoE, ~32B active)'
context_window_tokens: 200000
modality: [text, image, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 1.75
api_available: true
humaneval_score: 85.0
lmarena_score: 1320
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '89b99962ef6e'
---

GLM-4.6 est le modèle à poids ouverts bon marché de Zhipu (Z.ai), publié le 30 septembre 2025 comme mise à jour de GLM-4.5. Il utilise un mélange d'experts, avec environ 355 milliards de paramètres au total et environ 32 milliards actifs par token, et sa fenêtre de contexte est passée de 128 000 à 200 000 tokens pour tenir des sessions d'agents plus longues. Le modèle traite le texte, les images et le code, et Zhipu l'a ajusté en particulier pour l'usage d'outils dans des assistants de code comme Claude Code, Cline et Roo Code.

Sur les benchmarks de code, il se place près du haut du champ à poids ouverts : il mène LiveCodeBench v6 et reste compétitif face à DeepSeek-V3.1-Terminus et Claude Sonnet 4 sur plusieurs tâches d'agents. Son intérêt principal est le prix : bien en dessous d'un dollar par million de tokens d'entrée, il est bien moins cher que la plupart des modèles phares propriétaires, tout en restant utilisable pour du vrai travail de code. C'est pour cela qu'on le croise souvent dans l'outillage des développeurs, en auto-hébergé comme via API.
