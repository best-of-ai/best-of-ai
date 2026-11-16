---
title: 'Hunyuan3D'
name: 'Hunyuan3D'
slug: 'hunyuan3d'
subtitle: "Modèle à poids ouverts de Tencent pour générer des assets 3D à partir de texte ou d'images"
description: "Modèle à poids ouverts de Tencent pour générer des assets 3D à partir de texte ou d'images"
company: 'tencent'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/Tencent/Hunyuan3D-2'
price: 'Free'
rank: 5
release_date: '2025-01-21'
param_count: '2.6B (shape) + 1.3B (texture)'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [3d-generation, open-weight, api]
i18n_source: '07d08c139e5b'
---

Hunyuan3D est le système à poids ouverts de Tencent pour transformer des prompts texte ou des images de référence en assets 3D. La version 2.0, largement utilisée, a été publiée en janvier 2025. Le travail est découpé en deux modèles : un générateur de forme de 2,6 milliards de paramètres, construit sur un transformeur de diffusion à base de flow, qui produit un mesh sans texture, et un modèle de texture de 1,3 milliard de paramètres qui peint ensuite des matériaux PBR haute résolution sur ce mesh. Ce découpage laisse chaque partie se spécialiser. Le modèle de forme ne s'occupe que de la géométrie, le modèle de texture gère la couleur, la réponse à la lumière et le détail de surface. Tencent a publié les poids sur Hugging Face et GitHub sous sa licence Hunyuan, ce qui donne aux studios de jeux et aux artistes 3D un moyen de générer des assets en local, plutôt que via une API payante. Il est en concurrence avec d'autres générateurs 3D ouverts ou semi-ouverts, comme TripoSR et TripoSG de Stability AI. Les versions suivantes de Hunyuan3D (2.1, 2.5) ont poussé plus loin la fidélité des textures et le détail de la géométrie.
