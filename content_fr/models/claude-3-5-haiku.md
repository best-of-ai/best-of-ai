---
title: 'Claude 3.5 Haiku'
name: 'Claude 3.5 Haiku'
slug: 'claude-3-5-haiku'
subtitle: 'Le modèle rapide et peu cher d''Anthropic, au niveau de l''ancien Claude 3 Opus sur certains benchmarks'
description: 'Le modèle rapide et peu cher d''Anthropic, au niveau de l''ancien Claude 3 Opus sur certains benchmarks'
company: 'anthropic'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.anthropic.com/claude/haiku'
price: 'Paid'
rank: 6
release_date: '2024-11-04'
param_count: 'Undisclosed'
context_window_tokens: 200000
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.8
output_price_usd_per_m: 4
api_available: true
humaneval_score: 88.1
lmarena_score: 1240
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'API']
date: '2026-07-16'
tags: [llm, low-latency, foundation-model, api]
extra_model_types: ['Code']
i18n_source: '43df5415f16a'
---

Claude 3.5 Haiku est le modèle rapide et peu coûteux d'Anthropic dans la famille Claude 3.5, publié en octobre 2024 en même temps qu'un Claude 3.5 Sonnet revu. Anthropic l'a construit pour remplacer Claude 3 Haiku comme option la moins chère et la plus rapide de la gamme, tout en comblant une bonne partie de l'écart de capacité avec les modèles plus grands. Sur des évaluations de code comme SWE-bench Verified, Claude 3.5 Haiku se plaçait au niveau du Claude 3.5 Sonnet d'origine et dépassait plusieurs modèles plus grands disponibles au lancement. Anthropic annonçait un score de 88,1 % à HumanEval pour la génération de code.

Le modèle garde la fenêtre de contexte de 200 000 tokens, commune à la ligne Claude 3.5, et il est tarifé à 0,80 $ par million de tokens d'entrée et 4 $ par million de tokens de sortie. À sa sortie, c'était l'un des modèles proches de la frontière les moins chers du marché. Il vise des usages à fort volume et sensibles à la latence, comme le support client, la modération de contenu et l'extraction de données, là où la vitesse de réponse et le coût par appel comptent plus que le dernier cran de qualité de raisonnement. Il est disponible via l'API d'Anthropic, claude.ai et des plateformes cloud, dont AWS Bedrock.
