---
title: 'DistilBERT'
name: 'DistilBERT'
slug: 'distilbert'
subtitle: 'Versión destilada de BERT de Hugging Face, un 40 % más pequeña, que conserva la mayor parte del rendimiento'
description: 'Versión destilada de BERT de Hugging Face, un 40 % más pequeña, que conserva la mayor parte del rendimiento'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1910.01108'
price: 'Free'
rank: 7
release_date: '2019-10-02'
param_count: '66M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, small-model]
i18n_source: '4bb37eb28b4c'
---

DistilBERT es una versión comprimida del BERT de Google que Hugging Face publicó en octubre de 2019. Usa una técnica llamada destilación de conocimiento para entrenar un modelo alumno más pequeño que imite las salidas del BERT maestro durante el preentrenamiento. Con 66 millones de parámetros, es un 40 % más pequeño que el BERT-base original y va cerca de un 60 % más rápido, y conserva alrededor del 97 % del rendimiento de BERT en la suite de benchmarks GLUE. En tareas como la respuesta a preguntas de SQuAD y la clasificación de sentimiento de IMDb se queda a pocos puntos del BERT completo, pese al recorte de tamaño.

El artículo, «DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter», se convirtió en uno de los más citados en NLP, y el modelo pasó a ser la opción por defecto para equipos que necesitaban comprensión del lenguaje al nivel de BERT en hardware limitado, incluidos los móviles. Se publica bajo la licencia Apache 2.0 y sigue siendo uno de los modelos más descargados en Hugging Face años después de su salida.
