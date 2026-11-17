---
title: MiniCPM-V
name: MiniCPM-V
slug: minicpm-v
subtitle: Modelo multimodal de borda da OpenBMB, capaz de realizar em celulares tarefas
  visuais no nível do GPT-4V
description: Modelo multimodal de borda da OpenBMB, capaz de realizar em celulares
  tarefas visuais no nível do GPT-4V
company: openbmb
model_type: Multimodal
logo_url: ''
product_url: https://github.com/OpenBMB/MiniCPM-V
price: Free
rank: 5
release_date: '2024-05-20'
param_count: 8B
context_window_tokens: 32768
modality:
- text
- image
- video
open_weight: true
license: Apache 2.0
api_available: false
access_methods:
- Self-hosted
runs_at_home: true
platforms:
- Hugging Face
date: '2026-07-16'
tags:
- multimodal
- open-weight
- small-model
- on-device
i18n_source: '83a16a62bccc'
---
MiniCPM-V é uma linha de modelos de linguagem e visão com pesos abertos da OpenBMB, laboratório de pesquisa criado a partir da Universidade Tsinghua. A linha foi desenvolvida para executar compreensão de imagens e vídeos em celulares e outros dispositivos com recursos limitados, sem exigir uma GPU de servidor. A versão lançada em maio de 2024, MiniCPM-Llama3-V 2.5, combina uma base Llama3 de 8B parâmetros com um encoder visual SigLip. Segundo a OpenBMB, seu desempenho em OCR, raciocínio com várias imagens e respostas gerais a perguntas visuais iguala ou supera o GPT-4V em vários benchmarks públicos, mesmo funcionando totalmente offline em um celular.

A OpenBMB continuou desenvolvendo a série, com versões posteriores como MiniCPM-V 4.5 e 4.6 reduzindo ainda mais o número de parâmetros e melhorando a precisão. Isso reflete uma tendência mais ampla de diminuir a diferença entre modelos multimodais pequenos, executados no dispositivo, e modelos muito maiores hospedados na nuvem. Os modelos são distribuídos sob a licença Apache 2.0 no Hugging Face e no GitHub, para desenvolvedores que precisam de IA multimodal offline e com proteção de privacidade em hardware de consumo.
