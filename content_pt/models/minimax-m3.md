---
title: MiniMax M3
name: MiniMax M3
slug: minimax-m3
subtitle: Primeiro modelo de pesos abertos a combinar programação de ponta, contexto
  de 1 milhão de tokens e multimodalidade nativa
description: Primeiro modelo de pesos abertos a combinar programação de ponta, contexto
  de 1 milhão de tokens e multimodalidade nativa
company: minimax-ai
model_type: Multimodal
logo_url: ''
product_url: https://www.minimaxi.com/
price: Free
rank: 8
release_date: '2026-06-01'
param_count: 428B (23B active)
context_window_tokens: 1000000
modality:
- text
- image
- code
open_weight: true
license: Apache 2.0
input_price_usd_per_m: 0.3
output_price_usd_per_m: 1.2
api_available: true
lmarena_score: 1340
access_methods:
- API
- Self-hosted
runs_at_home: true
platforms:
- Hugging Face
- API
date: '2026-07-16'
tags:
- llm
- open-weight
- multimodal
- long-context
- coding
extra_model_types:
- Code
i18n_source: 'b89f089ecadf'
---
O MiniMax M3 é um modelo de mistura de especialistas com pesos abertos, lançado pela MiniMax em junho de 2026 e disponível no Hugging Face até 7 de junho. Ele tem cerca de 428 bilhões de parâmetros no total, dos quais aproximadamente 23 bilhões ficam ativos por token, distribuídos por 256 especialistas granulares. A MiniMax o apresenta como o primeiro modelo de pesos abertos a combinar programação de nível de ponta, janela de contexto de 1 milhão de tokens e entrada multimodal nativa de texto, imagens e vídeos. O laboratório informa resultados de 59% no SWE-Bench Pro e 66% no Terminal-Bench 2.1, benchmarks voltados a tarefas longas de programação e agentes, em vez de perguntas isoladas.

A arquitetura busca manter baixo o custo de inferência com contexto longo: segundo a MiniMax, o processamento por token com 1 milhão de tokens custa uma fração do valor da geração anterior, e tanto o prefill quanto a decodificação são várias vezes mais rápidos. O modelo é distribuído sob a licença Apache 2.0. Pela API da MiniMax, custa US$ 0,30 por milhão de tokens de entrada e US$ 1,20 por milhão de tokens de saída. A proposta é oferecer uma alternativa aberta e mais barata aos modelos fechados de ponta para desenvolvedores de agentes autônomos de programação e ferramentas que operam em grandes bases de código.
