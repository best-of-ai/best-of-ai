---
title: 'CosyVoice'
name: 'CosyVoice'
slug: 'cosyvoice'
subtitle: 'Modelo de clonación de voz zero-shot y de texto a voz de pesos abiertos de Alibaba'
description: 'Modelo de clonación de voz zero-shot y de texto a voz de pesos abiertos de Alibaba'
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

CosyVoice es un modelo de texto a voz y de clonación de voz del equipo FunAudioLLM de Alibaba, publicado como pesos abiertos en julio de 2024. Genera habla a partir de clips de audio de referencia cortos, así que puede clonar una voz con solo unos segundos de muestra y luego decir un texto arbitrario con esa voz en varios idiomas, entre ellos chino, inglés, japonés y coreano. El modelo se apoya en tokens semánticos de habla supervisados, emparejados con un enfoque de generación al estilo de un modelo de lenguaje, lo que le permite la clonación de voz entre idiomas y zero-shot sin un fine-tuning específico del hablante. Alibaba ha seguido actualizando la línea y publicó después CosyVoice 2 y CosyVoice 3, con modelos subyacentes más grandes y menor latencia, y la publicación original sigue disponible en Hugging Face y a través de la API de Model Studio de Alibaba Cloud bajo licencia Apache 2.0.
