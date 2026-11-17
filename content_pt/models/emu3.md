---
title: 'Emu3'
name: 'Emu3'
slug: 'emu3'
subtitle: 'Modelo de previsão do próximo token da BAAI que unifica geração e compreensão de texto, imagem e vídeo'
description: 'Modelo de previsão do próximo token da BAAI que unifica geração e compreensão de texto, imagem e vídeo'
company: 'baai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://baai-agents.github.io/Emu3/'
price: 'Free'
rank: 5
release_date: '2024-09-27'
param_count: '8B'
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, research]
extra_model_types: ['Image Generation']
i18n_source: '6fd97391d2f7'
---

O Emu3 é um modelo multimodal com pesos abertos da Beijing Academy of Artificial Intelligence (BAAI), lançado em setembro de 2024. Sua ideia central é tratar texto, imagens e vídeo como sequências de tokens discretos e treinar um único transformer para prever o próximo token nos três formatos, sem componentes separados de difusão ou no estilo CLIP. A BAAI publicou a versão de 8 bilhões de parâmetros nas variantes Chat e Gen, uma ajustada para compreensão de visão e linguagem e outra para geração. Apesar do design simplificado com um único objetivo, a BAAI afirmou que o Emu3 superou modelos abertos especializados da época, incluindo SDXL em geração de imagens e LLaVA-1.6 em compreensão visual e linguística. O projeto precede o Emu3.5, modelo maior da BAAI lançado no fim de 2025, que amplia a mesma abordagem de previsão do próximo token para 34 bilhões de parâmetros.