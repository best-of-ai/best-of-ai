---
title: 'GLM-5.2'
name: 'GLM-5.2'
slug: 'glm-5-2'
subtitle: "Le modèle phare à poids ouverts de Zhipu, sorti en même temps que Kimi K2.7 au milieu de 2026"
description: "Le modèle phare à poids ouverts de Zhipu, sorti en même temps que Kimi K2.7 au milieu de 2026"
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-06-13'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 1.4
output_price_usd_per_m: 4.4
api_available: true
mmlu_score: 91.72
humaneval_score: 88.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, coding, self-hosted]
extra_model_types: ['Code']
i18n_source: 'd5b4b307c39a'
---

GLM-5.2 est le modèle phare à poids ouverts de Zhipu AI, publié le 13 juin 2026 sous licence MIT. C'est un mélange d'experts d'environ 744 milliards de paramètres au total, dont environ 40 milliards actifs par token, et il sort avec une fenêtre de contexte de 1 million de tokens, très au-delà des 128 000 tokens de son prédécesseur GLM-4.6. Zhipu l'a construit pour les agents de programmation à long horizon, et l'a entraîné pendant des mois sur des scénarios d'ingénierie logicielle avec des agents, plutôt que sur le chat général.

Sur les benchmarks, il marque 91,72 % sur MMLU, 80,3 % sur GPQA Diamond et 62,1 % sur SWE-bench Pro. Ce dernier dépasse les 58,6 % annoncés pour GPT-5.5. Zhipu tarife l'accès à l'API à 1,40 $ par million de tokens d'entrée et 4,40 $ par million de tokens de sortie, une fraction de ce que facturent des modèles propriétaires comparables, et l'entreprise présente l'ensemble poids ouverts et performance en code comme un défi direct aux modèles frontier fermés d'OpenAI et d'Anthropic.
