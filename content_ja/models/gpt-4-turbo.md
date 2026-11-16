---
title: 'GPT-4 Turbo'
name: 'GPT-4 Turbo'
slug: 'gpt-4-turbo'
subtitle: 'コンテキスト長を伸ばし、GPT-4より高速・低価格になった後継モデル'
description: 'コンテキスト長を伸ばし、GPT-4より高速・低価格になった後継モデル'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/new-models-and-developer-products-announced-at-devday/'
price: 'Paid'
rank: 6
release_date: '2023-11-06'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 10
output_price_usd_per_m: 30
api_available: true
mmlu_score: 86.5
humaneval_score: 87.1
lmarena_score: 1250
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['ChatGPT', 'Azure OpenAI', 'API']
date: '2026-07-16'
tags: [llm, foundation-model, api]
extra_model_types: ['Code']
i18n_source: 'dfca7bbe4eb9'
---
GPT-4 Turboは、OpenAIが2023年11月に発表したGPT-4の更新版です。同社初の開発者会議で発表されました。基本的な性能水準はGPT-4と同じですが、コンテキスト長を128,000トークンに拡張し、知識の基準日を2023年4月に更新しました。料金も入力100万トークンあたり10ドル、出力100万トークンあたり30ドルと、初代GPT-4より大幅に下がりました。MMLUで86.5％、HumanEvalで87.1％を記録し、テキストと同じリクエストで画像を送れる視覚入力にも対応しました。

コンテキスト長の拡張には実用上の注意点もありました。第三者のテストでは、約32,000トークンを超えると情報への注意力が目立って低下し、密度の高い長文書では128Kの全体を活用しにくいことがわかりました。それでもGPT-4 Turboは2024年の大半にわたり、API開発者向けの標準的なGPT-4クラスモデルでした。OpenAI、Azure OpenAI、ChatGPTから利用できましたが、同年後半にGPT-4oが推奨モデルに置き換わりました。
