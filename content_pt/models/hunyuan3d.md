---
title: 'Hunyuan3D'
name: 'Hunyuan3D'
slug: 'hunyuan3d'
subtitle: 'Hunyuan3D é o sistema aberto da Tencent para transformar comandos de texto ou imagens de referência em recursos 3D, com a versão 2.0, amplamente utilizada, publicada em janeiro de 2025.'
description: 'Hunyuan3D é o sistema aberto da Tencent para transformar comandos de texto ou imagens de referência em recursos 3D, com a versão 2.0, amplamente utilizada, publicada em janeiro de 2025.'
company: 'tencent'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/Tencent/Hunyuan3D-2'
price: 'Free'
rank: 5
release_date: '2025-01-21'
param_count: '2.6B (shape) + 1.3B (texture)'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [3d-generation, open-weight, api]
i18n_source: '07d08c139e5b'
---

Hunyuan3D é o sistema aberto da Tencent para transformar comandos de texto ou imagens de referência em recursos 3D, com a versão 2.0, amplamente utilizada, publicada em janeiro de 2025. O trabalho é dividido entre dois modelos: um gerador de formas de 2,6B parâmetros, baseado em um transformer de difusão com fluxo, que produz uma malha sem textura, e um modelo de texturas de 1,3B parâmetros, que depois aplica materiais PBR de alta resolução à malha. Essa divisão em duas etapas permite especializar cada componente: o modelo de formas se concentra apenas na geometria, enquanto o de texturas cuida da cor, da resposta à iluminação e dos detalhes da superfície. A Tencent publicou os pesos no Hugging Face e no GitHub sob sua licença Hunyuan, oferecendo a estúdios de jogos e artistas 3D uma forma de gerar recursos localmente, sem API paga. O modelo concorre com outros geradores 3D abertos e semiabertos, como TripoSR e TripoSG da Stability AI. Versões posteriores do Hunyuan3D (2.1 e 2.5) avançaram ainda mais na fidelidade das texturas e nos detalhes geométricos.
