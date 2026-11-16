---
title: 'Emu Video'
name: 'Emu Video'
slug: 'emu-video'
subtitle: 'MetaのEmu画像生成モデルを土台にした、テキストから動画へのモデル'
description: 'MetaのEmu画像生成モデルを土台にした、テキストから動画へのモデル'
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

Emu VideoはMetaが2023年11月に発表した、テキストから動画を生成する研究モデルで、MetaのEmu画像生成モデルの上に作られています。テキストのプロンプトからいきなり動画を生成するのではなく、作業を2段階に分けます。まずEmuを使ってプロンプトから静止画を生成し、次に、テキストとその画像の両方を条件にして動画を生成します。Metaによると、この分割した方式のおかげで、GoogleのImagen VideoやMeta自身のMake-A-Videoのような以前のシステムが頼っていた、別々のモデルを何段も重ねるカスケードが不要になりました。それでいて、より高解像度の出力が得られます。人間による好みの評価では、評価者の大多数が、Imagen VideoやMake-A-Videoよりも、Emu Videoのクリップを選んだとMetaは述べています。公開されたのは研究論文とデモで、一般向けの製品ではありません。その技術は、単体のモデルとしてではなく、のちのMetaの動画機能に生かされました。
