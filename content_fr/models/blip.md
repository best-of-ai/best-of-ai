---
title: 'BLIP'
name: 'BLIP'
slug: 'blip'
subtitle: "Le modèle de préentraînement vision-langage de Salesforce, pour le légendage et la recherche"
description: "Le modèle de préentraînement vision-langage de Salesforce, pour le légendage et la recherche"
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/BLIP'
price: 'Free'
rank: 6
release_date: '2022-01-28'
param_count: '223M'
modality: [text, image]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy]
i18n_source: '0a995979513f'
---

BLIP (Bootstrapping Language-Image Pre-training) est un modèle vision-langage que Salesforce Research a présenté début 2022. Il couvre des tâches de compréhension, comme le légendage d'images et les questions visuelles, et des tâches de recherche, comme l'appariement entre une image et un texte. L'entraînement passe par une méthode d'amorçage qui nettoie les légendes bruitées prises sur le web : le modèle en génère de synthétiques et écarte les mauvais appariements. Il a ainsi atteint de bons résultats sans dépendre seulement d'énormes jeux de données non triés. Avec environ 223 millions de paramètres, BLIP est petit à côté des systèmes multimodaux plus tardifs, mais il a compté en montrant que la qualité des légendes pèse autant que leur nombre pour le préentraînement.

Salesforce a publié les poids et le code de BLIP en accès ouvert, sous licence BSD. Le modèle est devenu une base courante en recherche vision-langage, et une brique dans d'autres projets, dont les premières fonctions d'interrogation d'outils comme Stable Diffusion. Son successeur, BLIP-2, a gagné en efficacité en reliant des encodeurs d'image gelés à des modèles de langage gelés par un module de pont léger. Le BLIP d'origine sert encore dans le travail académique et dans les pipelines que l'on héberge soi-même, quand un modèle de légendage compact et bien documenté suffit.
