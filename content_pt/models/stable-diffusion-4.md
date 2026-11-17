---
title: Stable Diffusion 4
name: Stable Diffusion 4
slug: stable-diffusion-4
subtitle: Próximo modelo de difusão de pesos abertos da Stability AI para geração
  de imagens a partir de texto
description: Próximo modelo de difusão de pesos abertos da Stability AI para geração
  de imagens a partir de texto
company: stability-ai
model_type: Image Generation
logo_url: ''
product_url: https://stability.ai/
price: Free
rank: 7
release_date: '2026-07-15'
param_count: 12B
modality:
- text
- image
open_weight: true
license: Stability AI Community License
api_available: true
access_methods:
- Self-hosted
- API
runs_at_home: true
platforms:
- Hugging Face
- Stability API
date: '2026-07-19'
tags:
- image-generation
- open-weight
- text-to-image
- diffusion
- self-hosted
i18n_source: '14d55cb2be7c'
---
O Stable Diffusion 4 é a primeira grande atualização da linha da Stability AI desde o SD 3.5, no fim de 2024. O modelo cresceu para 12 bilhões de parâmetros e aprimorou a aderência aos prompts e a renderização de texto dentro das imagens, dois pontos fracos de longa data em comparação com concorrentes fechados, como Midjourney e Imagen. Ele é distribuído sob a mesma Stability AI Community License do SD 3.5, gratuitamente para pessoas físicas e pequenas empresas; acima de um limite de receita, é necessária uma licença paga.

Como de costume, os pesos estão disponíveis no Hugging Face, e versões quantizadas funcionam em uma única GPU de consumo. A Stability também oferece inferência hospedada por meio de sua própria API para equipes que preferem não gerenciar a infraestrutura. O SD4 chega em um momento de forte pressão sobre a Stability, diante do FLUX e de outros modelos abertos de imagem que reduziram sua vantagem. O lançamento aposta bastante no ecossistema comunitário de fine-tuning — LoRAs, ControlNets e checkpoints personalizados — que manteve o Stable Diffusion como escolha padrão para geração de imagens com pesos abertos, apesar da concorrência mais acirrada.
