---
title: 'Flan-T5'
name: 'Flan-T5'
slug: 'flan-t5'
subtitle: "Sucessor de pesos abertos do T5, ajustado para seguir instruções pelo Google"
description: "Sucessor de pesos abertos do T5, ajustado para seguir instruções pelo Google"
company: 'google'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/google/flan-t5-xxl'
price: 'Free'
rank: 4
release_date: '2022-10-20'
param_count: '11B'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, instruction-tuned, legacy]
i18n_source: '01962c85d25c'
---

O Flan-T5 é a versão do T5 ajustada para seguir instruções, lançada pelo Google em outubro de 2022. Em vez de alterar a arquitetura base, o Google ajustou o T5 em mais de mil tarefas formuladas como instruções, abrangendo tradução, resumo, raciocínio e classificação em muitos idiomas. Esse ajuste o tornou muito mais útil diretamente do que o T5 padrão, que precisava ser ajustado para cada tarefa para ter bom desempenho. O Google lançou a família em vários tamanhos, desde uma versão pequena de 80 milhões de parâmetros até o Flan-T5-XXL, com 11 bilhões de parâmetros; todos estão sob Apache 2.0 e podem ser baixados gratuitamente no Hugging Face. Sua janela de contexto de 512 tokens é curta para os padrões atuais e limita o modelo a documentos e prompts menores. Ainda é uma referência comum em pesquisas sobre ajuste de instruções e uma opção leve para equipes que querem um modelo aberto e auto-hospedado para tarefas simples de PLN, sem o custo computacional de um LLM decodificador maior.
