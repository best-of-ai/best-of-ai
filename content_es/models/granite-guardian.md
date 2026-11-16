---
title: 'Granite Guardian'
name: 'Granite Guardian'
slug: 'granite-guardian'
subtitle: 'El modelo de seguridad y detección de riesgos de IBM para filtrar entradas y salidas dañinas de un LLM'
description: 'El modelo de seguridad y detección de riesgos de IBM para filtrar entradas y salidas dañinas de un LLM'
company: 'ibm'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2024-10-21'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [safety, open-weight, enterprise]
i18n_source: '6ce71d1a9d0a'
---

Granite Guardian es la familia de modelos de seguridad de IBM, pensada para situarse junto a un LLM principal y marcar prompts o respuestas de riesgo antes de que lleguen a un usuario o a una aplicación. Salió con Granite 3.0 en octubre de 2024, en tamaños de 2B y 8B, ambos con fine-tuning a partir de los modelos instruct base de Granite y no entrenados desde cero. Comprueba daños catalogados en el AI Risk Atlas de IBM: intentos de jailbreak, lenguaje soez, sesgo social, violencia y llamadas a herramientas o resultados de recuperación alucinados en flujos de trabajo de agentes. IBM también ofrece una variante HAP (odio, abuso, lenguaje soez) mucho más pequeña, de 38 millones de parámetros, para equipos que necesitan barreras con presupuestos más ajustados de latencia o coste. Granite Guardian es de pesos abiertos bajo Apache 2.0 y se distribuye por Hugging Face, Ollama, NVIDIA y watsonx. Actualizaciones posteriores, incluida una 3.3 y una 4.1 con soporte para criterios de juicio definidos por el usuario, extendieron el mismo enfoque a modelos base de Granite más nuevos.
