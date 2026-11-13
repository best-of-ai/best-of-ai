---
title: 'Claude Opus 4.8'
name: 'Claude Opus 4.8'
slug: 'claude-opus-4-8'
subtitle: 'Le modèle de niveau Opus le plus capable d''Anthropic, pour l''analyse approfondie et les tâches à long horizon'
description: 'Le modèle de niveau Opus le plus capable d''Anthropic, pour l''analyse approfondie et les tâches à long horizon'
company: 'anthropic'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.anthropic.com/news/claude-opus-4-8'
price: 'Paid'
rank: 9
release_date: '2026-05-28'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 5
output_price_usd_per_m: 25
api_available: true
mmlu_score: 92.4
humaneval_score: 92.5
lmarena_score: 1415
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, reasoning, frontier-model, api]
extra_model_types: ['Code']
i18n_source: '9185c0fd20db'
---

Claude Opus 4.8 est le modèle de niveau Opus le plus capable d'Anthropic, publié le 28 mai 2026 comme mise à jour d'Opus 4.7. Cette mise à jour corrigeait certains travers de ce modèle, commentaires trop verbeux et à-coups dans l'appel d'outils. Il atteint environ 88,6 % à SWE-bench Verified et 69,2 % au SWE-bench Pro, plus dur, devant GPT-5.5 et Gemini 3.1 Pro sur le même test au moment de la sortie. Anthropic indique qu'il signale plus souvent sa propre incertitude, au lieu d'affirmer avec assurance des choses non étayées. Il prend en charge une fenêtre de contexte en entrée de 1 million de tokens, avec jusqu'à 128 000 tokens de sortie. Il a aussi introduit Dynamic Workflows, une fonction en préversion de recherche dans Claude Code : le modèle planifie une grande tâche, puis lance des centaines de sous-agents en parallèle dans une seule session. Le tarif est resté celui de la version précédente, 5 $ par million de tokens d'entrée et 25 $ par million de tokens de sortie, avec un mode plus rapide, « fast mode », à 10 $ / 50 $.
