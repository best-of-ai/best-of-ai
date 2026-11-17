---
title: 'Chameleon'
name: 'Chameleon'
slug: 'chameleon'
subtitle: "Modelo de fusão inicial da Meta que combina nativamente tokens de texto e imagem"
description: "Modelo de fusão inicial da Meta que combina nativamente tokens de texto e imagem"
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-fair-research-new-releases/'
price: 'Free'
rank: 6
release_date: '2024-05-16'
param_count: '34B'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'Research-only'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, open-weight]
extra_model_types: ['Image Generation']
i18n_source: '6e820e7a5edb'
---

O Chameleon é um modelo multimodal da Meta FAIR, descrito em um artigo de maio de 2024, que combina texto e imagens desde o início, em vez de acoplar um encoder de visão a um modelo de linguagem. A maioria dos sistemas multimodais usa “fusão tardia”, em que um encoder de imagem separado envia recursos visuais a um modelo de linguagem pré-treinado apenas com texto. O Chameleon, por sua vez, quantiza imagens em tokens discretos e treina do zero com sequências intercaladas de tokens de texto e imagem, para que o mesmo transformer aprenda a raciocinar sobre as duas modalidades e também possa gerar imagens, não apenas descrevê-las.

A Meta lançou dois tamanhos, Chameleon-7B e Chameleon-34B, e informou que a versão 34B superou modelos como Flamingo e IDEFICS em legendagem de imagens e perguntas visuais, além de competir com GPT-4V e Gemini Pro em testes de preferência humana em pares para tarefas de geração multimodal. Os pesos estão disponíveis no GitHub sob uma licença apenas para pesquisa, portanto o Chameleon não pode ser usado comercialmente. A Meta o apresentou principalmente como demonstração do treinamento por fusão inicial, e não como produto. Ideias do Chameleon influenciaram os modelos multimodais Llama posteriores da Meta, que ampliaram o treinamento no estilo de fusão inicial para uma linha de modelos mais abrangente, licenciada para uso comercial.
