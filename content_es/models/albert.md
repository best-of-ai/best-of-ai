---
title: 'ALBERT'
name: 'ALBERT'
slug: 'albert'
subtitle: 'Variante de BERT de Google que comparte parámetros para ser eficiente a gran escala'
description: 'Variante de BERT de Google que comparte parámetros para ser eficiente a gran escala'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1909.11942'
price: 'Free'
rank: 6
release_date: '2019-09-26'
param_count: '223M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
i18n_source: '4c3c3afa8529'
---

ALBERT (A Lite BERT) es un modelo de representación del lenguaje que Google Research y el Toyota Technological Institute publicaron en septiembre de 2019 como continuación de BERT. Usa dos trucos para reducir parámetros, la parametrización factorizada de los embeddings y el uso compartido de parámetros entre capas, para recortar con fuerza el número de parámetros sin dejar de competir en precisión con modelos mucho más grandes. La configuración mayor, ALBERT-xxlarge, con unos 223 millones de parámetros, tiene aproximadamente 18 veces menos parámetros que BERT-large, entrena más rápido y, en el momento de su publicación, marcó nuevas puntuaciones máximas en GLUE, SQuAD 2.0 y RACE.

Como BERT, ALBERT es un modelo solo encoder, pensado para tareas de comprensión como la clasificación, la respuesta a preguntas y la comprensión lectora, y no para generar texto abierto, y limita la entrada a 512 tokens por secuencia. Google publicó el código y los pesos preentrenados de forma abierta, y el modelo se convirtió en una referencia habitual en la investigación de NLP y en sistemas de producción a principios de la década de 2020, antes de que los modelos generativos solo decoder acapararan casi toda la atención del campo.
