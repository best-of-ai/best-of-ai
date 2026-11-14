---
title: 'Amazon Textract'
name: 'Amazon Textract'
subtitle: 'スキャンした文書からテキスト、表、フォームを取り出すAWSのサービス'
slug: 'amazon-textract'
description: 'Amazon Textractは、スキャンした文書とPDFからテキスト、表、フォームの項目を取り出すAWSのサービスです。構造を読み取る点で基本的なOCRを超え、身分証、請求書、文書への質問向けの機能も含みます。'
website: 'https://aws.amazon.com/textract/'
company: 'amazon'
logo_url: ''
category: 'document-ai'
category_name: 'ドキュメントAI'
price: 'Paid'
featured: false
rank: 7
alternatives:
  - google-document-ai
  - azure-ai-document-intelligence
  - abbyy
  - nanonets
  - docsumo
  - reducto
date: '2026-11-05'
tags: [document_ai, pdf, productivity, extraction, documents, ocr, summarization, document_processing, parsing, voice_enabled]
i18n_source: '41f5cac62ceb'
---

Textractは、文書の画像を構造化データに変えます。開発者がスキャンしたファイルやPDFを送ると、サービスは見つけたテキストとその配置を返します。表を識別して行と列を保ち、氏名欄とその値のようなフォームのキーと値の組を検出し、手書きも認識します。文字の塊を順不同で返すだけの単純なテキスト認識より、はるかに使いやすいです。

専用の機能は、よくある文書を対象にします。Analyze IDはパスポートと運転免許証を読み、Analyze Expenseは請求書とレシートから明細と合計を取り出し、融資向けの機能は住宅ローンの文書を処理します。Queriesでは、請求書の合計はいくらか、といった質問を文書に投げて答えを得られます。結果はComprehend、Bedrock、Step Functionsなどの他のAWSサービスと連携し、さらに分析できます。

Textractの料金はページ単位で、機能によって単価が異なり、最初の数か月には無料枠があります。きれいな文書では精度は良いですが、スキャンが悪い、レイアウトが珍しい、手書き、といった場合は下がることがあります。機密の文書では、セキュリティの設定に注意が必要です。代替にはGoogle Document AI、Azure Document Intelligence、ABBYY、そして無料だが構造の扱いでは劣るTesseractなどのオープンソースのツールがあります。Textractは、フォームと請求書を処理するAWS上のチームに向いています。
