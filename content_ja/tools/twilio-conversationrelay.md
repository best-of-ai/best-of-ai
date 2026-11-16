---
title: 'Twilio ConversationRelay'
name: 'Twilio ConversationRelay'
subtitle: '任意の言語モデルを電話の通話につなぎ、音声エージェントにする'
slug: 'twilio-conversationrelay'
description: 'ConversationRelayでは、開発者が好きな言語モデルを使い、Twilioの電話通話の上で音声AIエージェントを作れます。音声からテキスト、テキストから音声へのストリーミングはTwilioが処理し、会話のロジックは自分のサーバーが動かします。'
website: 'https://www.twilio.com/en-us/ai/conversational-ai'
company: 'twilio'
logo_url: ''
category: 'ai-agents'
category_name: 'AIエージェント'
price: 'Paid'
featured: false
rank: 6
alternatives:
  - livekit
  - vapi
  - openai-realtime-api
  - bland-ai
  - retell-ai
date: '2026-11-05'
tags: [ai, assistant, automation, productivity, enterprise, agent]
i18n_source: '09fae406af0d'
---

ConversationRelayは、電話の通話とAIをつなぎます。Twilioの番号に着信があると、サービスが発信者の音声をリアルタイムでテキストに変換し、WebSocketで開発者のサーバーに流します。サーバーがテキストを返すと、Twilioが音声に変換するので、発信者には自然な応答が聞こえます。これで、任意の大規模言語モデルと自社の業務ロジックを組み込めます。

音声の面倒な部分はTwilioが管理します。発信者がエージェントの発話に割り込んだ場合の処理、複数の言語と音声プロバイダへの対応、通話の人間への転送（文字起こし付き）などです。単純なフロー向けのノーコードのStudioウィジェットもあり、HIPAAやPCIの選択肢を含め、規制のある業界向けのコンプライアンス対応もあります。レポート機能では、レイテンシとエージェントが苦戦する箇所が分かります。

ConversationRelayは使用量に応じた課金で、通常のTwilio音声の料金に上乗せされます。音声とモデルのプロバイダは、それぞれ別に料金がかかります。電話の会話ではレイテンシが非常に重要なので、設計とテストに手間がかかります。代替にはVapi、Retell AI、Bland AI、LiveKit、Amazon Connectがあります。Twilio ConversationRelayは、AIの電話エージェントを作る開発者に向いています。
