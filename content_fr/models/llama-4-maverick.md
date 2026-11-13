---
title: 'Llama 4 Maverick'
name: 'Llama 4 Maverick'
slug: 'llama-4-maverick'
subtitle: "Modèle phare multimodal à mélange d'experts et à poids ouverts de Meta"
description: "Modèle phare multimodal à mélange d'experts et à poids ouverts de Meta"
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 8
release_date: '2025-04-05'
param_count: '400B (17B active)'
context_window_tokens: 1000000
modality: [text, image]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 86.0
humaneval_score: 85.0
lmarena_score: 1330
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, self-hosted, mixture-of-experts]
i18n_source: '1e256fde4e77'
---

Llama 4 Maverick est le modèle phare de Meta dans la sortie Llama 4 d'avril 2025, construit comme un mélange d'experts de 400 milliards de paramètres au total, mais seulement 17 milliards actifs par token, répartis sur 128 experts. Il est nativement multimodal, entraîné pour traiter texte et images ensemble plutôt que d'ajouter un encodeur de vision sur un modèle de texte après coup, et il prend en charge une fenêtre de contexte d'un million de tokens. Meta a indiqué que Maverick dépasse GPT-4o et Gemini 2.0 Flash sur un ensemble de benchmarks publics, et qu'il égale DeepSeek V3 sur le raisonnement et le code tout en utilisant moins de la moitié des paramètres actifs. Il est distribué sous la Llama 4 Community License, avec les poids sur Hugging Face et via des fournisseurs cloud comme AWS Bedrock et Together AI.
