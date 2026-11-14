---
title: 'Flamingo'
name: 'Flamingo'
slug: 'flamingo'
subtitle: 'DeepMindの視覚言語モデル。少数ショットでのマルチモーダル推論の先駆け'
description: 'DeepMindの視覚言語モデル。少数ショットでのマルチモーダル推論の先駆け'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/tackling-multiple-tasks-with-a-single-visual-language-model/'
price: 'Paid'
rank: 6
release_date: '2022-04-29'
param_count: '80B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, vision, research]
---

Flamingoは、DeepMindが2022年4月に発表した視覚言語モデルです。画像、動画、テキストをまとめて扱い、ほんの数個の例を見せるだけで、それらについての自由形式の質問に答えられるように作られています。土台はDeepMindの700億パラメータの言語モデルChinchillaで、そこに視覚エンコーダーとクロスアテンション層を足し、視覚入力に応じてテキストを生成できるようにしました。全体では約800億パラメータになります。中心となる発想は、視覚言語タスクでの少数ショット学習です。新しいデータセットごとにファインチューニングする代わりに、プロンプトの中に少数の例を示せば、そこから一般化できます。GPT-3がテキストで見せたのと似た方法です。公開時には、キャプション生成、視覚的質問応答、視覚的対話を含む16の視覚言語ベンチマークで、それまでの少数ショット手法をすべて上回りました。DeepMindはFlamingoを製品や公開APIとしては出さず、研究用モデルのままでした。ただ、そのアーキテクチャは、OpenFlamingoのようなオープンな再実装や、Googleのその後のマルチモーダルモデルの設計に影響を与えました。
