---
title: 'Emu Video'
name: 'Emu Video'
slug: 'emu-video'
subtitle: "Le modèle texte-vers-vidéo de Meta, construit sur le générateur d'images Emu"
description: "Le modèle texte-vers-vidéo de Meta, construit sur le générateur d'images Emu"
company: 'meta-ai'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/emu-text-to-video-generation-image-editing-research/'
price: 'Paid'
rank: 5
release_date: '2023-11-16'
param_count: 'Undisclosed'
modality: [text, video]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [video-generation, research, legacy]
i18n_source: 'd734ff203780'
---

Emu Video est un modèle de recherche texte-vers-vidéo que Meta a présenté en novembre 2023, construit sur le générateur d'images Emu de Meta. Au lieu de générer la vidéo directement à partir d'un prompt texte en une étape, il coupe le travail en deux : d'abord Emu génère une image fixe à partir du prompt, puis il génère une vidéo conditionnée à la fois par le texte et par cette image. Meta a indiqué que cette approche factorisée lui permettait d'éviter la cascade profonde de modèles séparés sur laquelle s'appuyaient des systèmes plus anciens comme Imagen Video de Google et Make-A-Video de Meta, tout en produisant une sortie de plus haute résolution. Dans des évaluations de préférence humaine, Meta a dit que les évaluateurs préféraient les extraits d'Emu Video à ceux d'Imagen Video et de Make-A-Video dans la grande majorité des cas. Il est sorti comme article de recherche et démo, pas comme produit public, et ses techniques ont nourri des fonctions vidéo Meta ultérieures plutôt que d'être livrées comme modèle autonome.
