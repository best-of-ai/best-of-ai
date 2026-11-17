---
title: 'CodeT5+'
name: 'CodeT5+'
slug: 'codet5'
subtitle: "Família de modelos de código encoder-decoder de pesos abertos da Salesforce"
description: "Família de modelos de código encoder-decoder de pesos abertos da Salesforce"
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeT5'
price: 'Free'
rank: 3
release_date: '2023-05-13'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
humaneval_score: 30.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '20777365e144'
---

O CodeT5+ é uma família de modelos de código com pesos abertos criada pela Salesforce Research e lançada em maio de 2023 como continuação do modelo encoder-decoder CodeT5 original. Há vários tamanhos, de 220 milhões a 16 bilhões de parâmetros, e os modelos podem funcionar apenas como encoder, apenas como decoder ou como encoder-decoder completo. Assim, uma única arquitetura cobre tarefas de compreensão de código, como detecção de defeitos, e tarefas de geração, como conclusão de código e síntese de texto para código. O treinamento combina remoção de ruído em trechos, modelagem de linguagem causal, aprendizado contrastivo e correspondência entre texto e código; segundo a Salesforce, essa abordagem dá vantagem sobre modelos de código somente decodificadores de tamanho semelhante em tarefas RAG. A variante 16B alcança cerca de 30,9% em pass@1 no HumanEval, e uma versão do mesmo checkpoint ajustada para instruções supera 35%, vencendo o antigo code-cushman-001 da OpenAI no mesmo benchmark. Os pesos estão no Hugging Face sob licença BSD-3-Clause, tornando o CodeT5+ uma das primeiras alternativas totalmente abertas aos modelos proprietários da era Codex.
