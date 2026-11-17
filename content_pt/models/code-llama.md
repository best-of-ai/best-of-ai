---
title: 'Code Llama'
name: 'Code Llama'
slug: 'code-llama'
subtitle: "Variante Llama da Meta especializada em código e com pesos abertos"
description: "Variante Llama da Meta especializada em código e com pesos abertos"
company: 'meta-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://ai.meta.com/blog/code-llama-large-language-model-coding/'
price: 'Free'
rank: 6
release_date: '2023-08-24'
param_count: '34B'
context_window_tokens: 100000
modality: [text, code]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
humaneval_score: 53.7
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: 'f77a90c92a53'
---

O Code Llama é a versão do Llama 2 da Meta especializada em código, lançada em agosto de 2023. Foi treinado adicionalmente com dados focados em código a partir dos pesos base do Llama 2 e chegou em três tamanhos fundamentais — 7B, 13B e 34B parâmetros —, cada um com versão base, versão especializada em Python e versão ajustada para instruções, voltada a assistência de programação por chat. Mais tarde, a Meta adicionou uma variante 70B. Uma mudança importante em relação ao Llama 2 base foi ampliar a janela de contexto de 4.096 para até 100 mil tokens, ajustando os embeddings posicionais RoPE. Isso tornou o modelo muito mais útil para ler e editar arquivos longos ou bases de código inteiras de uma vez.

No benchmark HumanEval, o modelo 34B obteve 53,7% em pass@1, aproximadamente no nível do GPT-3.5 na época do lançamento, mas bem abaixo do GPT-4. O Code Llama é publicado sob a mesma licença comunitária Llama 2 do modelo original, que permite uso comercial para a maioria das empresas, e seus pesos podem ser baixados gratuitamente do Hugging Face. Foi um dos primeiros modelos de programação com pesos abertos amplamente adotados e estabeleceu uma referência para modelos posteriores, como Codestral e DeepSeek Coder.
