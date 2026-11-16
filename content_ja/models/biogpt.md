---
title: 'BioGPT'
name: 'BioGPT'
slug: 'biogpt'
subtitle: '生物医学の文献で事前学習した、Microsoftの分野特化の生成モデル'
description: '生物医学の文献で事前学習した、Microsoftの分野特化の生成モデル'
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BioGPT'
price: 'Free'
rank: 5
release_date: '2022-09-24'
param_count: '347M (base), 1.5B (Large)'
context_window_tokens: 1024
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [healthcare, open-weight, legacy]
i18n_source: 'b08c07fb9738'
---

BioGPTは、Microsoft Researchが2022年10月に発表した言語モデルで、汎用モデルを後から適応させたものではなく、最初から生物医学のテキスト向けに作られています。GPT-2型のデコーダアーキテクチャで、約1,500万件のPubMedの要旨をゼロから学習しました。3億4,700万パラメータのベース版と、15億パラメータのBioGPT-Large版があります。ファインチューンではなく、最初から生物医学のテキストで学習しているので、生物医学の関係抽出、医学文献への質問応答、文書分類といったタスクで、従来の汎用言語モデルを上回りました。MicrosoftはMITライセンスで、両方のチェックポイントをHugging FaceとGitHubに公開しています。分野特化のモデルをゼロから学習しなくても生物医学のNLPツールを作れるため、研究グループがよく出発点にします。汎用の指示チューニング済みチャットモデルが広がる前のモデルで、その後更新されていません。現在は汎用のアシスタントではなく、限られた生物医学のテキストタスク向けの、軽量でセルフホストできる選択肢としてよく使われます。
