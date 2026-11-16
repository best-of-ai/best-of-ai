---
title: 'Ling-3.0-Flash'
name: 'Ling-3.0-Flash'
slug: 'ling-3-0-flash'
subtitle: "Modèle de raisonnement à poids ouverts et économe d'Ant Group, fait pour des agents d'IA en production"
description: "Modèle de raisonnement à poids ouverts et économe d'Ant Group, fait pour des agents d'IA en production"
company: 'ant-group'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.antgroup.com'
price: 'Free'
rank: 6
release_date: '2026-07-23'
param_count: '124B (5.1B active)'
context_window_tokens: 262144
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.075
output_price_usd_per_m: 0.22
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'OpenRouter']
date: '2026-08-09'
tags: [llm, open-weight, reasoning, agentic, mixture-of-experts, efficiency]
extra_model_types: ['Code']
i18n_source: '368f5f371b66'
---

Ling-3.0-Flash est la dernière entrée de la gamme Ling d'Ant Group, centrée sur l'efficacité, construite par son labo inclusionAI et présentée le 23 juillet 2026 comme modèle de fondation à raisonnement hybride pour des charges d'agents d'IA en production. C'est un mélange d'experts de 124 milliards de paramètres qui n'active qu'environ 5,1 milliards de paramètres par token, prend en charge nativement une fenêtre de contexte de 256 000 tokens qui peut monter jusqu'à 1 million, et Ant dit qu'il égale ou dépasse des modèles de deux à trois fois son nombre de paramètres sur le raisonnement, le suivi d'instructions et les benchmarks de long contexte. Un système de cache hiérarchique au niveau du cluster réduit le temps jusqu'au premier token sur les longues conversations de 60 à 80 %. Ant a tarifé l'API de première main à 0,075 $ par million de tokens d'entrée et 0,22 $ par million de tokens de sortie, parmi les tarifs les plus bas mesurés pour un modèle à 38 ou plus sur l'Artificial Analysis Intelligence Index, et a publié les poids sur Hugging Face sous licence MIT.
