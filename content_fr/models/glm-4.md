---
title: 'GLM-4'
name: 'GLM-4'
slug: 'glm-4'
subtitle: "Le modèle généraliste à poids ouverts de Zhipu en 2024"
description: "Le modèle généraliste à poids ouverts de Zhipu en 2024"
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 5
release_date: '2024-06-05'
param_count: '9B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 72.4
humaneval_score: 71.8
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted]
i18n_source: 'b05c60de4627'
---

GLM-4 est la version à poids ouverts de Zhipu AI de juin 2024, distribuée sous le nom GLM-4-9B, avec des variantes base, chat et long contexte. À 9 milliards de paramètres, il est assez petit pour tourner sur un seul GPU haut de gamme, et Zhipu a indiqué qu'il dépassait le Llama 3 8B de Meta sur des évaluations de sémantique, de maths, de raisonnement et de code. La variante chat gère aussi la navigation web, l'exécution de code et des appels d'outils sur mesure via le function calling, plus une fenêtre de contexte qui va jusqu'à 128 000 tokens.

Le modèle a ajouté 26 langues en plus du chinois et de l'anglais, dont le japonais, le coréen et l'allemand, ce qui a élargi son usage hors du marché d'origine de Zhipu. Publié sous Apache 2.0, GLM-4 est devenu l'un des petits modèles à poids ouverts les plus repris sur Hugging Face, et il a posé l'architecture de base que Zhipu a ensuite agrandie en GLM-4-Plus, GLM-4.5 et GLM-4.6.
