---
title: 'AudioCraft'
name: 'AudioCraft'
slug: 'audiocraft'
subtitle: 'Open-Source-Framework von Meta für Musik- und Soundeffektgenerierung'
description: 'Open-Source-Framework von Meta für Musik- und Soundeffektgenerierung'
company: 'meta-ai'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/audiocraft-musicgen-audiogen-encodec-generative-ai-audio/'
price: 'Free'
rank: 6
release_date: '2023-08-02'
param_count: '300M-3.3B (MusicGen), 1.5B (AudioGen)'
modality: [audio, text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['GitHub']
date: '2026-07-16'
tags: [audio, open-weight, music-generation]
i18n_source: '0ed2f655dea3'
---

AudioCraft ist eine Codebibliothek, die Meta im August 2023 veröffentlichte. Sie bündelt drei generative Audiomodelle: MusicGen für Musik aus Text, AudioGen für Umgebungsgeräusche und EnCodec, den neuronalen Audiocodec, den beide zum Tokenisieren von Wellenformen verwenden. MusicGen ist in mehreren Größen verfügbar (300 Mio., 1,5 Mrd. und 3,3 Mrd. Parameter); Varianten können zusätzlich einer Melodie neben dem Textprompt folgen. AudioGen gibt es als Modell mit 1,5 Milliarden Parametern, das auf Geräusche statt Musik trainiert wurde. Meta veröffentlichte Code und Gewichte unter MIT-Lizenz. Dadurch war AudioCraft eines der ersten vollständig offenen Toolkits für die Generierung von Audio aus Text – im Gegensatz zu geschlossenen Systemen etwa von Google. Die kleineren Checkpoints laufen auf einer einzelnen Consumer-GPU. Die Bibliothek ist zu einer verbreiteten Grundlage für Open-Source-Musikgenerierung und Forschung zu steuerbarer Audiosynthese geworden.
