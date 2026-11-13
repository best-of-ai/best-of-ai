---
title: 'CodeGen2'
name: 'CodeGen2'
slug: 'codegen2'
subtitle: "Modèle de code à poids ouverts de Salesforce, pour le remplissage et la synthèse de programmes en plusieurs tours"
description: "Modèle de code à poids ouverts de Salesforce, pour le remplissage et la synthèse de programmes en plusieurs tours"
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeGen2'
price: 'Free'
rank: 5
release_date: '2023-05-03'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [code, open-weight]
i18n_source: '19442e527069'
---

CodeGen2 est la famille de modèles de code ouverts de deuxième génération de Salesforce Research, sortie en mai 2023 à la suite du CodeGen d'origine. Elle existe en quatre tailles : 1B, 3,7B, 7B et 16B de paramètres. Le principal progrès par rapport au premier CodeGen est le remplissage (infilling) : le modèle peut compléter un morceau de code manquant à partir du contexte des deux côtés, au lieu de générer le texte seulement de gauche à droite. Il est donc mieux adapté aux vrais flux de travail dans un éditeur, comme l'autocomplétion et la réparation de code, là où il faut écrire au milieu d'un fichier déjà là.

Les modèles sont entraînés sur un mélange de langue naturelle et de code source, dans de nombreux langages de programmation, et publiés sous la licence permissive Apache 2.0 via Hugging Face et GitHub. CodeGen2 a été testé avec un contexte utile d'environ 2 000 tokens, modeste aux standards d'aujourd'hui, mais typique des modèles de code de cette époque. Salesforce le présentait comme une alternative commode pour la recherche, face à des modèles de code fermés comme Codex. Il a ensuite été suivi de CodeGen2.5, un modèle plus petit réglé pour égaler les performances de prédécesseurs plus gros.
