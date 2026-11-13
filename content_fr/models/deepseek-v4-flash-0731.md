---
title: 'DeepSeek-V4-Flash-0731'
name: 'DeepSeek-V4-Flash-0731'
slug: 'deepseek-v4-flash-0731'
subtitle: "Le modèle MoE de 284B sous licence MIT de DeepSeek, réentraîné pour un code agentique plus solide"
description: "Le modèle MoE de 284B sous licence MIT de DeepSeek, réentraîné pour un code agentique plus solide"
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 6
release_date: '2026-07-31'
param_count: '284B (13B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-08-09'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: '247907c6207f'
---

DeepSeek-V4-Flash-0731 fait sortir DeepSeek-V4-Flash de la preview vers une bêta publique, sous la forme d'un checkpoint dont le post-training a été refait, annoncé le 31 juillet 2026 dans le changelog de l'API. L'architecture est inchangée depuis les débuts du modèle en avril : un mélange d'experts de 284 milliards de paramètres, dont 13 milliards actifs par token, un expert partagé plus 256 experts routés, et une fenêtre de contexte d'un million de tokens. Ce qui change, c'est le pipeline de post-training : DeepSeek l'a réajusté pour le code, l'usage agentique d'outils et le raisonnement, et l'API prend désormais en charge nativement le format Responses et fonctionne avec Codex dès le départ. Il reste sous licence MIT et en accès libre, donc les équipes peuvent l'auto-héberger à des fins commerciales sans restriction. Il faut environ 110 GB de mémoire en quantification 3 bits, ou un nœud 4x GB300 en pleine précision. Le tarif de l'API est resté bas, à 0,14 $ par million de tokens en entrée et 0,28 $ par million de tokens en sortie.
