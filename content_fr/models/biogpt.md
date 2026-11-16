---
title: 'BioGPT'
name: 'BioGPT'
slug: 'biogpt'
subtitle: "Le modèle génératif de Microsoft, propre au domaine, préentraîné sur la littérature biomédicale"
description: "Le modèle génératif de Microsoft, propre au domaine, préentraîné sur la littérature biomédicale"
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BioGPT'
price: 'Free'
rank: 5
release_date: '2022-09-24'
param_count: '347M (base), 1.5B (Large)'
context_window_tokens: 1024
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [healthcare, open-weight, legacy]
i18n_source: 'b08c07fb9738'
---

BioGPT est un modèle de langage que Microsoft Research a présenté en octobre 2022, construit pour le texte biomédical plutôt qu'adapté après coup à partir d'un modèle généraliste. Il reprend une architecture de décodeur de type GPT-2, entraînée de zéro sur environ 15 millions de résumés PubMed. Il existe en version de base à 347 millions de paramètres et en BioGPT-Large à 1,5 milliard de paramètres. Entraîné sur du texte biomédical dès le départ, et pas seulement ajusté dessus par fine-tuning, il a dépassé les modèles de langage généralistes plus anciens sur l'extraction de relations biomédicales, la réponse à des questions sur la littérature médicale et la classification de documents. Microsoft a publié les deux checkpoints sous licence MIT sur Hugging Face et GitHub. C'est devenu un point de départ courant pour les groupes de recherche qui construisent des outils de NLP biomédical sans entraîner un modèle de domaine de zéro. Il précède la vague des modèles de chat généralistes ajustés par instructions, et il n'a pas été mis à jour depuis. On s'en sert surtout aujourd'hui comme option légère, que l'on peut héberger soi-même, pour des tâches étroites de texte biomédical, plutôt que comme assistant général.
