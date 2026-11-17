---
title: 'CodeGen2'
name: 'CodeGen2'
slug: 'codegen2'
subtitle: "Modelo de código aberto da Salesforce para preenchimento e síntese de programas em várias etapas"
description: "Modelo de código aberto da Salesforce para preenchimento e síntese de programas em várias etapas"
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeGen2'
price: 'Free'
rank: 5
release_date: '2023-05-03'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [code, open-weight]
i18n_source: '19442e527069'
---

O CodeGen2 é a segunda geração da família de modelos abertos de código da Salesforce Research, lançada em maio de 2023 como continuação do CodeGen original. Há quatro tamanhos: 1B, 3,7B, 7B e 16B parâmetros. A principal melhoria em relação ao primeiro CodeGen é o suporte a preenchimento de lacunas: o modelo completa um trecho de código ausente usando o contexto que aparece antes e depois, em vez de apenas gerar texto da esquerda para a direita. Isso o torna mais adequado a fluxos reais de edição, como preenchimento automático e correção de código, nos quais é necessário escrever no meio de um arquivo existente.

Os modelos foram treinados com uma mistura de linguagem natural e código-fonte de várias linguagens de programação. São publicados sob a licença permissiva Apache 2.0 pelo Hugging Face e pelo GitHub. O CodeGen2 foi testado com contexto útil de cerca de 2.000 tokens, modesto para os padrões atuais, mas típico de modelos de código daquela época. A Salesforce o apresentou como alternativa de pesquisa aberta a modelos fechados como o Codex; depois, lançou o CodeGen2.5, menor e ajustado para igualar o desempenho dos antecessores maiores.
