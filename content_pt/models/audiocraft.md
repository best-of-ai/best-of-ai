---
title: 'AudioCraft'
name: 'AudioCraft'
slug: 'audiocraft'
subtitle: "Framework de código aberto da Meta para geração de música e efeitos sonoros"
description: "Framework de código aberto da Meta para geração de música e efeitos sonoros"
company: 'meta-ai'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/audiocraft-musicgen-audiogen-encodec-generative-ai-audio/'
price: 'Free'
rank: 6
release_date: '2023-08-02'
param_count: '300M-3.3B (MusicGen), 1.5B (AudioGen)'
modality: [audio, text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['GitHub']
date: '2026-07-16'
tags: [audio, open-weight, music-generation]
i18n_source: '0ed2f655dea3'
---

AudioCraft é uma biblioteca de código que a Meta lançou em agosto de 2023, reunindo três modelos de áudio generativo: MusicGen, para gerar música a partir de texto; AudioGen, para efeitos sonoros ambientais; e EnCodec, o codec neural de áudio que ambos usam para tokenizar formas de onda. O MusicGen tem vários tamanhos (300M, 1,5B e 3,3B parâmetros), com variantes que também podem seguir uma melodia junto com um comando de texto, enquanto o AudioGen é oferecido como modelo de 1,5B parâmetros treinado com efeitos sonoros, não música. A Meta publicou o código e os pesos sob a licença MIT, fazendo do AudioCraft um dos primeiros conjuntos de ferramentas totalmente abertos para geração de áudio a partir de texto, em contraste com sistemas fechados de empresas como o Google. As versões menores rodam em uma única GPU de consumo, e a biblioteca se tornou uma base comum para projetos de geração musical de código aberto e pesquisas sobre síntese de áudio controlável.
