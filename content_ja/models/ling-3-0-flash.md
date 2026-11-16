---
title: 'Ling-3.0-Flash'
name: 'Ling-3.0-Flash'
slug: 'ling-3-0-flash'
subtitle: '本番環境のAIエージェント向けに作られた、効率的なオープンウェイト推論モデル'
description: '本番環境のAIエージェント向けに作られた、効率的なオープンウェイト推論モデル'
company: 'ant-group'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.antgroup.com'
price: 'Free'
rank: 6
release_date: '2026-07-23'
param_count: '124B (5.1B active)'
context_window_tokens: 262144
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.075
output_price_usd_per_m: 0.22
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'OpenRouter']
date: '2026-08-09'
tags: [llm, open-weight, reasoning, agentic, mixture-of-experts, efficiency]
extra_model_types: ['Code']
i18n_source: '368f5f371b66'
---
Ling-3.0-Flashは、Ant GroupのInclusionAI研究所が開発した、効率性重視のLingシリーズ最新モデルです。2026年7月23日に、本番環境のAIエージェント向けハイブリッド推論基盤モデルとして発表されました。総パラメータ数1,240億のMixture of Expertsモデルですが、トークンあたりの有効パラメータは約51億です。ネイティブでは256,000トークンのコンテキスト長を備え、最大100万トークンまで拡張できます。Antによると、推論、指示追従、長文コンテキストのベンチマークで、総パラメータ数が2〜3倍のモデルに匹敵または上回る性能です。クラスター単位の階層キャッシュ機構により、長い会話で最初のトークンが出るまでの時間を60〜80％短縮します。公式API料金は入力100万トークンあたり0.075ドル、出力100万トークンあたり0.22ドルです。Artificial Analysis Intelligence Indexで38以上のスコアを持つモデルの中でも最安級です。重みはMITライセンスでHugging Faceに公開されています。
