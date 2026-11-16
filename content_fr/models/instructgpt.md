---
title: 'InstructGPT'
name: 'InstructGPT'
slug: 'instructgpt'
subtitle: "Modèle de 2022 d'OpenAI qui a introduit l'instruction-tuning par RLHF à grande échelle"
description: "Modèle de 2022 d'OpenAI qui a introduit l'instruction-tuning par RLHF à grande échelle"
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/instruction-following/'
price: 'Paid'
rank: 5
release_date: '2022-01-27'
param_count: '175B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [API]
runs_at_home: false
platforms: ['API']
date: '2026-07-16'
tags: [llm, foundation-model, legacy, rlhf]
i18n_source: 'e5b0714c6a82'
---

InstructGPT est la version de GPT-3 ajustée par fine-tuning chez OpenAI, décrite dans l'article « Training Language Models to Follow Instructions with Human Feedback » d'Ouyang et al. OpenAI l'a annoncé en janvier 2022 et a mis l'article complet sur arXiv en mars. L'équipe l'a construit en trois étapes : recueillir des démonstrations de bonnes réponses écrites par des annotateurs humains et ajuster GPT-3 dessus, rassembler des classements humains de plusieurs sorties du modèle, puis utiliser ces classements pour entraîner un modèle de récompense qui guide un fine-tuning supplémentaire par apprentissage par renforcement. OpenAI a entraîné trois tailles, 1,3B, 6B et 175B de paramètres, toutes avec la fenêtre de contexte de 2 048 tokens de GPT-3.

Le résultat le plus cité de l'article : les évaluateurs humains préféraient les sorties du InstructGPT 1,3B à celles du GPT-3 175B de base, alors que le plus petit a cent fois moins de paramètres. Cet écart montrait que l'ajustement par retours humains comptait plus que la taille brute pour produire les réponses que les gens voulaient vraiment, et il réduisait les sorties toxiques et fausses sans beaucoup coûter en capacité générale. La technique mise au point ici, l'apprentissage par renforcement à partir de retours humains, est devenue la méthode standard pour transformer un modèle de langage brut en assistant utilisable, et elle a mené directement à ChatGPT moins d'un an plus tard.
