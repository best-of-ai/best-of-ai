---
title: 'InternVL2'
name: 'InternVL2'
slug: 'internvl2'
subtitle: "Famille ouverte de modèles vision-langage du Shanghai AI Lab, au niveau des modèles multimodaux propriétaires"
description: "Famille ouverte de modèles vision-langage du Shanghai AI Lab, au niveau des modèles multimodaux propriétaires"
company: 'shanghai-ai-lab'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/OpenGVLab/InternVL'
price: 'Free'
rank: 6
release_date: '2024-07-04'
param_count: '76B (flagship; family spans 1B-108B)'
context_window_tokens: 8192
modality: [text, image, video]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '75f0788941ee'
---

InternVL2 est une famille de modèles vision-langage ouverts de l'OpenGVLab du Shanghai AI Laboratory, sortie le 4 juillet 2024, de 1B jusqu'à une configuration phare de 108B (76B InternViT + Llama 3 70B). Les modèles associent l'encodeur de vision InternViT à un modèle de langage, et la plus grande configuration, InternVL2-Llama3-76B, a obtenu 62,0 % sur le benchmark MMMU, au niveau de GPT-4o à l'époque, et devant les autres modèles multimodaux ouverts sur des tâches de compréhension de documents et de graphiques comme DocVQA et ChartQA. Au-delà des images fixes, InternVL2 peut traiter la vidéo en échantillonnant des images et en raisonnant dessus, et il accepte plusieurs images pour les documents et les comparaisons. Il est sorti sous licence MIT, avec les poids sur Hugging Face, et c'était alors l'une des alternatives ouvertes les plus solides aux systèmes fermés comme GPT-4o et Gemini. Le Shanghai AI Lab a enchaîné avec InternVL2.5 en décembre 2024, qui a fait passer le plus grand modèle au-dessus de 70 % sur MMMU.
