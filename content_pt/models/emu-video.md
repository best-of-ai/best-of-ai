---
title: 'Emu Video'
name: 'Emu Video'
slug: 'emu-video'
subtitle: 'Modelo de texto para vídeo da Meta, desenvolvido sobre o gerador de imagens Emu'
description: 'Modelo de texto para vídeo da Meta, desenvolvido sobre o gerador de imagens Emu'
company: 'meta-ai'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/emu-text-to-video-generation-image-editing-research/'
price: 'Paid'
rank: 5
release_date: '2023-11-16'
param_count: 'Undisclosed'
modality: [text, video]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [video-generation, research, legacy]
i18n_source: 'd734ff203780'
---

O Emu Video é um modelo de pesquisa de texto para vídeo apresentado pela Meta em novembro de 2023, desenvolvido sobre o gerador de imagens Emu da própria empresa. Em vez de gerar vídeo diretamente a partir de um prompt em uma única etapa, divide o processo em duas: primeiro, usa o Emu para criar uma imagem estática a partir do prompt; depois, gera um vídeo condicionado pelo texto e pela imagem. A Meta relatou que essa abordagem dispensava a cascata profunda de modelos separados usada por sistemas anteriores, como Imagen Video do Google e Make-A-Video da própria Meta, e ainda produzia resultados em maior resolução. Em avaliações de preferência humana, a Meta afirmou que avaliadores preferiram a maioria dos clipes do Emu Video aos do Imagen Video e Make-A-Video. Foi lançado como artigo de pesquisa e demonstração, não como produto público; suas técnicas alimentaram recursos de vídeo posteriores da Meta, mas não foram publicadas como modelo independente.