---
title: 'AudioLM'
name: 'AudioLM'
slug: 'audiolm'
subtitle: "Le framework de Google pour générer de la parole réaliste et des continuations audio"
description: "Le framework de Google pour générer de la parole réaliste et des continuations audio"
company: 'google-deepmind'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://google-research.github.io/seanet/audiolm/examples/'
price: 'Paid'
rank: 5
release_date: '2022-09-07'
param_count: 'Undisclosed'
modality: [audio]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [audio, research, legacy]
i18n_source: '944df39235b8'
---

AudioLM est un framework de recherche que Google a publié en septembre 2022. Il traite la génération audio comme un problème de modélisation du langage sur des tokens audio discrets, au lieu des approches habituelles de régression sur spectrogramme ou sur forme d'onde. Il combine deux représentations : des tokens sémantiques issus de w2v-BERT, un modèle de parole auto-supervisé, qui captent la structure à longue distance, et des tokens acoustiques issus du codec neuronal SoundStream, qui gardent le détail fin de l'audio pour une synthèse de bonne qualité. Entraîné seulement sur de l'audio brut, sans transcription ni annotation, il peut continuer quelques secondes de parole ou de piano d'une façon qui reste cohérente sur des dizaines de secondes, là où les méthodes de génération audio plus anciennes peinaient. Google ne l'a jamais sorti comme produit. C'est resté un article et une page de démo, et Google DeepMind s'est servi de cette approche par tokens comme brique pour des travaux plus tardifs, comme MusicLM et des parties de Lyria.
