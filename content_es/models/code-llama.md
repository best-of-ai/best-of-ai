---
title: 'Code Llama'
name: 'Code Llama'
slug: 'code-llama'
subtitle: 'Variante de Llama de pesos abiertos de Meta, especializada en código'
description: 'Variante de Llama de pesos abiertos de Meta, especializada en código'
company: 'meta-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://ai.meta.com/blog/code-llama-large-language-model-coding/'
price: 'Free'
rank: 6
release_date: '2023-08-24'
param_count: '34B'
context_window_tokens: 100000
modality: [text, code]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
humaneval_score: 53.7
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: 'f77a90c92a53'
---

Code Llama es la versión de Llama 2 de Meta centrada en código, publicada en agosto de 2023. Se entrenó más a fondo con datos ricos en código sobre los pesos base de Llama 2 y salió en tres tamaños fundacionales (7B, 13B y 34B de parámetros), cada uno con una versión base, una versión especializada en Python y una versión ajustada para instrucciones, para ayuda a programar al estilo de un chat. Meta añadió después una variante de 70B. Un cambio clave respecto al modelo Llama 2 base fue ampliar la ventana de contexto de 4096 tokens hasta 100 000 tokens, mediante un ajuste de los embeddings posicionales RoPE, lo que hizo al modelo mucho más útil para leer y editar archivos largos o bases de código enteras de una pasada.

En el benchmark HumanEval, el modelo de 34B obtuvo un 53,7 % de pass@1, más o menos a la par de GPT-3.5 en el momento de la publicación, aunque muy por detrás de GPT-4. Code Llama se publica bajo la misma licencia Llama 2 Community License que su modelo de origen, que permite el uso comercial para la mayoría de las empresas, y sus pesos se pueden descargar de forma gratuita en Hugging Face. Fue uno de los primeros modelos de programación de pesos abiertos de adopción amplia y fijó una plantilla con la que competirían después otros modelos de código abiertos, entre ellos Codestral y DeepSeek Coder.
