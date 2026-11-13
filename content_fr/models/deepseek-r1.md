---
title: 'DeepSeek R1'
name: 'DeepSeek R1'
slug: 'deepseek-r1'
subtitle: "Le modèle de raisonnement de DeepSeek qui a égalé les modèles frontier fermés en maths et en code"
description: "Le modèle de raisonnement de DeepSeek qui a égalé les modèles frontier fermés en maths et en code"
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-01-20'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.19
api_available: true
mmlu_score: 90.8
humaneval_score: 92.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, chain-of-thought]
i18n_source: 'fa3b02ee20e3'
---

DeepSeek R1 est un modèle de raisonnement publié par le laboratoire chinois DeepSeek le 20 janvier 2025. Il repose sur une architecture de mélange d'experts de 671 milliards de paramètres, dont 37 milliards actifs par token, et une partie de l'entraînement a été faite par apprentissage par renforcement à grande échelle, pas seulement par fine-tuning supervisé. Ça l'a poussé à dérouler les problèmes étape par étape avant de répondre. Au lancement, il a égalé l'o1 d'OpenAI sur les benchmarks de maths, de programmation et de sciences (90,8 sur MMLU, et parmi les meilleurs modèles de l'époque sur des problèmes du type AIME et Codeforces), avec des poids ouverts sous licence MIT et un tarif d'API très en dessous de celui d'o1.

La sortie a fait du bruit bien au-delà des cercles habituels de la recherche en IA : l'app de DeepSeek a brièvement pris la tête du classement de l'App Store américain, et l'annonce qu'un laboratoire chinois relativement petit avait entraîné un modèle de raisonnement de classe frontier pour une fraction du coût habituel a secoué les actions du secteur. R1 est disponible via l'API et l'interface de chat de DeepSeek. Ses poids ouverts permettent aussi de l'auto-héberger : il est largement recopié sur Hugging Face et servi par des fournisseurs d'inférence tiers.
