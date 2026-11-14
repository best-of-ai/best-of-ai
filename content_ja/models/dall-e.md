---
title: 'DALL-E'
name: 'DALL-E'
slug: 'dall-e'
subtitle: 'OpenAIが2021年に出した、最初のテキストから画像へのモデル'
description: 'OpenAIが2021年に出した、最初のテキストから画像へのモデル'
company: 'openai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://openai.com/index/dall-e/'
price: 'Paid'
rank: 5
release_date: '2021-01-05'
param_count: '12B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [image-generation, legacy]
i18n_source: '69880ba7eb3a'
---

DALL-EはOpenAIが2021年1月に発表した最初のテキストから画像へのモデルで、GPT-3を基にした120億パラメータの派生モデルです。テキストのキャプションから画像を生成するように学習されています。画像生成を系列予測の問題として扱う仕組みで、離散VAEが画像をトークンに変換し、自己回帰型のtransformerがテキストのプロンプトからそのトークンを予測します。できあがった画像は、あとからCLIPモデルで順位付けされます。インターネットから集めた約2億5000万組のテキストと画像のペアで学習しており、アボカドの形をした肘掛け椅子のように、それまで組み合わされたことのない概念の組み合わせでも、もっともらしい画像を作れました。DALL-Eは一般向けの製品としては公開されず、OpenAIは研究プレビューにとどめました。のちに拡散モデルベースのDALL-E 2に置き換えられ、DALL-E 2はより少ないパラメータ数で、より鮮明な画像を出しました。
