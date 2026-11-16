---
title: 'Falcon 3'
name: 'Falcon 3'
slug: 'falcon-3'
subtitle: 'TIIの効率重視の小型オープンウェイトモデルファミリー'
description: 'TIIの効率重視の小型オープンウェイトモデルファミリー'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 4
release_date: '2024-12-17'
param_count: '10B'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Falcon License'
api_available: false
mmlu_score: 73.1
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
---

Falcon 3は、アブダビのTechnology Innovation Instituteが2024年12月に公開したオープンウェイトの言語モデルファミリーです。1B、3B、7B、10Bパラメータの4サイズがあり、それぞれにベース版とinstruct版があります。TIIはGPU1枚やノートPCといった控えめなハードウェアで動くように作りつつ、大きなオープンモデルとも競えることを狙いました。10Bモデルは公開時点で、13B未満のモデルを対象にしたHugging Faceのランキングで首位に立ちました。MMLUは73.1、GSM8Kは83.1で、同程度のLlamaやGemmaの派生モデルを上回っています。ほとんどのサイズが32Kトークンのコンテキスト長に対応します(1Bモデルは8Kまで)。重みはHugging Faceで、TII独自のFalcon Licenseのもと、セルフホスト用に配布されています。Falcon 3は、先行するFalconとFalcon Mambaに続くもので、フロンティア級のパラメータ数を追うのをやめ、小さく安く動くモデルへ移ったTIIの方針を表しています。
