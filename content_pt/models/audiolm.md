---
title: 'AudioLM'
name: 'AudioLM'
slug: 'audiolm'
subtitle: "Framework do Google para gerar fala realista e continuações de áudio"
description: "Framework do Google para gerar fala realista e continuações de áudio"
company: 'google-deepmind'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://google-research.github.io/seanet/audiolm/examples/'
price: 'Paid'
rank: 5
release_date: '2022-09-07'
param_count: 'Undisclosed'
modality: [audio]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [audio, research, legacy]
i18n_source: '944df39235b8'
---

AudioLM é uma estrutura de pesquisa publicada pelo Google em setembro de 2022 que trata a geração de áudio como um problema de modelagem de linguagem sobre tokens discretos de áudio, em vez das abordagens usuais de regressão de espectrogramas ou formas de onda. Ela combina duas representações: tokens semânticos do w2v-BERT, um modelo de fala auto-supervisionado que captura estruturas de longo alcance, e tokens acústicos do codec neural SoundStream, que preservam detalhes finos do áudio para síntese de alta qualidade. Treinado somente com áudio bruto, sem transcrições nem anotações de texto, pode continuar alguns segundos de fala ou música de piano de forma coerente por dezenas de segundos, algo com que métodos anteriores de geração de áudio tinham dificuldade. O Google nunca o lançou como produto; ele permaneceu como artigo de pesquisa e página de demonstração, e o Google DeepMind usou sua abordagem baseada em tokens como componente de trabalhos posteriores, como MusicLM e partes do Lyria.
