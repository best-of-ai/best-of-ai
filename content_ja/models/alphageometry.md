---
title: 'AlphaGeometry'
name: 'AlphaGeometry'
slug: 'alphageometry'
subtitle: 'オリンピック級の幾何問題を解くDeepMindのニューロシンボリックシステム'
description: 'オリンピック級の幾何問題を解くDeepMindのニューロシンボリックシステム'
company: 'google-deepmind'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/'
price: 'Paid'
rank: 6
release_date: '2024-01-17'
param_count: 'Undisclosed'
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [reasoning, math, research]
i18n_source: '1dbe543ce262'
---

AlphaGeometryはGoogle DeepMindのニューロシンボリックシステムで、2024年1月にNatureで発表されました。国際数学オリンピック（IMO）の出場者に並ぶ水準で幾何の問題を解きます。合成した幾何の証明で学習した言語モデルと、従来型の記号的な演繹エンジンを組み合わせています。ニューラル側が新しい点や線といった有用な補助線を提案し、記号側が形式的な論理演繹で証明を仕上げます。2000年から2022年のIMOの幾何問題30問のベンチマークで25問を解き、金メダリストの平均に近く、従来の自動定理証明器を大きく上回りました。

DeepMindは、人間の手本をまったく使わずに生成した1億件の合成定理と証明で、言語モデルを学習させました。オリンピック級の幾何問題にラベル付きのデータが少ないためです。このプロジェクトは研究のみで製品にはなりませんでしたが、ニューラルモデルと記号ソルバーを組み合わせれば、どちらか一方に頼る手法より成績が上がることを示しました。1年後にDeepMindはAlphaGeometry2を発表し、過去25年のIMOの幾何問題全体で解答率を84パーセントに引き上げ、初めて金メダリストの平均を上回りました。
