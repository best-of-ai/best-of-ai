---
title: 'GPT-4 Turbo'
name: 'GPT-4 Turbo'
slug: 'gpt-4-turbo'
subtitle: "Successeur de GPT-4, plus rapide et moins cher, avec une plus grande fenêtre de contexte"
description: "Successeur de GPT-4, plus rapide et moins cher, avec une plus grande fenêtre de contexte"
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/new-models-and-developer-products-announced-at-devday/'
price: 'Paid'
rank: 6
release_date: '2023-11-06'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 10
output_price_usd_per_m: 30
api_available: true
mmlu_score: 86.5
humaneval_score: 87.1
lmarena_score: 1250
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['ChatGPT', 'Azure OpenAI', 'API']
date: '2026-07-16'
tags: [llm, foundation-model, api]
extra_model_types: ['Code']
i18n_source: 'dfca7bbe4eb9'
---

GPT-4 Turbo est la mise à jour de GPT-4 qu'OpenAI a annoncée en novembre 2023, lors de sa première conférence pour développeurs. Il a gardé le niveau de capacité de GPT-4, mais a porté la fenêtre de contexte à 128 000 tokens, ajouté une date de coupure des connaissances en avril 2023, et baissé les tarifs à 10 $ par million de tokens d'entrée et 30 $ par million de tokens de sortie, bien en dessous des tarifs d'origine de GPT-4. Il obtient 86,5 % au MMLU et 87,1 % sur HumanEval, et il ajoute l'entrée visuelle : on peut envoyer des images avec le texte dans la même requête.

La grande fenêtre venait avec une limite concrète. Des tests indépendants ont montré que la qualité de l'attention baissait nettement au-delà d'environ 32 000 tokens, donc la fenêtre complète de 128 000 tenait mieux en théorie que dans un usage dense de longs documents. Malgré cela, GPT-4 Turbo est devenu le modèle de classe GPT-4 par défaut pour les développeurs d'API pendant une bonne partie de 2024, en accès direct chez OpenAI, via Azure OpenAI et dans ChatGPT, jusqu'à ce que GPT-4o le remplace comme option recommandée plus tard dans l'année.
