---
title: 'NVIDIA CUDA'
name: 'NVIDIA CUDA'
subtitle: 'NVIDIAのGPUコンピューティングのプラットフォームとツールキット'
slug: 'nvidia-cuda'
description: 'CUDAは、NVIDIAのGPUで汎用のコードを動かすためのプラットフォームです。コンパイラ、ランタイム、cuDNNやcuBLASなどのライブラリを含み、主要なディープラーニングフレームワークのほぼすべてが依存しています。'
website: 'https://developer.nvidia.com/cuda-toolkit'
company: 'nvidia'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Free'
featured: false
rank: 10
alternatives:
  - amd-rocm
  - openvino
  - qualcomm-ai-hub
  - nvidia-nim
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, machine_learning, training]
i18n_source: '06f483092a94'
---

CUDAは、プログラマーがNVIDIAのグラフィックスプロセッサを、描画以外の用途に使えるようにするソフトウェア層です。カーネルと呼ばれる関数を、たいていC++かPythonで書くと、数千のGPUスレッドで同時に実行されます。大量の並列計算でできている処理に向いており、科学シミュレーション、動画処理、そして何よりニューラルネットワークがこれに当てはまります。このためCUDAは、現代のAIの学習と推論の土台になりました。

CUDAを使う人の多くは、直接は書きません。PyTorch、TensorFlow、JAXが、NVIDIAのライブラリを呼び出します。ニューラルネットワークの演算にはcuDNN、線形代数にはcuBLAS、GPU間の通信にはNCCLが使われます。TensorRTと関連ツールは、デプロイに向けてモデルを最適化します。これらのライブラリは長年チューニングされてきたため、CUDAで動くモデルは、他社のハードウェアで同じコードを動かすより、そのままで速いことがよくあります。このソフトウェア面のリードが、NVIDIAのGPUがAIのデータセンターを占めている大きな理由です。

CUDAは無料でダウンロードできますが、NVIDIAのハードウェアでしか動きません。これが主な批判点です。CUDAで書いたコードは、移植しなければAMDやIntelのGPUでは動かせず、多くの企業がこのロックインを避けようとしています。代替としてよく挙がるのは、AMDのROCm、OpenAIのTriton、SYCL、AppleのMetalですが、どれもCUDAがカバーする範囲の一部にとどまります。ほとんどの開発者にとっての実用的な助言は単純です。CUDAを処理してくれるフレームワークを使い、プロファイリングで速度がもっと必要だと分かったときだけ、カーネルを書く段階に踏み込むことです。
