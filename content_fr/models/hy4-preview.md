---
title: 'Hy4 Preview'
name: 'Hy4 Preview'
slug: 'hy4-preview'
subtitle: "Modèle phare à poids ouverts de Tencent Hunyuan, conçu avec ses propres outils de développement"
description: "Modèle phare à poids ouverts de Tencent Hunyuan, conçu avec ses propres outils de développement"
company: 'tencent'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/'
price: 'Paid'
rank: 6
release_date: '2026-08-28'
param_count: '770B (MoE, 49B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.834
output_price_usd_per_m: 2.501
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-09-18'
tags: [llm, open-weight, code, moe, apache-2.0, agentic]
extra_model_types: ['Reasoning']
i18n_source: '24e04c87a390'
---

Tencent a publié Hy4 Preview en open source le 28 août 2026. C'est un modèle de mélange d'experts de 770 milliards de paramètres, dont 49 milliards actifs, avec une fenêtre de contexte d'un million de tokens, sous licence Apache 2.0. Plutôt que de construire un modèle de chat généraliste, l'équipe Hunyuan de Tencent l'a entraîné sur des données de travail d'ingénieurs logiciel, de développeurs de jeux, d'analystes en finance et d'experts en sécurité, et l'a co-conçu avec ses propres produits CodeBuddy et WorkBuddy.

Dans l'évaluation interne en aveugle de Tencent, où 163 experts ont jugé 203 vraies tâches d'ingénierie, Hy4 Preview a obtenu 2,99 sur 4,00 en moyenne, juste devant GLM-5.3 à 2,92 et Kimi K3 à 2,94. Le tarif API est de 0,834 $ par million de tokens en entrée et de 2,501 $ par million de tokens en sortie, avec l'entrée en cache à 0,042 $ par million.
