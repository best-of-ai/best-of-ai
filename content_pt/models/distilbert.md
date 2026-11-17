---
title: 'DistilBERT'
name: 'DistilBERT'
slug: 'distilbert'
subtitle: 'Versão destilada do BERT pela Hugging Face, 40% menor e com a maior parte do desempenho original'
description: 'Versão destilada do BERT pela Hugging Face, 40% menor e com a maior parte do desempenho original'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1910.01108'
price: 'Free'
rank: 7
release_date: '2019-10-02'
param_count: '66M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, small-model]
i18n_source: '4bb37eb28b4c'
---

O DistilBERT é uma versão compactada do BERT do Google, lançada pela Hugging Face em outubro de 2019. Usa uma técnica chamada destilação de conhecimento para treinar um modelo aluno menor que imita as saídas do modelo professor BERT maior durante o pré-treinamento. Com 66 milhões de parâmetros, é 40% menor que o BERT-base original e roda cerca de 60% mais rápido, mantendo aproximadamente 97% do desempenho do BERT na série de benchmarks GLUE. Em tarefas como perguntas e respostas do SQuAD e classificação de sentimento no IMDb, fica a poucos pontos do BERT completo apesar do tamanho reduzido.

O artigo “DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter” tornou-se um dos mais citados em PLN. O modelo virou uma escolha padrão para equipes que precisam de compreensão de linguagem no nível do BERT em hardware limitado, inclusive dispositivos móveis. É publicado sob a licença Apache 2.0 e continua entre os modelos mais baixados no Hugging Face, anos após o lançamento.