---
title: 'Megatron-Turing NLG'
name: 'Megatron-Turing NLG'
slug: 'megatron-turing-nlg'
subtitle: "Modèle de recherche de 530 milliards de paramètres de NVIDIA et Microsoft, parmi les plus grands LLM denses de son époque"
description: "Modèle de recherche de 530 milliards de paramètres de NVIDIA et Microsoft, parmi les plus grands LLM denses de son époque"
company: 'nvidia'
model_type: 'Language'
logo_url: ''
product_url: 'https://developer.nvidia.com/megatron-turing-natural-language-generation'
price: 'Paid'
rank: 5
release_date: '2021-10-11'
param_count: '530B'
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, research, legacy]
extra_model_types: ['Reasoning']
i18n_source: '06b0502910e0'
---

Megatron-Turing NLG est un modèle de langage à transformeur dense de 530 milliards de paramètres, que NVIDIA et Microsoft ont entraîné ensemble et annoncé en octobre 2021. C'était alors le plus grand modèle de langage monolithique (hors mélange d'experts) jamais entraîné, construit en combinant le parallélisme tensoriel de Megatron-LM, chez NVIDIA, avec le parallélisme de pipeline de DeepSpeed et l'optimiseur ZeRO, chez Microsoft, sur des centaines de GPU A100. Le modèle a 105 couches de transformeur et a été entraîné sur un corpus de 270 milliards de tokens, tiré de texte web, de livres et d'autres sources sélectionnées.

Il a surtout servi de démonstration de recherche et d'ingénierie, pour voir jusqu'où la montée en échelle des modèles denses et les logiciels d'entraînement distribué pouvaient aller, avant que les architectures de mélange d'experts deviennent la voie plus pratique vers des modèles plus grands. NVIDIA et Microsoft ont publié des résultats en complétion, en compréhension de lecture et en raisonnement, où il dépassait des prédécesseurs plus petits comme GPT-3 et Turing-NLG, mais le modèle lui-même n'a jamais été ouvert comme produit public ni comme API.
