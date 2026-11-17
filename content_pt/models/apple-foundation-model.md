---
title: 'Apple Foundation Model'
name: 'Apple Foundation Model'
slug: 'apple-foundation-model'
subtitle: "Modelos fundamentais da Apple, no dispositivo e em servidores, que alimentam o Apple Intelligence"
description: "Modelos fundamentais da Apple, no dispositivo e em servidores, que alimentam o Apple Intelligence"
company: 'apple'
model_type: 'Language'
logo_url: ''
product_url: 'https://machinelearning.apple.com/research/introducing-apple-foundation-models'
price: 'Paid'
rank: 6
release_date: '2024-06-10'
param_count: '3B (on-device)'
context_window_tokens: 32000
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['iOS', 'macOS']
date: '2026-07-16'
tags: [llm, on-device, foundation-model]
i18n_source: '7fbb8197cfde'
---

Os Foundation Models da Apple são o par de modelos de linguagem por trás do Apple Intelligence, apresentado em junho de 2024 na WWDC: um modelo com cerca de 3 bilhões de parâmetros, executado diretamente em hardware de iPhone, iPad e Mac, e um modelo maior, executado nos servidores Private Cloud Compute da própria Apple para tarefas que o modelo no dispositivo não consegue realizar sozinho. O modelo local usa técnicas como compartilhamento de cache KV e treinamento com reconhecimento de quantização de 2 bits para caber nos limites de memória e energia de um celular, enquanto o modelo de servidor usa uma arquitetura transformer de mistura de especialistas. A janela de contexto útil do modelo local é limitada a 4.096 tokens, enquanto o modelo de servidor aceita até 32.000 tokens.

A Apple não vende acesso por API a esses modelos como fazem OpenAI e Anthropic. Em vez disso, eles alimentam recursos integrados ao sistema, como ferramentas de escrita, resumos de notificações e os recursos renovados da Siri. Desde a WWDC 2025, eles também estão disponíveis para desenvolvedores terceirizados pelo framework Foundation Models, para que aplicativos possam chamar o modelo no dispositivo diretamente, de graça e sem conexão à internet. Desde então, a Apple atualizou a linha na WWDC 2025 e apresentou uma terceira geração na WWDC 2026, concentrando-se em geral em ganhos de qualidade e eficiência, em vez de aumentos drásticos de tamanho, o que reflete a preferência da empresa por privacidade e inferência no dispositivo em vez de enviar dados dos usuários a modelos de ponta hospedados na nuvem.
