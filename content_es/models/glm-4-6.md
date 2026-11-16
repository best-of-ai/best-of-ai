---
title: 'GLM-4.6'
name: 'GLM-4.6'
slug: 'glm-4-6'
subtitle: 'Modelo de pesos abiertos de gama económica de Zhipu, para la programación del día a día'
description: 'Modelo de pesos abiertos de gama económica de Zhipu, para la programación del día a día'
company: 'zhipu-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2025-09-30'
param_count: '355B (MoE, ~32B active)'
context_window_tokens: 200000
modality: [text, image, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 1.75
api_available: true
humaneval_score: 85.0
lmarena_score: 1320
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '89b99962ef6e'
---

GLM-4.6 es el modelo de pesos abiertos de gama económica de Zhipu (Z.ai), publicado el 30 de septiembre de 2025 como mejora de GLM-4.5. Usa un diseño de mezcla de expertos con unos 355 000 millones de parámetros en total y cerca de 32 000 millones activos por token, y su ventana de contexto pasó de 128 000 a 200 000 tokens para aguantar sesiones agénticas más largas. El modelo trabaja texto, imágenes y código, y Zhipu lo ajustó en concreto para el uso de herramientas dentro de asistentes de programación como Claude Code, Cline y Roo Code.

En benchmarks de programación el modelo queda cerca de lo más alto del campo de pesos abiertos: lidera LiveCodeBench v6 y compite con DeepSeek-V3.1-Terminus y Claude Sonnet 4 en varias tareas agénticas. Su principal argumento de venta es el precio: muy por debajo de un dólar por millón de tokens de entrada, queda muy por debajo de la mayoría de modelos insignia propietarios y sigue sirviendo para trabajo real de programación, por eso aparece a menudo en herramientas de desarrollo autoalojadas y por API.
