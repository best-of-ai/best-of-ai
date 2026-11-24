---
title: 'Kalanos Grader'
name: 'Kalanos Grader'
subtitle: 'Audit qualité open source pour les enregistrements d''entraînement de robots'
slug: 'kalanos-grader'
description: 'Kalanos Grader est un outil en ligne de commande gratuit sous licence Apache-2.0 qui audite en local les enregistrements d''entraînement de robots et d''IA physique. Il note les problèmes de timing, de mouvement, d''intégrité, de vision et d''annotation, et produit un rapport HTML ou JSON.'
website: 'https://kalanos.ai/grader'
logo_url: ''
category: 'robotics'
category_name: 'Robotique'
price: 'Free'
featured: false
rank: 5
alternatives:
  - foxglove
  - cleanlab
  - formant
date: '2026-11-24'
tags: [robotics, data_quality, dataset_audit, imitation_learning, physical_ai, open_source, cli, python, lerobot, free_tier]
i18n_source: 'cadc52e004d3'
---

Kalanos Grader vérifie les épisodes enregistrés d'un robot avant de s'entraîner dessus. On l'installe avec pip et on lance `kalanos grade ./my_recordings --report audit.html`. L'outil cherche des problèmes de timing, de signal et de mouvement, montre quels épisodes sont à revoir et pourquoi, puis écrit le résultat dans un rapport HTML ou en JSON. Aucun compte n'est nécessaire, et les audits locaux tournent sur ta propre machine.

Chaque enregistrement reçoit une note de 0 à 100 sur cinq familles : intégrité, timing, mouvement, vision et annotation. Par défaut, l'intégrité pèse 3, le timing, le mouvement et la vision 2 chacun, et l'annotation 1. La note mesure la qualité dans le périmètre évalué. Kalanos précise que ce n'est ni un taux de réussite ni une prédiction du comportement d'un modèle entraîné. La page montre un audit d'exemple sur 50 épisodes ALOHA, dont 39 ont réussi et 11 ont demandé une revue.

Il faut Python 3.10 ou plus récent. Les jeux de données LeRobot v2.0, v2.1 et v3.0, ainsi que les fichiers CSV et JSON ou JSONL, fonctionnent avec le paquet de base. Les enregistrements HDF5 et MCAP ou ROS 2 demandent des extras, les contrôles caméra demandent l'extra vidéo, et certaines structures HDF5 arbitraires peuvent ne pas être prises en charge. Un rapport complet sur 1 000 épisodes a pris environ 52 minutes lors du test de Kalanos lui-même, qui précise que ce n'est pas un benchmark. L'outil convient aux équipes d'apprentissage par imitation qui veulent vérifier vite la qualité d'un jeu de données.
