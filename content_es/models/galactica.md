---
title: 'Galactica'
name: 'Galactica'
slug: 'galactica'
subtitle: 'Modelo de Meta de 2022 entrenado con literatura científica, retirado a los pocos días del lanzamiento'
description: 'Modelo de Meta de 2022 entrenado con literatura científica, retirado a los pocos días del lanzamiento'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://galactica.org/'
price: 'Free'
rank: 3
release_date: '2022-11-15'
param_count: '120B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Non-commercial research license'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, science, legacy]
i18n_source: 'b7bc3c6e1cc7'
---

Galactica es un modelo de lenguaje que Meta AI construyó en concreto para la ciencia, entrenado con 48 millones de artículos, libros de texto, material de referencia y enciclopedias, y no con el texto web general con el que se entrenan la mayoría de los modelos de lenguaje grandes. Meta lo publicó en noviembre de 2022 en tamaños que iban de 125 millones a 120 000 millones de parámetros, y la versión más grande se entrenó con unos 106 000 millones de tokens de texto científico seleccionado. Podía generar citas, resolver problemas de matemáticas, escribir notación química y redactar artículos al estilo de Wikipedia, y Meta lo presentó como una herramienta para que quienes investigan resumieran artículos y buscaran en la literatura científica.

La demo pública se retiró a los tres días del lanzamiento, después de que se mostrara que producía citas inventadas y afirmaciones científicas erróneas, dichas con un tono de autoridad. El episodio se convirtió en un ejemplo temprano muy citado de los riesgos de publicar modelos generativos sin salvaguardas suficientes, y es anterior al lanzamiento de ChatGPT en unas dos semanas. Meta dejó los pesos disponibles para investigadores en Hugging Face bajo una licencia no comercial, y hoy Galactica se cita sobre todo como un caso de advertencia, no como una herramienta en uso.
