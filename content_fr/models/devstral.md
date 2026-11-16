---
title: 'Devstral'
name: 'Devstral'
slug: 'devstral'
subtitle: "Le modèle à poids ouverts de Mistral, ajusté pour le code agentique et l'exploration de bases de code"
description: "Le modèle à poids ouverts de Mistral, ajusté pour le code agentique et l'exploration de bases de code"
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/devstral/'
price: 'Free'
rank: 6
release_date: '2025-05-21'
param_count: '24B'
context_window_tokens: 128000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0.3
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, agentic, api]
i18n_source: '10cd7f3fca31'
---

Devstral est un modèle de code de 24 milliards de paramètres que Mistral AI a publié le 21 mai 2025, construit avec All Hands AI, l'équipe derrière le framework d'agents OpenHands. Contrairement à la plupart des modèles de code, surtout ajustés pour l'autocomplétion ou la génération en un tour, Devstral est entraîné pour le code agentique : explorer une base de code sur plusieurs fichiers, utiliser des outils et mener des tâches de génie logiciel en plusieurs étapes. Sur SWE-bench Verified, il a obtenu 46,8 %, devant tous les modèles ouverts disponibles à la sortie, et même devant certains modèles propriétaires plus grands.

Mistral a publié les poids sous licence Apache 2.0, et le modèle est assez petit pour tourner sur un seul GPU grand public haut de gamme, ce qui en a fait une base courante pour des agents de code en local. Mistral a ensuite enchaîné avec Devstral Small 1.1 et le plus grand Devstral 2, chacun poussant les scores SWE-bench plus haut. Le Devstral d'origine reste notable comme l'un des premiers modèles à poids ouverts conçus autour du génie logiciel agentique, plutôt que de la complétion de code généraliste.
