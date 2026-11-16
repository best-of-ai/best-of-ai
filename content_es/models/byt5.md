---
title: 'ByT5'
name: 'ByT5'
slug: 'byt5'
subtitle: 'Variante de T5 de Google, sin tokens, que opera directamente sobre bytes en bruto'
description: 'Variante de T5 de Google, sin tokens, que opera directamente sobre bytes en bruto'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2105.13626'
price: 'Free'
rank: 4
release_date: '2021-05-28'
param_count: '13B'
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, research]
i18n_source: 'e8007dd611dd'
---

ByT5 es una variante del modelo de texto a texto T5 de Google que Google Research publicó a mediados de 2021. Destaca por prescindir por completo de la tokenización y operar directamente sobre bytes UTF-8 en bruto. Los modelos de lenguaje habituales parten el texto en tokens de subpalabras con un vocabulario fijo construido por un tokenizador, lo que funciona bien para las lenguas y los sistemas de escritura en torno a los que se construyó ese vocabulario, pero tiende a tratar mal las palabras raras, las faltas de ortografía y las lenguas menos habituales. ByT5 lo evita tratando cada entrada como una secuencia de bytes, con un vocabulario de solo unos cientos de valores posibles en lugar de decenas de miles de tokens de subpalabras.

La contrapartida es que las secuencias de bytes son mucho más largas que las de tokens para el mismo texto, así que ByT5 necesita encoders más profundos y más cómputo por entrada para igualar a los modelos basados en tokens en los benchmarks habituales. Google publicó una familia de tamaños de ByT5 hasta ByT5-XXL, de unos 13 000 millones de parámetros, con todos los checkpoints abiertos en Hugging Face bajo Apache 2.0. Fue especialmente bien en texto ruidoso, transliteración y tareas multilingües con sistemas de escritura de pocos recursos, lo que lo convirtió en una referencia útil en la investigación sobre modelado sin tokenización y a nivel de caracteres, aunque la mayoría de los modelos de lenguaje de producción se han quedado con enfoques basados en tokens por su eficiencia.
