---
title: 'Flan-T5'
name: 'Flan-T5'
slug: 'flan-t5'
subtitle: 'Sucesor de pesos abiertos de T5, de Google, ajustado con instrucciones'
description: 'Sucesor de pesos abiertos de T5, de Google, ajustado con instrucciones'
company: 'google'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/google/flan-t5-xxl'
price: 'Free'
rank: 4
release_date: '2022-10-20'
param_count: '11B'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, instruction-tuned, legacy]
i18n_source: '01962c85d25c'
---

Flan-T5 es la versión de T5 ajustada con instrucciones de Google, su transformer de texto a texto anterior, publicada en octubre de 2022. En lugar de cambiar la arquitectura base, Google hizo fine-tuning de T5 en más de mil tareas formuladas como instrucciones, que cubrían traducción, resumen, razonamiento y clasificación en muchos idiomas. Ese fine-tuning lo hizo mucho más usable de entrada que el T5 simple, que necesitaba un ajuste específico de la tarea para rendir bien. Google publicó la familia en varios tamaños, desde una versión pequeña de 80 millones de parámetros hasta Flan-T5-XXL, de 11 000 millones, todos bajo la licencia Apache 2.0 y descargables gratis en Hugging Face. Su ventana de contexto de 512 tokens es corta para los estándares actuales, lo que lo limita a documentos y prompts breves. Sigue siendo una referencia habitual en investigación sobre ajuste con instrucciones y una opción ligera para equipos que quieren un modelo abierto y autoalojado para tareas de NLP sencillas, sin el coste de cómputo de un LLM solo decodificador más grande.
