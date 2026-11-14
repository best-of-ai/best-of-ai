---
title: 'Megatron-Turing NLG'
name: 'Megatron-Turing NLG'
slug: 'megatron-turing-nlg'
subtitle: 'NVIDIAとMicrosoftの当時最大級の530B高密度LLM研究モデル'
description: 'NVIDIAとMicrosoftの当時最大級の530B高密度LLM研究モデル'
company: 'nvidia'
model_type: 'Language'
logo_url: ''
product_url: 'https://developer.nvidia.com/megatron-turing-natural-language-generation'
price: 'Paid'
rank: 5
release_date: '2021-10-11'
param_count: '530B'
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, research, legacy]
extra_model_types: ['Reasoning']
i18n_source: '06b0502910e0'
---
Megatron-Turing NLGはNVIDIAとMicrosoftが共同学習し2021年10月に発表した5300億パラメータの高密度Transformerです。当時、混合エキスパートではない単一構成の言語モデルとして最大でした。数百基のA100 GPU上でNVIDIA Megatron-LMのテンソル並列化とMicrosoft DeepSpeedのパイプライン並列化・ZeROオプティマイザーを組み合わせました。105層で、ウェブ文章、書籍、選定データからなる2,700億トークンで学習しました。

混合エキスパートが大規模化の現実的な道筋となる前に、高密度モデルと分散学習ソフトの限界を示す研究デモでした。文章補完、読解、推論でGPT-3やTuring-NLGを上回る結果が公表されましたが、製品やAPIとして一般公開されませんでした。
