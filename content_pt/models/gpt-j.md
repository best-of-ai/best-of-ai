---
title: 'GPT-J'
name: 'GPT-J'
slug: 'gpt-j'
subtitle: 'GPT-J é um modelo de linguagem de 6 bilhões de parâmetros lançado pela EleutherAI em 9 de junho de 2021, uma das primeiras reproduções abertas convincentes da arquitetura GPT-3, numa época em que a OpenAI mantinha o próprio GPT-3 fechado atrás de uma API paga.'
description: 'GPT-J é um modelo de linguagem de 6 bilhões de parâmetros lançado pela EleutherAI em 9 de junho de 2021, uma das primeiras reproduções abertas convincentes da arquitetura GPT-3, numa época em que a OpenAI mantinha o próprio GPT-3 fechado atrás de uma API paga.'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 3
release_date: '2021-06-04'
param_count: '6B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '3c03d602f92a'
---

GPT-J é um modelo de linguagem de 6 bilhões de parâmetros lançado pela EleutherAI em 9 de junho de 2021, uma das primeiras reproduções abertas convincentes da arquitetura GPT-3, numa época em que a OpenAI mantinha o próprio GPT-3 fechado atrás de uma API paga. Foi treinado com o Pile, conjunto de dados de texto de 825 GB criado pela EleutherAI, usando a biblioteca Mesh Transformer JAX para paralelizar o treinamento em pods de TPU, em vez de GPUs. Com 28 camadas e uma janela de contexto de 2.048 tokens, era visivelmente menor que a configuração maior do GPT-3, mas ainda realizava geração de texto geral, respostas a perguntas e preenchimento de código suficientemente bem para se tornar uma referência padrão em pesquisa de PLN de código aberto. Foi lançado sob a licença Apache 2.0, permitindo que qualquer pessoa baixasse, ajustasse e implantasse o modelo sem as restrições de uso da OpenAI, o que o tornou uma base popular para os primeiros projetos abertos de chatbots. Desde então, GPT-J foi substituído por GPT-NeoX-20B e outros modelos abertos posteriores, mas continua sendo uma referência frequentemente citada sobre como a comunidade de código aberto alcançou os laboratórios fechados na era GPT-3.
