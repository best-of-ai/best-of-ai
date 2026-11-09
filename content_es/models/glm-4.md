---
title: 'GLM-4'
name: 'GLM-4'
slug: 'glm-4'
subtitle: 'Modelo de uso general y pesos abiertos de Zhipu, de 2024'
description: 'Modelo de uso general y pesos abiertos de Zhipu, de 2024'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 5
release_date: '2024-06-05'
param_count: '9B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 72.4
humaneval_score: 71.8
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted]
i18n_source: 'b05c60de4627'
---

GLM-4 es el lanzamiento de pesos abiertos de Zhipu AI de junio de 2024, distribuido como GLM-4-9B con variantes base, chat y de contexto largo. Con 9000 millones de parámetros es lo bastante pequeño para correr en una sola GPU de gama alta, y aun así Zhipu informó de que superaba al Llama 3 8B de Meta en evaluaciones semánticas, matemáticas, de razonamiento y de código. La variante de chat también admite navegación web, ejecución de código y llamadas a herramientas propias mediante function calling, más una ventana de contexto que llega a 128 000 tokens.

El modelo añadió soporte para 26 idiomas además del chino y el inglés, entre ellos japonés, coreano y alemán, lo que amplió su uso fuera del mercado de origen de Zhipu. Publicado bajo Apache 2.0, GLM-4 se convirtió en uno de los modelos pequeños de pesos abiertos más adoptados en Hugging Face y fijó la arquitectura base que Zhipu escaló después en GLM-4-Plus, GLM-4.5 y GLM-4.6.
