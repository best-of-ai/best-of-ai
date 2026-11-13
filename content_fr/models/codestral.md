---
title: 'Codestral'
name: 'Codestral'
slug: 'codestral'
subtitle: "Modèle de génération et de complétion de code de Mistral"
description: "Modèle de génération et de complétion de code de Mistral"
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral/'
price: 'Free'
rank: 6
release_date: '2024-05-29'
param_count: '22B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 0.9
api_available: true
humaneval_score: 81.1
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, code, open-weight, api]
i18n_source: '0c94b2ec4923'
---

Codestral est le modèle de génération de code dédié de Mistral AI, d'abord sorti en mai 2024 avec 22 milliards de paramètres. Il est fait pour la complétion fill-in-the-middle et la génération de code dans plusieurs langages, et il est sorti avec 81,1 % en pass@1 sur HumanEval, devant des modèles de code plus gros comme Code Llama 70B et DeepSeek Coder 33B à l'époque. La version d'origine avait une fenêtre de contexte de 32 000 tokens et la licence Mistral AI Non-Production License, qui limitait l'usage gratuit à la recherche et aux tests, et exigeait une licence commerciale à part pour un déploiement en production.

Mistral a ensuite porté la fenêtre de contexte de Codestral à 256 000 tokens et, en avril 2026, l'a replacé sous Apache 2.0. La restriction d'usage commercial est tombée, et le modèle peut s'utiliser librement dans les IDE, les assistants de code et les pipelines de CI. Codestral est disponible en poids téléchargeables sur Hugging Face et via l'API de Mistral, actuellement à 0,30 $ par million de tokens d'entrée et 0,90 $ par million de tokens de sortie. Il est en concurrence directe avec d'autres modèles de code ouverts de taille moyenne, comme Codestral Mamba et Code Llama. Le passage à une licence permissive a été largement vu comme un changement net dans l'espace des modèles de code open source.
