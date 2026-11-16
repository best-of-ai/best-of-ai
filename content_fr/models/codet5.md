---
title: 'CodeT5+'
name: 'CodeT5+'
slug: 'codet5'
subtitle: "Famille de modèles de code encodeur-décodeur à poids ouverts, chez Salesforce"
description: "Famille de modèles de code encodeur-décodeur à poids ouverts, chez Salesforce"
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeT5'
price: 'Free'
rank: 3
release_date: '2023-05-13'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
humaneval_score: 30.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '20777365e144'
---

CodeT5+ est une famille de modèles de code à poids ouverts construite par Salesforce Research, sortie en mai 2023 à la suite du modèle encodeur-décodeur CodeT5 d'origine. Elle va de 220 millions à 16 milliards de paramètres, et peut tourner en encodeur seul, en décodeur seul ou en encodeur-décodeur complet. Une même architecture couvre donc des tâches de compréhension du code, comme la détection de défauts, et des tâches de génération, comme la complétion de code et la synthèse de code à partir de texte. L'entraînement mêle span denoising, modélisation de langage causale, apprentissage contrastif et appariement texte-code. Salesforce dit que cette approche lui donne un avantage sur les modèles de code à décodeur seul de taille proche, pour les tâches de génération augmentée par la recherche. La variante 16B tourne autour de 30,9 % en pass@1 sur HumanEval, et une version du même checkpoint ajustée pour les instructions dépasse 35 %, devant l'ancien code-cushman-001 d'OpenAI sur le même benchmark. Les poids sont sur Hugging Face sous licence BSD-3-Clause, ce qui fait de CodeT5+ l'une des premières alternatives pleinement ouvertes aux modèles de code propriétaires de l'ère Codex.
