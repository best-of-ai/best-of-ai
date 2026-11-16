---
title: 'Codex'
name: 'Codex'
slug: 'codex'
subtitle: "Modèle de complétion de code d'origine d'OpenAI, qui faisait tourner les débuts de GitHub Copilot"
description: "Modèle de complétion de code d'origine d'OpenAI, qui faisait tourner les débuts de GitHub Copilot"
company: 'openai'
model_type: 'Code'
logo_url: ''
product_url: 'https://openai.com/index/openai-codex/'
price: 'Paid'
rank: 6
release_date: '2021-08-10'
param_count: '12B'
context_window_tokens: 4096
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: false
humaneval_score: 28.8
access_methods: [Research]
runs_at_home: false
platforms: ['API (deprecated)']
date: '2026-07-16'
tags: [code, legacy, foundation-model]
i18n_source: '2cde22dddd75'
---

Codex est le premier modèle de génération de code dédié d'OpenAI, annoncé en août 2021 comme un descendant de GPT-3 ajusté par fine-tuning sur des milliards de lignes de code source public issues de GitHub. La plus grande version publiée avait 12 milliards de paramètres et une fenêtre de contexte de 4 096 tokens. Elle résolvait 28,8 % des problèmes du benchmark HumanEval d'OpenAI du premier coup, et 77,5 % quand on lui laissait 100 essais échantillonnés par problème. C'est Codex qui faisait tourner le GitHub Copilot d'origine, lors de la préversion technique de 2021, l'un des premiers déploiements à grande échelle d'un LLM comme assistant de programmation, plutôt que comme démo de chat ou de complétion. OpenAI l'a proposé par une API en bêta privée pendant quelques années, avant de retirer l'API Codex autonome en mars 2023 et d'en intégrer les capacités aux modèles suivants des familles GPT-3.5 et GPT-4. Le nom sert encore de marque aux produits de programmation agentique plus récents d'OpenAI, mais le modèle Codex d'origine n'est plus accessible par l'API.
