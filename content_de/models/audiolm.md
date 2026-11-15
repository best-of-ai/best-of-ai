---
title: 'AudioLM'
name: 'AudioLM'
slug: 'audiolm'
subtitle: 'Googles Framework zur Generierung realistischer Sprach- und Audiofortsetzungen'
description: 'Googles Framework zur Generierung realistischer Sprach- und Audiofortsetzungen'
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

AudioLM ist ein Forschungsframework, das Google im September 2022 veröffentlichte. Es behandelt Audiogenerierung als Sprachmodellierungsaufgabe über diskrete Audio-Tokens statt als übliche Regression von Spektrogrammen oder Wellenformen. Es kombiniert zwei Repräsentationen: semantische Tokens von w2v-BERT, einem selbstüberwachten Sprachmodell, erfassen die langfristige Struktur; akustische Tokens des neuronalen SoundStream-Codecs bewahren feine Audiodetails für eine hochwertige Synthese. Das ausschließlich mit Roh-Audio und ohne Texttranskripte oder Annotationen trainierte Modell kann kurze Sprach- oder Klavieraufnahmen so fortsetzen, dass sie über mehrere zehn Sekunden hinweg kohärent bleiben – etwas, womit frühere Audiogenerierungsmethoden Schwierigkeiten hatten. Google brachte es nie als Produkt heraus; es blieb bei einer Forschungsarbeit und einer Demoseite. Google DeepMind nutzte den tokenbasierten Ansatz später als Baustein für Arbeiten wie MusicLM und Teile von Lyria.
