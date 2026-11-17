---
title: 'BLOOMZ'
name: 'BLOOMZ'
slug: 'bloomz'
subtitle: "Variante do BLOOM ajustada para seguir instruções em diferentes idiomas"
description: "Variante do BLOOM ajustada para seguir instruções em diferentes idiomas"
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/bigscience/bloomz'
price: 'Free'
rank: 5
release_date: '2022-11-03'
param_count: '176B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'RAIL License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual, legacy]
i18n_source: '9dff7db95770'
---

BLOOMZ é a versão do BLOOM ajustada para seguir instruções pelo BigScience, lançada no fim de 2022 após o ajuste fino do modelo-base de 176 bilhões de parâmetros com o xP3, uma grande coleção de tarefas multilíngues formuladas como instruções em linguagem natural. O projeto buscava generalização entre idiomas: o BLOOMZ foi ajustado principalmente com instruções em inglês, mas mostrou que conseguia seguir instruções em idiomas que nunca tinham sido associados a instruções durante o ajuste fino, desde que tivesse encontrado esses idiomas no pré-treinamento original do BLOOM. Foi uma das primeiras demonstrações públicas de que habilidades de seguimento de instruções podem ser transferidas entre idiomas, sem exigir ajuste separado para cada um.

Assim como o BLOOM, o BLOOMZ mantém a janela de contexto de 2.048 tokens e a arquitetura transformer densa do modelo-base, e é distribuído sob a mesma licença RAIL, que permite amplo uso com uma lista de aplicações proibidas. Hoje, interessa principalmente a pesquisadores que estudam ajuste de instruções multilíngue, em vez de servir como modelo de chat para produção, pois modelos abertos mais recentes, ajustados para seguir instruções, oferecem melhor qualidade e janelas de contexto muito maiores com custo computacional semelhante ou menor.
