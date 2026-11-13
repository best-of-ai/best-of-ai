---
title: 'AlphaGeometry'
name: 'AlphaGeometry'
slug: 'alphageometry'
subtitle: "Le système neuro-symbolique de DeepMind qui résout des problèmes de géométrie de niveau olympiade"
description: "Le système neuro-symbolique de DeepMind qui résout des problèmes de géométrie de niveau olympiade"
company: 'google-deepmind'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/'
price: 'Paid'
rank: 6
release_date: '2024-01-17'
param_count: 'Undisclosed'
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [reasoning, math, research]
i18n_source: '1dbe543ce262'
---

AlphaGeometry est un système neuro-symbolique de Google DeepMind, publié dans Nature en janvier 2024, conçu pour résoudre des problèmes de géométrie au niveau des participants aux Olympiades internationales de mathématiques. Il couple un modèle de langage entraîné sur des preuves de géométrie générées de façon synthétique et un moteur classique de déduction symbolique : la moitié neuronale propose des constructions auxiliaires utiles, comme de nouveaux points ou de nouvelles droites, et la moitié symbolique mène la déduction logique formelle jusqu'à la preuve. Sur un benchmark de 30 problèmes de géométrie des IMO, de 2000 à 2022, il en a résolu 25, proche du score moyen d'un médaillé d'or et loin devant les prouveurs automatiques de théorèmes qui précédaient.

DeepMind a entraîné le modèle de langage sur cent millions de théorèmes et de preuves synthétiques, générés sans aucune démonstration humaine, les données étiquetées de géométrie d'olympiade étant rares. Le projet est resté de la recherche et n'est jamais devenu un produit, mais il a montré qu'associer un modèle neuronal et un solveur symbolique pouvait dépasser les approches qui ne s'appuient que sur l'une des deux techniques. Un an plus tard, DeepMind a enchaîné avec AlphaGeometry2, qui a porté le taux de résolution à 84 % de tous les problèmes de géométrie des 25 dernières années d'IMO, au-dessus de la moyenne d'un médaillé d'or pour la première fois.
