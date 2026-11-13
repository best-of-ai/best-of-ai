---
title: 'Llama Guard 2'
name: 'Llama Guard 2'
slug: 'llama-guard-2'
subtitle: "Ancien modèle de classification de sécurité du contenu de Meta, avant Llama Guard 3"
description: "Ancien modèle de classification de sécurité du contenu de Meta, avant Llama Guard 3"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-llama-3/'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [safety, open-weight, legacy]
i18n_source: '1ec3f0456e4e'
---

Llama Guard 2 est un classifieur de sécurité du contenu que Meta a sorti en même temps que Llama 3 en avril 2024, construit sur une base Llama 3 8B plutôt que comme modèle de chat généraliste. Il vérifie à la fois les prompts qui entrent dans un modèle de langage et les réponses qui en sortent, et il signale le contenu sur 11 catégories de risque tirées de la taxonomie MLCommons, dont la violence, le discours de haine et le contenu sexuel. Les développeurs le font tourner comme garde-fou devant ou derrière un autre LLM dans un pipeline, plutôt que de l'utiliser pour générer des réponses directement. Meta l'a depuis remplacé par Llama Guard 3, mais il reste disponible sur Hugging Face sous la Llama 3 Community License, pour les équipes qui le font déjà tourner en production.
