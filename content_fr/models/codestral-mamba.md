---
title: 'Codestral Mamba'
name: 'Codestral Mamba'
slug: 'codestral-mamba'
subtitle: "Modèle de code de Mistral, bâti sur l'architecture à espace d'états Mamba plutôt que sur un transformeur"
description: "Modèle de code de Mistral, bâti sur l'architecture à espace d'états Mamba plutôt que sur un transformeur"
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral-mamba/'
price: 'Free'
rank: 6
release_date: '2024-07-16'
param_count: '7B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.25
output_price_usd_per_m: 0.25
api_available: true
humaneval_score: 75.0
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, api]
i18n_source: '071ce3f5be62'
---

Codestral Mamba est un modèle de génération de code que Mistral AI a sorti en juillet 2024. Son intérêt tient surtout à l'architecture : au lieu du transformeur qu'utilisent presque tous les autres modèles de code, il repose sur Mamba, une architecture de modèle à espace d'états. Ces modèles traitent les séquences avec un coût linéaire, et non quadratique, selon la longueur. La vitesse d'inférence baisse donc moins vite quand le contexte s'allonge. Mistral l'a taillé à environ 7 milliards de paramètres et lui a donné une fenêtre de contexte de 256 000 tokens. L'entreprise indique des performances de récupération en contexte qui restent fiables même à cette longueur.

Sur HumanEval, Codestral Mamba tourne autour de 75 % en pass@1, au niveau de modèles de code à transformeur bien plus gros. Il est publié sous licence Apache 2.0 : les poids se téléchargent, s'ajustent par fine-tuning et s'utilisent dans un cadre commercial. Il est aussi disponible via l'API de Mistral, à 0,25 $ par million de tokens d'entrée et de sortie. Mistral le présentait comme une preuve de concept. Les architectures à espace d'états peuvent égaler les transformeurs sur de vraies tâches de code, avec une inférence plus rapide et moins chère pour les usages à long contexte, comme le raisonnement sur de grands dépôts.
