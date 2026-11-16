---
title: 'GPT-3'
name: 'GPT-3'
slug: 'gpt-3'
subtitle: '大規模なfew-shot学習が可能であることを初めて示した2020年のモデル'
description: '大規模なfew-shot学習が可能であることを初めて示した2020年のモデル'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/gpt-3-apps/'
price: 'Paid'
rank: 6
release_date: '2020-06-11'
param_count: '175B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [API]
runs_at_home: false
platforms: ['API']
date: '2026-07-16'
tags: [llm, foundation-model, legacy]
---

GPT-3は、OpenAIが2020年5月の論文「Language Models are Few-Shot Learners」で説明し、2020年6月11日にベータ版APIで公開した言語モデルです。パラメータ数は1750億で、GPT-2より桁が1つ大きくなりました。主な成果は、1つのモデルが、プロンプトの中にほんの数個の例を置くだけで、翻訳、算術、質問応答などのタスクを、タスク専用のファインチューンなしでこなせたことです。コンテキスト長は、のちの基準では小さく、約2,048トークンでした。

論文のfew-shot学習の結果があったから、GPT-3は単にGPT-2より大きいだけのモデルではなく、転換点になりました。アーキテクチャを変えず、規模だけで質的に新しい能力が生まれることを示し、研究機関のあいだで、より大きなモデルを学習させる競争の引き金になりました。GPT-3自体はAPIのみの提供で、重みは公開されませんでした。OpenAIは最終的に、元のモデルを終了して、指示チューニングした後継モデルに切り替えました。
