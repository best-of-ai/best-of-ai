---
title: 'Hunyuan DiT'
name: 'Hunyuan DiT'
slug: 'hunyuan-dit'
subtitle: "Transformeur de diffusion à poids ouverts de Tencent, pour le texte-vers-image en chinois et en anglais"
description: "Transformeur de diffusion à poids ouverts de Tencent, pour le texte-vers-image en chinois et en anglais"
company: 'tencent'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Tencent/HunyuanDiT'
price: 'Free'
rank: 5
release_date: '2024-05-14'
param_count: '1.5B'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: '7a104e51d815'
---

Hunyuan-DiT est le modèle texte-vers-image à poids ouverts de Tencent, construit sur une architecture de transformeur de diffusion plutôt que sur le design U-Net de la plupart des modèles de diffusion plus anciens. Tencent l'a publié en mai 2024, en associant un transformeur de débruitage de 1,5 milliard de paramètres à des encodeurs de texte CLIP bilingue et T5 multilingue, pour suivre des prompts en chinois ou en anglais avec une fidélité comparable. Ce focus bilingue est l'argument principal du modèle : la plupart des modèles texte-vers-image ouverts de l'époque géraient mal les prompts en chinois, et Hunyuan-DiT a été entraîné pour combler cet écart. Il génère des images en 1024x1024 et inclut un composant de chat multimodal qui permet d'affiner une image sur plusieurs tours de dialogue, au lieu de réécrire tout le prompt à chaque fois. Tencent a publié les poids sur Hugging Face et GitHub sous sa licence Hunyuan, puis a sorti une mise à jour 1.1 qui corrigeait la sursaturation et les artefacts de filigrane du checkpoint d'origine.
