---
title: 'Flamingo'
name: 'Flamingo'
slug: 'flamingo'
subtitle: "Modelo visão-linguagem da DeepMind que introduziu o raciocínio multimodal com poucos exemplos"
description: "Modelo visão-linguagem da DeepMind que introduziu o raciocínio multimodal com poucos exemplos"
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/tackling-multiple-tasks-with-a-single-visual-language-model/'
price: 'Paid'
rank: 6
release_date: '2022-04-29'
param_count: '80B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, vision, research]
i18n_source: '98bf1c585f2e'
---

O Flamingo é um modelo visão-linguagem publicado pela DeepMind em abril de 2022, criado para processar imagens, vídeos e texto em conjunto e responder a perguntas abertas depois de ver apenas alguns exemplos. Ele parte do Chinchilla, modelo de linguagem de 70B parâmetros da DeepMind, e adiciona encoders de visão e camadas de atenção cruzada que permitem condicionar a geração de texto à entrada visual, levando o modelo completo a cerca de 80B parâmetros. A ideia central era o aprendizado com poucos exemplos em tarefas visão-linguagem: em vez de ajustar o modelo para cada novo conjunto de dados, bastava incluir alguns exemplos no prompt para que o Flamingo generalizasse, de forma semelhante ao GPT-3 em tarefas de texto. No lançamento, superou todas as abordagens anteriores de poucos exemplos em 16 benchmarks visão-linguagem, incluindo legendagem, perguntas visuais e diálogo visual. A DeepMind nunca lançou o Flamingo como produto ou API pública; ele permaneceu um modelo de pesquisa, mas sua arquitetura influenciou sistemas multimodais posteriores, incluindo reimplementações abertas como o OpenFlamingo e escolhas de design nos modelos multimodais subsequentes do Google.
