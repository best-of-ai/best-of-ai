---
title: 'Devstral'
name: 'Devstral'
slug: 'devstral'
subtitle: 'Modelo de pesos abertos da Mistral ajustado para programação agêntica e exploração de bases de código'
description: 'Modelo de pesos abertos da Mistral ajustado para programação agêntica e exploração de bases de código'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/devstral/'
price: 'Free'
rank: 6
release_date: '2025-05-21'
param_count: '24B'
context_window_tokens: 128000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0.3
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, agentic, api]
i18n_source: '10cd7f3fca31'
---

O Devstral é um modelo de código com 24 bilhões de parâmetros lançado pela Mistral AI em 21 de maio de 2025, desenvolvido em colaboração com a All Hands AI, equipe por trás do framework de agentes OpenHands. Diferentemente da maioria dos modelos de código, ajustados principalmente para autocompletar ou gerar trechos em uma única etapa, o Devstral foi treinado especificamente para programação agêntica: explorar vários arquivos de uma base de código, usar ferramentas e concluir tarefas de engenharia de software em várias etapas. No SWE-bench Verified, marcou 46,8%, superando todos os modelos abertos disponíveis no lançamento e até alguns modelos proprietários maiores.

A Mistral publicou os pesos sob a licença Apache 2.0. O modelo é pequeno o bastante para rodar em uma única GPU de consumo de alto desempenho, tornando-se uma base popular para agentes locais de programação. A Mistral lançou depois o Devstral Small 1.1 e o maior Devstral 2, ambos com pontuações mais altas no SWE-bench. O Devstral original continua notável por ter sido um dos primeiros modelos abertos criados especificamente para engenharia de software agêntica, em vez de completar código para uso geral.