---
title: 'Kosmos-2'
name: 'Kosmos-2'
slug: 'kosmos-2'
subtitle: "Modèle multimodal ancré de Microsoft, qui relie le langage à des régions précises de l'image"
description: "Modèle multimodal ancré de Microsoft, qui relie le langage à des régions précises de l'image"
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/microsoft/unilm/tree/master/kosmos-2'
price: 'Free'
rank: 5
release_date: '2023-06-26'
param_count: '1.6B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '327b99415fef'
---

Kosmos-2 est un modèle multimodal de Microsoft Research, publié en juin 2023, avec environ 1,6 milliard de paramètres. Son trait distinctif est l'ancrage : au lieu de seulement décrire une image en texte, il relie des expressions de sa sortie à des boîtes englobantes précises dans l'image, de sorte qu'une phrase sur « un chien » ou « la chaise à gauche » pointe vers les pixels exacts dont il parle. Microsoft l'a entraîné sur GrIT, un grand jeu de données de paires image-texte ancrées construit pour cela, combiné à des corpus multimodaux généraux, et l'a évalué sur la compréhension d'expressions référentielles, l'ancrage de syntagmes et les tâches vision-langage habituelles. Kosmos-2 était une sortie de recherche, pas un produit, pour montrer que l'ancrage pouvait s'apprendre de bout en bout dans un modèle de langage, plutôt que d'être ajouté à côté avec un détecteur séparé. Le code et les poids sont ouverts sur GitHub et Hugging Face sous licence MIT, et ce travail a nourri les recherches multimodales suivantes de Microsoft, dont des parties des gammes vision-langage Florence et Phi.
