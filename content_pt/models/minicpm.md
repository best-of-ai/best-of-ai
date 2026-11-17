---
title: MiniCPM
name: MiniCPM
slug: minicpm
subtitle: Modelo pequeno e eficiente da OpenBMB, desenvolvido para funcionar bem em
  celulares e dispositivos de borda
description: Modelo pequeno e eficiente da OpenBMB, desenvolvido para funcionar bem
  em celulares e dispositivos de borda
company: openbmb
model_type: Language
logo_url: ''
product_url: https://github.com/OpenBMB/MiniCPM
price: Free
rank: 5
release_date: '2024-02-01'
param_count: 2.4B
context_window_tokens: 4096
modality:
- text
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
- llm
- open-weight
- small-model
- on-device
i18n_source: '0dcdb45ddc3c'
---
O MiniCPM é um modelo de linguagem com 2,4B parâmetros, lançado pela OpenBMB em fevereiro de 2024 e desenvolvido para funcionar bem em celulares e outros dispositivos de borda, nos quais um modelo de 7B ou 13B seria pesado demais. Apesar do tamanho reduzido, a OpenBMB informou que ele chega perto do Mistral 7B em benchmarks gerais e supera modelos maiores, como Llama 2 13B e Falcon 40B, em várias tarefas, especialmente compreensão de chinês, matemática e programação. Uma variante separada de contexto longo, MiniCPM-2B-128k, amplia a janela para 128.000 tokens em casos de uso com muitos documentos.

O modelo tem pesos abertos sob a licença Apache 2.0 e é distribuído pelo Hugging Face. Ele é voltado a desenvolvedores de aplicativos offline ou de baixo custo que precisam de um modelo capaz dentro de limites restritos de memória e processamento. Também serviu de base para os modelos multimodais MiniCPM-V posteriores da OpenBMB e ajudou a consolidar o foco do laboratório em IA eficiente e executada no dispositivo, como alternativa a simplesmente aumentar a escala dos modelos.
