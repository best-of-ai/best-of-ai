---
title: 'CogVideoX'
name: 'CogVideoX'
slug: 'cogvideox'
subtitle: "Família de modelos de texto para vídeo com pesos abertos da Zhipu"
description: "Família de modelos de texto para vídeo com pesos abertos da Zhipu"
company: 'zhipu-ai'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogVideo'
price: 'Free'
rank: 6
release_date: '2024-08-27'
param_count: '5B'
modality: [text, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [video-generation, open-weight, api]
i18n_source: '892ae410997f'
---

O CogVideoX é o modelo de texto para vídeo com pesos abertos da Zhipu AI, desenvolvido com o laboratório KEG da Universidade Tsinghua e lançado em agosto de 2024 como sucessor do projeto CogVideo original. Há variantes de 2B e 5B parâmetros, que usam um VAE causal 3D para compressão espacial e temporal junto com um transformer com LayerNorm adaptativa especializada. O modelo oferece geração de texto para vídeo, imagem para vídeo e continuação de vídeo a partir de um quadro ou prompt. A versão 5B gera clipes de até 10 segundos, com resolução de até 768p e 16 quadros por segundo; em novembro de 2024, a Zhipu lançou a atualização CogVideoX-1.5, com vídeos mais longos e de maior resolução. Os pesos estão sob Apache 2.0 no Hugging Face. A Zhipu também disponibiliza os modelos por sua própria API, oferecendo tanto uso local de um modelo aberto quanto serviço hospedado, de forma semelhante às opções de vídeo da Stability AI e da Runway.
