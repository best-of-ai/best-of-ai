---
title: 'Gato'
name: 'Gato'
slug: 'gato'
subtitle: "Agente generalista único da DeepMind treinado com texto, imagens e controle robótico"
description: "Agente generalista único da DeepMind treinado com texto, imagens e controle robótico"
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/a-generalist-agent/'
price: 'Paid'
rank: 5
release_date: '2022-05-12'
param_count: '1.18B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, generalist-agent]
i18n_source: '7358d84afc22'
---

O Gato é uma única rede neural apresentada pela DeepMind em maio de 2022, cujos mesmos pesos podem executar mais de 600 tarefas: jogar Atari, legendar imagens, manter uma conversa por texto e controlar um braço robótico real para empilhar blocos. Em vez de treinar modelos separados para cada tarefa, a DeepMind serializou todas as entradas — texto, imagens, torques das articulações ou pressionamentos de botões — em uma única sequência plana de tokens e treinou um transformer único com todas elas. A arquitetura é semelhante à de um grande modelo de linguagem, mas os tokens representam ações e dados de sensores, além de palavras.

Com 1,18 bilhão de parâmetros, o Gato é pequeno diante dos 175 bilhões do GPT-3, e seu desempenho em cada tarefa fica abaixo do de especialistas desenvolvidos especificamente para ela. O que o tornou relevante foi demonstrar que uma única rede podia realizar razoavelmente bem tarefas tão diferentes, com modalidades e problemas de controle distintos. A DeepMind o descreveu como uma etapa de pesquisa rumo a agentes de uso mais geral, não como produto; o Gato nunca foi disponibilizado publicamente nem oferecido por API.
