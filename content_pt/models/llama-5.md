---
title: 'Llama 5'
name: 'Llama 5'
slug: 'llama-5'
subtitle: "Próximo modelo multimodal principal de pesos abertos da Meta, criado para dispositivos e centros de dados"
description: "Próximo modelo multimodal principal de pesos abertos da Meta, criado para dispositivos e centros de dados"
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 9
release_date: '2026-07-14'
param_count: '520B (24B active)'
context_window_tokens: 2000000
modality: [text, image, audio]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 89.5
humaneval_score: 90.0
lmarena_score: 1381
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock', 'Azure AI Foundry']
date: '2026-07-19'
tags: [llm, open-weight, multimodal, self-hosted, mixture-of-experts]
i18n_source: '47cdfc96510e'
---

Llama 5 é a continuação da linha Llama 4 do ano anterior pela Meta, novamente lançado como modelo de mistura de especialistas, agora ampliado para 520 bilhões de parâmetros totais e 24 bilhões ativos por token. O maior salto é a janela de contexto de 2 milhões de tokens, o dobro do oferecido pelo Llama 4 Maverick, que a Meta promove para tarefas como ingerir bases de código completas ou transcrições longas de vídeo em uma única passagem. Ele processa nativamente entradas de texto, imagem e áudio, em vez de acrescentar codificadores a uma base somente de texto, e a Meta afirma que supera por pequena margem Gemini 3.5 Pro e GPT-5.6 em vários benchmarks abertos, mantendo a eficiência graças ao roteamento esparso de especialistas.

Como nos lançamentos Llama anteriores, os pesos são abertos sob a Llama 4 Community License e estão disponíveis imediatamente no Hugging Face; parceiros de hospedagem como Together AI, AWS Bedrock e Azure AI Foundry oferecem inferência gerenciada a equipes que não querem executá-lo. A Meta continua sem conceder direitos comerciais completos a empresas acima de determinado limite de usuários, a mesma exceção aplicada desde o Llama 2.
