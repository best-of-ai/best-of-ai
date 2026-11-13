---
title: 'Flan-T5'
name: 'Flan-T5'
slug: 'flan-t5'
subtitle: 'Le successeur à poids ouverts de T5 chez Google, ajusté par instructions'
description: 'Le successeur à poids ouverts de T5 chez Google, ajusté par instructions'
company: 'google'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/google/flan-t5-xxl'
price: 'Free'
rank: 4
release_date: '2022-10-20'
param_count: '11B'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, instruction-tuned, legacy]
i18n_source: '01962c85d25c'
---

Flan-T5 est la version de T5 ajustée par instructions chez Google, son transformer texte vers texte plus ancien, sortie en octobre 2022. Plutôt que de changer l'architecture de base, Google a fait du fine-tuning de T5 sur plus de mille tâches formulées comme des instructions, couvrant la traduction, le résumé, le raisonnement et la classification, dans de nombreuses langues. Cet ajustement le rend bien plus utilisable tel quel que le T5 de base, qui demandait un réglage propre à chaque tâche pour bien marcher. Google a publié la famille en plusieurs tailles, d'une petite version à 80 millions de paramètres jusqu'à Flan-T5-XXL à 11 milliards, toutes sous licence Apache 2.0 et téléchargeables librement sur Hugging Face. Sa fenêtre de contexte de 512 tokens est courte aux standards actuels, ce qui le limite aux documents et aux prompts courts. Il reste une base de comparaison courante pour la recherche sur l'ajustement par instructions, et une option légère pour les équipes qui veulent un modèle ouvert, auto-hébergé, pour des tâches de traitement du langage simples, sans le coût de calcul d'un plus grand LLM à décodeur seul.
