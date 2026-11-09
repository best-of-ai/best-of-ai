---
title: 'Llama 2'
name: 'Llama 2'
slug: 'llama-2'
subtitle: 'El lanzamiento de pesos abiertos de Meta en 2023 que puso en marcha el ecosistema abierto de LLM'
description: 'El lanzamiento de pesos abiertos de Meta en 2023 que puso en marcha el ecosistema abierto de LLM'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2023-07-18'
param_count: '70B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
mmlu_score: 68.9
humaneval_score: 29.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '69c51717a945'
---

Llama 2 es la línea de modelos de lenguaje de pesos abiertos de segunda generación de Meta, publicada el 18 de julio de 2023 en tamaños de 7B, 13B y 70B, junto a versiones de chat de cada uno. Se entrenó con 2 billones de tokens y admite una ventana de contexto de 4096 tokens, modesta para lo que vino después, pero competitiva cuando salió. El modelo de 70B obtuvo 68,9 en MMLU, cerca de GPT-3.5, aunque se quedó muy atrás en generación de código: solo llegó a 29,9 en HumanEval, frente al 48,1 de GPT-3.5. Lo que importó más que las puntuaciones en bruto fue la licencia: Meta permitió el uso comercial para la mayoría de las empresas, lo que hizo de Llama 2 el primer modelo de pesos abiertos de verdad lo bastante bueno para construir productos, y arrancó la oleada de fine-tunes, variantes cuantizadas y modelos derivados que hoy llenan Hugging Face. Los pesos siguen pudiéndose descargar gratis años después, aunque Meta ha publicado desde entonces Llama 3 y Llama 4.
