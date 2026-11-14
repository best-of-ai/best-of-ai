---
title: 'AMD ROCm'
name: 'AMD ROCm'
subtitle: 'AI開発とGPU計算のためのオープンなソフトウェアプラットフォーム'
slug: 'amd-rocm'
description: 'AMD ROCmは、AMDのGPU上でAIと高性能計算を行うためのオープンなソフトウェアプラットフォームです。ドライバ、コンパイラ、ライブラリ、フレームワーク対応を備え、開発者は機械学習モデルを学習し、実行できます。'
website: 'https://rocm.docs.amd.com/'
company: 'amd'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Free'
featured: false
rank: 5
alternatives:
  - nvidia-cuda
  - openvino
  - qualcomm-ai-hub
date: '2026-07-17'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, machine_learning, training, model_based]
i18n_source: 'b6be5b2911d8'
---

ROCmは、NVIDIAのCUDAに対するAMDの答えです。プログラムがAMDのグラフィックスプロセッサを汎用計算に使うためのソフトウェア群で、ドライバ、コンパイラのツールチェーン、数学と通信のライブラリ、デバッグとプロファイリングのツールを含みます。その多くはオープンソースです。

AIの作業で中心になるのは、フレームワークへの対応です。PyTorch、TensorFlow、JAXなどがROCm上で動き、vLLMのような推論ツールや多くのモデルライブラリにAMD向けのビルドがあります。開発者は、CUDAに似たプログラミング層であるHIPを使ってCUDAのコードを移植できます。大規模なクラウドとスーパーコンピュータの導入では、AMD InstinctアクセラレータとROCmが使われています。

ROCmは無料です。成熟度とエコシステムの支援では、これまでCUDAに後れを取ってきたため、特定のGPUやライブラリとの互換性はばらつき、確認が必要ですが、差は縮まっています。代替にはNVIDIA CUDA、Intel oneAPI、Mac向けのApple Metal、Vulkanベースの計算があります。ROCmは、AIにAMDのハードウェアを使う開発者と組織に向いています。
