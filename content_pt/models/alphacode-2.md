---
title: 'AlphaCode 2'
name: 'AlphaCode 2'
slug: 'alphacode-2'
subtitle: "Modelo de programação competitiva da DeepMind baseado no Gemini, entre os melhores competidores humanos"
description: "Modelo de programação competitiva da DeepMind baseado no Gemini, entre os melhores competidores humanos"
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

AlphaCode 2 é o sistema de programação competitiva do Google DeepMind, publicado como relatório técnico em dezembro de 2023, como continuação do AlphaCode original. Em vez de ser um único modelo, é um fluxo de processamento baseado em modelos Gemini ajustados: ele amostra até um milhão de soluções em C++ para cada problema e depois as filtra com verificações baseadas em testes, agrupamento por comportamento e um modelo de pontuação aprendido, selecionando cerca de dez respostas finais. Em um conjunto de competições recentes do Codeforces, resolveu 43% dos problemas em até dez tentativas, quase o dobro dos 25% do AlphaCode original.

O DeepMind estimou que o desempenho do AlphaCode 2 o colocaria no percentil 85 entre os competidores humanos do Codeforces, entre as classificações “Expert” e “Candidate Master” da plataforma. O projeto foi apenas de pesquisa e nunca foi lançado como produto ou API; seu principal objetivo foi demonstrar quanto um bom modelo-base, combinado com amostragem e filtragem intensivas, pode melhorar o desempenho em problemas de programação difíceis e verificáveis. Ele é um antecessor direto das técnicas de raciocínio e geração de código posteriormente incorporadas às linhas Gemini e AlphaProof do DeepMind.
