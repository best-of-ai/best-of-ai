---
title: 'SenseNova Loop-9B'
name: 'SenseNova Loop-9B'
slug: 'sensenova-loop-9b'
subtitle: "Modelo multimodal de 9B com pesos abertos da SenseTime que reutiliza suas camadas em loop"
description: "Modelo multimodal de 9B com pesos abertos da SenseTime que reutiliza suas camadas em loop"
company: 'sensetime'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.sensetime.com/en/news/sensenova-loop-9b-release-20261118-1435'
price: 'Free'
rank: 5
release_date: '2026-11-17'
param_count: '9B (about 14.6B inference-equivalent)'
context_window_tokens: 512000
modality: [text, image]
open_weight: true
license: 'Open weights'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-11-24'
tags: [llm, open-weight, multimodal, small-model, self-hosted]
i18n_source: '842af8c2e04b'
---

O SenseNova Loop-9B é o lançamento oficial do modelo multimodal com pesos abertos da SenseTime, publicado em 17 de novembro de 2026 após uma prévia. Tem cerca de 9B de parâmetros em 32 camadas de decodificador distintas, que rodam como 56 computações de camada por passada, o que dá aproximadamente 14,6B de parâmetros equivalentes na inferência. Aceita texto e imagens, produz texto e lida com até 512.000 tokens de contexto.

Os pesos de 4 bits têm cerca de 4,9 GB, então cabem em hardware de consumo, e uma versão AWQ oficial saiu no dia do lançamento. A SenseTime o chama de comparável ao Qwen3.8-27B: 41,36 contra 44,60 no NL2Repo e 65,31 contra 65,01 no AIDABench. Os pesos estão no Hugging Face em sensenova/sensenova-loop, com o código no GitHub.
