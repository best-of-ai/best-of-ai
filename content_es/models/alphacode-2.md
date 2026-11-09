---
title: 'AlphaCode 2'
name: 'AlphaCode 2'
slug: 'alphacode-2'
subtitle: 'Modelo de programación competitiva de DeepMind, basado en Gemini, entre los mejores competidores humanos'
description: 'Modelo de programación competitiva de DeepMind, basado en Gemini, entre los mejores competidores humanos'
company: 'google-deepmind'
model_type: 'Code'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/alphacode-2-technical-report/'
price: 'Paid'
rank: 6
release_date: '2023-12-06'
param_count: 'Undisclosed'
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [code, research]
i18n_source: 'd985a201f8f1'
---

AlphaCode 2 es el sistema de programación competitiva de Google DeepMind, publicado como informe técnico en diciembre de 2023 como continuación del AlphaCode original. No es un solo modelo, sino un proceso construido sobre modelos Gemini con fine-tuning: muestrea hasta un millón de soluciones candidatas en C++ por problema y luego las filtra con comprobaciones basadas en tests, agrupación por comportamiento y un modelo de puntuación aprendido, hasta quedarse con unas diez entregas finales. En un conjunto de concursos recientes de Codeforces resolvió el 43 % de los problemas en un máximo de diez intentos, casi el doble del 25 % del AlphaCode original.

DeepMind estimó que el rendimiento de AlphaCode 2 lo situaría en el percentil 85 entre los competidores humanos de Codeforces, entre los rangos Expert y Candidate Master de esa plataforma. El proyecto fue solo de investigación, nunca se publicó como producto ni como API, y sirvió sobre todo para mostrar cuánto puede mejorar un modelo base sólido, más un muestreo y un filtrado intensos, en problemas de programación difíciles y verificables. Es un antecesor directo de las técnicas de razonamiento y de generación de código que después se incorporaron al trabajo de DeepMind en Gemini y AlphaProof.
