---
title: 'CosyVoice'
name: 'CosyVoice'
slug: 'cosyvoice'
subtitle: "Modèle à poids ouverts d'Alibaba pour le clonage de voix zero-shot et la synthèse vocale"
description: "Modèle à poids ouverts d'Alibaba pour le clonage de voix zero-shot et la synthèse vocale"
company: 'alibaba'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://github.com/FunAudioLLM/CosyVoice'
price: 'Free'
rank: 5
release_date: '2024-07-09'
param_count: 'Undisclosed'
modality: [audio, text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Alibaba Cloud']
date: '2026-07-16'
tags: [text-to-speech, open-weight, voice-cloning, api]
i18n_source: '6cc55c56d545'
---

CosyVoice est un modèle de synthèse vocale et de clonage de voix de l'équipe FunAudioLLM d'Alibaba, publié en poids ouverts en juillet 2024. Il génère de la parole à partir de courts extraits audio de référence : quelques secondes d'échantillon suffisent pour cloner une voix, puis lire un texte quelconque dans cette voix, dans plusieurs langues, dont le chinois, l'anglais, le japonais et le coréen. Le modèle s'appuie sur des tokens sémantiques de parole supervisés, avec une génération de type modèle de langage. Il peut ainsi cloner une voix d'une langue à l'autre, en zero-shot, sans fine-tuning propre au locuteur. Alibaba a poursuivi la gamme, avec CosyVoice 2 puis CosyVoice 3, sur des modèles sous-jacents plus gros et avec une latence plus basse. La version d'origine reste sur Hugging Face et via l'API Model Studio d'Alibaba Cloud, sous licence Apache 2.0.
