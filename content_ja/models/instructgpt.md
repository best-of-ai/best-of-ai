---
title: 'InstructGPT'
name: 'InstructGPT'
slug: 'instructgpt'
subtitle: '大規模なRLHFによる指示調整を初めて導入したOpenAIの2022年モデル'
description: '大規模なRLHFによる指示調整を初めて導入したOpenAIの2022年モデル'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/instruction-following/'
price: 'Paid'
rank: 5
release_date: '2022-01-27'
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
tags: [llm, foundation-model, legacy, rlhf]
i18n_source: 'e5b0714c6a82'
---
InstructGPTはOpenAIがGPT-3をファインチューニングしたモデルで、Ouyangらの論文「Training Language Models to Follow Instructions with Human Feedback」で説明されています。OpenAIは2022年1月に発表し、同年3月に論文全文をarXivで公開しました。開発は3段階で進みました。人間の評価者が書いた望ましい回答例でGPT-3を調整し、複数の出力に対する人間の順位付けを集め、その評価から報酬モデルを訓練して、強化学習による追加調整を導きました。GPT-3のコンテキスト長2,048トークンを引き継ぐ1.3B、6B、175Bの3サイズを訓練しました。

論文でよく引用されるのは、パラメータ数が100分の1しかない1.3B版の出力を、人間の評価者が元の175B GPT-3より好んだ結果です。人が望む応答を作るには規模を大きくするだけでなく、人間のフィードバックによる調整が重要だと示し、一般的な能力をあまり損なわずに有害な出力や誤りを減らしました。ここでOpenAIが開発した人間のフィードバックによる強化学習（RLHF）は、生の言語モデルを実用的なアシスタントに変える標準的手法となり、1年足らずでChatGPTにつながりました。
