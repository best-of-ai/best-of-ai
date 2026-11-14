---
title: 'Hunyuan3D'
name: 'Hunyuan3D'
slug: 'hunyuan3d'
subtitle: 'テキストや画像から3Dアセットを生成するTencentのオープンウェイトモデル'
description: 'テキストや画像から3Dアセットを生成するTencentのオープンウェイトモデル'
company: 'tencent'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/Tencent/Hunyuan3D-2'
price: 'Free'
rank: 5
release_date: '2025-01-21'
param_count: '2.6B (shape) + 1.3B (texture)'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [3d-generation, open-weight, api]
i18n_source: '07d08c139e5b'
---
Hunyuan3Dはテキストプロンプトや参照画像から3Dアセットを生成するTencentのシステムで、広く使われた2.0版は2025年1月に公開されました。処理を2つのモデルに分けています。まず26億パラメータの形状生成モデルがフローベースの拡散トランスフォーマーを使い、テクスチャのないメッシュを作成します。次に13億パラメータのテクスチャモデルが、そのメッシュに高解像度のPBR素材を適用します。2段階に分けることで、形状モデルはジオメトリに、テクスチャモデルは色、光の反射、表面の細部に集中できます。重みはHugging FaceとGitHubでHunyuanライセンスのもと公開され、ゲームスタジオや3Dアーティストは有料APIを使わずローカルで生成できます。TripoSRやStability AIのTripoSGなど、オープンまたは一部公開の3D生成モデルと競合します。後続の2.1版と2.5版では、テクスチャの忠実度と形状の細部がさらに向上しました。
