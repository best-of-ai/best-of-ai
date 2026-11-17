---
title: 'Falcon 7B'
name: 'Falcon 7B'
slug: 'falcon-7b'
subtitle: "Categoria compacta Falcon do TII, que ajudou a popularizar a versão original"
description: "Categoria compacta Falcon do TII, que ajudou a popularizar a versão original"
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 5
release_date: '2023-05-25'
param_count: '7B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, legacy]
i18n_source: '61f475ea6988'
---

O Falcon 7B é o modelo menor da versão original do Falcon do TII. Foi treinado no mesmo conjunto RefinedWeb do Falcon 40B, mas dimensionado para implantação mais barata em uma única GPU. O TII o treinou durante cerca de duas semanas no início de 2023 e o publicou sob a licença permissiva Apache 2.0, que permite aos desenvolvedores usá-lo, modificá-lo e implantá-lo comercialmente sem royalties. Essa escolha de licença chamou atenção na época, pois muitos modelos abertos comparáveis restringiam o uso à pesquisa. O Falcon 7B compartilha a arquitetura transformer apenas decodificadora do modelo 40B, com atenção multiquery, mas tem contexto de 2.048 tokens e exige menos computação, tornando-se uma opção comum para experimentos de ajuste fino e uso em dispositivos em 2023 e no início de 2024. Desde então, o TII avançou para as famílias Falcon 3 e Falcon Mamba, enquanto o Falcon 7B permanece como modelo legado amplamente replicado no Hugging Face.
