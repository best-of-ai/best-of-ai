---
title: 'Chameleon'
name: 'Chameleon'
slug: 'chameleon'
subtitle: 'Le modèle à fusion précoce de Meta, qui mélange nativement des tokens de texte et d''image'
description: 'Le modèle à fusion précoce de Meta, qui mélange nativement des tokens de texte et d''image'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-fair-research-new-releases/'
price: 'Free'
rank: 6
release_date: '2024-05-16'
param_count: '34B'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'Research-only'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, open-weight]
extra_model_types: ['Image Generation']
i18n_source: '6e820e7a5edb'
---

Chameleon est un modèle multimodal de Meta FAIR, décrit dans un article de mai 2024, qui mélange texte et images dès la base au lieu de greffer un encodeur de vision sur un modèle de langage. La plupart des systèmes multimodaux utilisent une fusion tardive : un encodeur d'image séparé envoie des caractéristiques visuelles à un modèle de langage préentraîné sur du texte seul. Chameleon quantifie plutôt les images en tokens discrets et s'entraîne de zéro sur des suites où des tokens de texte et d'image sont entrelacés. Le même transformer apprend donc à raisonner sur les deux modalités, et il peut aussi générer des images en sortie, pas seulement les décrire.

Meta a publié deux tailles, Chameleon-7B et Chameleon-34B, et indique que la version 34B dépassait des modèles comme Flamingo et IDEFICS en description d'images et en questions-réponses visuelles, tout en tenant la comparaison avec GPT-4V et Gemini Pro dans des tests de préférence humaine par paires, sur des tâches de génération à modalités mixtes. Les poids sont disponibles sur GitHub sous une licence limitée à la recherche : Chameleon ne peut donc pas servir dans un cadre commercial. Meta l'a surtout présenté comme une démonstration d'entraînement en fusion précoce, pas comme un produit. Des idées venues de Chameleon ont alimenté les Llama multimodaux suivants de Meta, qui ont étendu un entraînement de ce type à une ligne de modèles plus large, sous licence commerciale.
