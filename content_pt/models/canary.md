---
title: 'Canary'
name: 'Canary'
slug: 'canary'
subtitle: "Modelo multilíngue de reconhecimento e tradução de fala da NVIDIA"
description: "Modelo multilíngue de reconhecimento e tradução de fala da NVIDIA"
company: 'nvidia'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://huggingface.co/nvidia/canary-1b'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '1B'
modality: [audio, text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['NVIDIA NIM', 'Hugging Face']
date: '2026-07-16'
tags: [speech-recognition, open-weight, multilingual]
i18n_source: 'ad7707d7cc9a'
---

Canary é uma família de modelos de fala da equipe NeMo da NVIDIA; o principal, Canary-1B, foi lançado em abril de 2024. Ao contrário de um modelo típico de reconhecimento automático de fala (ASR), que apenas transcreve o áudio, o Canary faz reconhecimento e tradução de fala entre inglês, francês, alemão e espanhol: converte o áudio falado em texto no mesmo idioma ou o traduz para outro. O modelo combina um encoder FastConformer com um decodificador transformer, uma arquitetura que a NVIDIA ajustou para alcançar alta precisão com um modelo relativamente pequeno. No lançamento, superou concorrentes várias vezes maiores na Open ASR Leaderboard do Hugging Face.

A NVIDIA distribui o Canary-1B pelo Hugging Face e pelo framework NeMo para uso auto-hospedado, e também como API hospedada via NVIDIA NIM. O Canary-1B original é licenciado sob CC-BY-NC 4.0, que restringe o uso a fins não comerciais. Desde então, a NVIDIA lançou variantes mais novas, incluindo Canary-1B-Flash e Canary-1B-v2, sob a licença mais permissiva CC-BY-4.0, com autorização comercial explícita e inferência mais rápida.
