---
title: 'InternLM2.5'
name: 'InternLM2.5'
slug: 'internlm2-5'
subtitle: "Génération InternLM mise à jour du Shanghai AI Lab, plus forte en outils et en raisonnement"
description: "Génération InternLM mise à jour du Shanghai AI Lab, plus forte en outils et en raisonnement"
company: 'shanghai-ai-lab'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-07-03'
param_count: '7B (1.8B and 20B variants also released)'
context_window_tokens: 1000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 72.8
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, long-context]
i18n_source: '4f1fc404afae'
---

InternLM2.5 est la suite d'InternLM2 au Shanghai AI Laboratory, sortie à partir du 3 juillet 2024 en 7B et 1,8B, avec une version 20B ajoutée le 1er août 2024. Le modèle de chat 7B obtient 72,8 au MMLU et dépasse Llama 3 8B Instruct et Gemma 2 9B sur plusieurs benchmarks de raisonnement et de maths, selon les évaluations OpenCompass du développeur. Un checkpoint dédié, 7B-Chat-1M, étend la fenêtre de contexte à un million de tokens et peut retrouver des faits précis dans des documents d'un million de tokens lors de tests d'aiguille dans une botte de foin, tandis que le 20B standard plafonne à 200 000 tokens. La série ajoute aussi des appels de fonctions et un usage d'outils de type agent plus solides que l'InternLM2 d'origine, et tous les poids sont sous licence Apache 2.0, via Hugging Face et le dépôt GitHub InternLM.
