---
title: 'ESM-2'
name: 'ESM-2'
slug: 'esm-2'
subtitle: "Le modèle de langage de protéines de Meta, utilisé pour prédire la structure à partir de la séquence"
description: "Le modèle de langage de protéines de Meta, utilisé pour prédire la structure à partir de la séquence"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/protein-folding-esmfold-metagenomics/'
price: 'Free'
rank: 6
release_date: '2022-10-31'
param_count: '15B'
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [science, biology, open-weight]
i18n_source: '603d0e8b688e'
---

ESM-2 est un modèle de langage de protéines de Meta AI, publié en octobre 2022, entraîné sur environ 250 millions de séquences de protéines, sans étape d'alignement de séquences multiples. Il existe en plusieurs tailles, jusqu'à 15 milliards de paramètres, le plus grand modèle de langage de protéines au moment de la sortie. Meta a constaté qu'en montant en taille, ses représentations internes commencent à encoder l'information structurale 3D des protéines, sans avoir été entraîné explicitement à le faire. C'est cette propriété qui alimente ESMFold, le système de prédiction de structure de Meta : il lit une séquence de protéine via ESM-2 et transforme la représentation obtenue directement en coordonnées atomiques, en sautant les bases d'alignement sur lesquelles s'appuient des outils comme AlphaFold, ce qui rend la prédiction de structure nettement plus rapide. Meta a publié les poids ouvertement et s'est servi d'ESM-2 pour construire l'ESM Metagenomic Atlas, une base publique de structures prédites pour des centaines de millions de protéines jusque-là non caractérisées.
