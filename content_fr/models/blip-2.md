---
title: 'BLIP-2'
name: 'BLIP-2'
slug: 'blip-2'
subtitle: "Le successeur plus efficace de BLIP chez Salesforce, qui amorce le préentraînement vision-langage depuis des encodeurs gelés"
description: "Le successeur plus efficace de BLIP chez Salesforce, qui amorce le préentraînement vision-langage depuis des encodeurs gelés"
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/LAVIS/tree/main/projects/blip2'
price: 'Free'
rank: 6
release_date: '2023-01-30'
param_count: '3.7B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '8456e2d29321'
---

BLIP-2 est un modèle vision-langage que Salesforce Research a publié en janvier 2023. Il repose sur une astuce d'efficacité précise : au lieu d'entraîner de zéro, ensemble, un gros encodeur d'image et un modèle de langage, il gèle un encodeur d'image déjà préentraîné et un modèle de langage déjà préentraîné, et n'entraîne qu'un connecteur léger entre les deux, le Q-Former. Ce Q-Former compte environ 188 millions de paramètres entraînables, moins de 2 % du modèle total. BLIP-2 coûtait donc bien moins cher à entraîner que les modèles vision-langage comparables de l'époque, tout en restant bon en légendage d'images et en questions visuelles. Salesforce a publié plusieurs variantes qui associent le Q-Former à différents modèles de langage gelés, dont des versions sur OPT (2,7B et 6,7B de paramètres) et Flan-T5 (jusqu'à 11B de paramètres), pour choisir entre capacité et coût de calcul. Le code et les poids sont sur GitHub et Hugging Face, sous licence MIT, dans la bibliothèque LAVIS de Salesforce. L'idée d'un encodeur gelé plus un connecteur léger, que ce modèle a fait connaître, a ensuite marqué d'autres modèles multimodaux, qui greffent de la même façon la vision sur un modèle de langage déjà là plutôt que de tout entraîner d'un bloc.
