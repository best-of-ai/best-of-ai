---
title: 'ComfyUI'
name: 'ComfyUI'
subtitle: 'AIの画像と動画の生成向け、ノード型のビジュアルなワークフロー構築'
slug: 'comfyui'
description: 'ComfyUIは、画像、動画、音声の生成ワークフローを組む、オープンソースのノード型インターフェースです。モデル、プロンプト、サンプラー、制御のノードをつないでグラフにし、ワークフロー全体をファイルとして共有できます。'
website: 'https://github.com/comfyanonymous/ComfyUI'
company: 'github'
logo_url: ''
category: 'image-generation'
category_name: '画像生成'
price: 'Free'
featured: false
rank: 8
alternatives:
  - stable-diffusion
  - invokeai
  - civitai
  - krea-ai
  - leonardo-ai
  - flux
date: '2025-09-21'
tags: [image_generation, creative, text_to_image, visual, graphics, generative_ai, art, diffusion, prompting, open_source, customizable, image_based]
i18n_source: '0937aa929bc6'
---

ComfyUIは、パイプライン全体を見せることで、生成AIを細かく制御できます。プロンプト欄とボタンではなく、グラフを組み立てます。モデルを読み込み、プロンプトをエンコードし、サンプラーを設定し、誘導にLoRAやControlNetを足し、アップスケールして保存します。各ステップは、中を見てつなぎ直せるノードです。最初はStable Diffusion向けで、今はFLUXを含む多くの画像、動画、音声のモデルに対応しているので、新しいモデルはComfyUIで先に使えることが多いです。

ノード方式には実用上の利点があります。ワークフローは再現でき、JSONファイルとして保存するか、生成した画像へ埋め込めます。ほかの人がまったく同じ設定を読み込めます。大きなコミュニティが機能を足すカスタムノードを書き、利用者は商品写真、キャラクターの一貫性、動画のアニメーションなどの作業向けにワークフローを共有します。メモリ効率がよいので、それほど高性能でないGPUでも動き、ローカルへのインストールに加え、デスクトップアプリとホスト型のクラウドサービスもあります。

ComfyUIは無料のオープンソースです。習得のハードルは高く、カスタムノードと依存関係を動かし続けるには手間がかかります。Automatic1111とForgeはより簡単なインターフェースで、InvokeAIはより整ったもので、Midjourneyのようなホスト型のツールは設定が要りません。最大限の制御が欲しい人や、自動化したパイプラインを組みたい人の選択です。
