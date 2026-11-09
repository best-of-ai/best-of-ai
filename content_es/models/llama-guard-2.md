---
title: 'Llama Guard 2'
name: 'Llama Guard 2'
slug: 'llama-guard-2'
subtitle: 'El modelo clasificador de seguridad de contenido anterior de Meta, previo a Llama Guard 3'
description: 'El modelo clasificador de seguridad de contenido anterior de Meta, previo a Llama Guard 3'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-llama-3/'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [safety, open-weight, legacy]
i18n_source: '1ec3f0456e4e'
---

Llama Guard 2 es un clasificador de seguridad de contenido que Meta publicó junto a Llama 3 en abril de 2024, construido sobre una base Llama 3 de 8B y no como modelo de chat de propósito general. Revisa tanto los prompts que entran en un modelo de lenguaje como las respuestas que salen, y marca contenido en 11 categorías de riesgo tomadas de la taxonomía de MLCommons: violencia, discurso de odio y contenido sexual, entre otras. Los desarrolladores lo ejecutan como barrera delante o detrás de otro LLM en una canalización, en lugar de usarlo para generar respuestas directamente. Meta lo ha sustituido desde entonces por Llama Guard 3, pero sigue disponible en Hugging Face bajo la Llama 3 Community License para equipos que ya lo tienen en producción.
