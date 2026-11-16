---
title: 'Emu'
name: 'Emu'
slug: 'emu'
subtitle: 'Meta AIの画像機能を支える、Metaの写実的なテキストから画像へのモデル'
description: 'Meta AIの画像機能を支える、Metaの写実的なテキストから画像へのモデル'
company: 'meta-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/emu-text-to-video-generation-image-editing-research/'
price: 'Paid'
rank: 6
release_date: '2023-09-27'
param_count: 'Undisclosed'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Chat UI]
runs_at_home: false
platforms: ['Meta AI', 'Instagram', 'WhatsApp']
date: '2026-07-16'
tags: [image-generation, legacy]
i18n_source: 'a6c0c0fec705'
---

Emuは、2023年9月の論文で説明されたMetaのテキストから画像へのモデルです。約11億組の画像とテキストのペアで事前学習した潜在拡散モデルで、その後、手作業で選んだ少数の高品質な画像でファインチューンしています。Metaはこの手法をクオリティチューニングと呼びました。このやり方によって、比較的標準的な拡散のアーキテクチャのまま、基盤のモデルをあまり変えずに、より安定して写実的で見栄えのよい出力が得られるようになりました。MetaはこれをFacebook Messenger、Instagram、WhatsAppにあるMeta AIのステッカーや画像作成の機能の裏にある画像生成器として使いました。EmuはEmu VideoやEmu Editなど、Metaのその後の研究プロジェクトのベースモデルにもなりました。Meta自身のアプリの外では、単体のAPIや製品としては提供されていません。
