---
title: 'MiniMax M3'
name: 'MiniMax M3'
slug: 'minimax-m3'
subtitle: 'El primer modelo de pesos abiertos que une programación de frontera, un contexto de 1 millón de tokens y multimodalidad nativa'
description: 'El primer modelo de pesos abiertos que une programación de frontera, un contexto de 1 millón de tokens y multimodalidad nativa'
company: 'minimax-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.minimaxi.com/'
price: 'Free'
rank: 8
release_date: '2026-06-01'
param_count: '428B (23B active)'
context_window_tokens: 1000000
modality: [text, image, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 1.2
api_available: true
lmarena_score: 1340
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, long-context, coding]
extra_model_types: ['Code']
i18n_source: 'b89f089ecadf'
---

MiniMax M3 es un modelo de mezcla de expertos y de pesos abiertos que MiniMax publicó en junio de 2026, con los pesos en Hugging Face el 7 de junio. Tiene unos 428 000 millones de parámetros en total, con cerca de 23 000 millones activos por token, repartidos en 256 expertos de grano fino. MiniMax lo presenta como el primer modelo de pesos abiertos que junta capacidad de programación de nivel frontera, una ventana de contexto de 1 millón de tokens y entrada multimodal nativa de texto, imágenes y vídeo. El laboratorio informa de un 59 % en SWE-Bench Pro y un 66 % en Terminal-Bench 2.1, benchmarks orientados a programación de larga duración y a tareas de agentes, no a responder una pregunta suelta.

La arquitectura está hecha para que la inferencia de contexto largo salga barata: MiniMax dice que el coste de cómputo por token, a 1 millón de tokens, es una fracción del de su generación anterior, con el prefill y la decodificación varias veces más rápidos. Se publica bajo Apache 2.0 y se cobra a 0,30 $ por millón de tokens de entrada y 1,20 $ por millón de tokens de salida en la API de MiniMax. Queda como alternativa abierta y de menor coste frente a los modelos cerrados de programación de frontera, para quien construye agentes de programación autónomos y herramientas que trabajan sobre bases de código grandes.
