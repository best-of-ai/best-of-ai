---
title: 'DeepSeek-MoE-16B'
name: 'DeepSeek-MoE-16B'
slug: 'deepseek-moe-16b'
subtitle: 'Modelo temprano de mezcla de expertos de grano fino de DeepSeek, que informó sus arquitecturas MoE posteriores'
description: 'Modelo temprano de mezcla de expertos de grano fino de DeepSeek, que informó sus arquitecturas MoE posteriores'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-MoE'
price: 'Free'
rank: 5
release_date: '2024-01-11'
param_count: '16.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
i18n_source: '61ec60299e14'
---

DeepSeek-MoE-16B, publicado en enero de 2024, fue el intento temprano de DeepSeek de una arquitectura de mezcla de expertos de grano fino, y sus decisiones de diseño pasaron a los modelos posteriores V2 y V3 de la empresa. Tiene 16 400 millones de parámetros en total, pero solo unos 2800 millones activos por token, algo que consigue con dos técnicas descritas en su artículo: partir los expertos en unidades más pequeñas y más especializadas, y aislar un conjunto de expertos compartidos que siempre se activan para capturar el conocimiento común. Entrenado desde cero con 2 billones de tokens en inglés y en chino, llegó a un rendimiento comparable al de los modelos densos DeepSeek 7B y Llama 2 7B usando solo alrededor del 40 % del cómputo que esos modelos necesitan en la inferencia. Tiene una ventana de contexto de 4096 tokens y se publicó bajo la licencia abierta de DeepSeek para uso autoalojado, sobre todo como demostración de investigación de la especialización de expertos y no como una publicación centrada en producción.
