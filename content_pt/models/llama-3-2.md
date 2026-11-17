---
title: 'Llama 3.2'
name: 'Llama 3.2'
slug: 'llama-3-2'
subtitle: "Primeira geração Llama da Meta com variantes capazes de visão e execução em dispositivos"
description: "Primeira geração Llama da Meta com variantes capazes de visão e execução em dispositivos"
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2024-09-25'
param_count: '90B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Llama 3.2 Community License'
api_available: true
mmlu_score: 86.0
lmarena_score: 1250
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, self-hosted]
extra_model_types: ['Reasoning']
i18n_source: '70c7f383bbf6'
---

Llama 3.2 é o lançamento da Meta de setembro de 2024 que introduziu visão na linha Llama, junto com um conjunto de pequenos modelos somente de texto criados para celulares e dispositivos de borda. A variante de visão principal 90B combina uma arquitetura de texto Llama 3.1 com um codificador de imagem treinado em cerca de seis bilhões de pares imagem-texto, permitindo ler gráficos, legendar fotos e responder a perguntas sobre imagens, além de receber prompts de texto simples. A Meta também lançou modelos leves 1B e 3B na mesma família, voltados à execução local em hardware móvel, e não em um centro de dados. Em benchmarks de raciocínio, o modelo 90B tem desempenho próximo ao Llama 3.1 70B, acrescentando entrada multimodal, e é distribuído sob a Llama 3.2 Community License, com pesos no Hugging Face.
