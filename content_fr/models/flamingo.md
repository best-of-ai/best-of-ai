---
title: 'Flamingo'
name: 'Flamingo'
slug: 'flamingo'
subtitle: 'Le modèle vision-langage de DeepMind qui a ouvert le raisonnement multimodal en few-shot'
description: 'Le modèle vision-langage de DeepMind qui a ouvert le raisonnement multimodal en few-shot'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/tackling-multiple-tasks-with-a-single-visual-language-model/'
price: 'Paid'
rank: 6
release_date: '2022-04-29'
param_count: '80B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, vision, research]
i18n_source: '98bf1c585f2e'
---

Flamingo est un modèle vision-langage publié par DeepMind en avril 2022, conçu pour traiter ensemble images, vidéos et texte, et répondre à des questions ouvertes à leur sujet après n'avoir vu qu'une poignée d'exemples. Il part de Chinchilla, le modèle de langage à 70 milliards de paramètres de DeepMind, et ajoute des encodeurs de vision et des couches d'attention croisée qui permettent de conditionner la génération de texte à l'entrée visuelle, ce qui porte le modèle complet à environ 80 milliards de paramètres. L'idée centrale était l'apprentissage few-shot pour les tâches vision-langage : plutôt que du fine-tuning sur chaque nouveau jeu de données, on pouvait montrer à Flamingo quelques exemples dans son prompt, et il généralisait à partir de là, un peu comme GPT-3 le faisait pour le texte. À sa sortie, il a battu toutes les approches few-shot précédentes sur 16 benchmarks vision-langage, dont les légendes d'images, les questions-réponses visuelles et le dialogue visuel. DeepMind n'a jamais sorti Flamingo comme produit ni comme API publique. Il est resté un modèle de recherche, mais son architecture a influencé les systèmes multimodaux suivants, dont des réimplémentations ouvertes comme OpenFlamingo et des choix de conception dans les modèles multimodaux ultérieurs de Google.
