---
title: 'Kimi K2.6'
name: 'Kimi K2.6'
slug: 'kimi-k2-6'
subtitle: "Modèle à poids ouverts de Moonshot, fait pour les tâches agentiques et l'usage d'outils de longue durée"
description: "Modèle à poids ouverts de Moonshot, fait pour les tâches agentiques et l'usage d'outils de longue durée"
company: 'moonshot-ai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-04-20'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.6
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 88.0
humaneval_score: 87.0
lmarena_score: 1355
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, agentic, reasoning, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: 'f4220c32edb6'
---

Kimi K2.6 est le modèle phare à poids ouverts de Moonshot AI, sorti en avril 2026 comme successeur du Kimi K2 d'origine. C'est un mélange d'experts de 1 billion de paramètres qui active environ 32 milliards de paramètres par token, livré nativement en INT4 pour une inférence moins chère, avec une fenêtre de contexte de 262 144 tokens. Le modèle est fait pour le travail agentique de longue durée : Moonshot l'a conçu autour de l'orchestration multi-agents, de sessions de code qui tournent des heures sans intervention humaine, et d'une entrée multimodale native plutôt qu'une vision ajoutée après coup. Des évaluations indépendantes d'Artificial Analysis le classent comme le modèle à poids ouverts le plus fort disponible, à quelques points des grands systèmes fermés d'OpenAI et d'Anthropic sur des tâches comme SWE-Bench Pro et Humanity's Last Exam, pour une fraction de leur prix par token. Moonshot publie les poids sous une licence MIT modifiée, donc n'importe qui peut télécharger le modèle et l'auto-héberger, plutôt que de passer par l'API de Moonshot.
