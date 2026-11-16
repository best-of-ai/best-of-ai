---
title: 'Whisper'
name: 'Whisper'
subtitle: 'OpenAIのオープンソースの音声認識モデル'
slug: 'whisper'
description: 'Whisperは、OpenAIのオープンソースの音声認識モデルです。多くの言語の音声を文字起こしし、音声を英語に翻訳でき、アクセントや背景ノイズにも強いです。自分で動かすことも、OpenAIのAPI経由で使うこともできます。'
website: 'https://openai.com/research/whisper'
company: 'openai'
logo_url: ''
category: 'transcription'
category_name: '文字起こし'
price: 'Free'
featured: false
rank: 9
alternatives:
  - assemblyai
  - deepgram
  - speechmatics
  - gladia
  - azure-ai-speech
date: '2026-07-17'
tags: [transcription, speech_to_text, audio, text, conversion, captions, subtitles, accuracy, real_time, open_source, free_tier, voice_enabled]
i18n_source: 'bb082e1aec7b'
---

Whisperは、多言語の非常に大規模で多様な音声データで学習した音声認識モデルです。この学習のおかげで頑健性が高く、アクセント、背景ノイズ、専門用語への対応が従来の多くのシステムより優れ、数十の言語で動きます。話されている言語を自動で判定し、句読点を加え、他の言語の音声を英語のテキストに翻訳することもできます。

モデルはオープンソースで公開され、ノートPCで動く小型のものから、高性能なGPUが必要な大型のものまで、複数のサイズがあります。この公開をきっかけに、whisper.cppやfaster-whisperといった高速版、タイムスタンプや話者ラベルを加えるツール、裏でWhisperを使う文字起こし、字幕、音声入力のアプリなど、幅広いエコシステムが生まれました。自分でホストしたくない人向けに、OpenAIはAPIとしても提供しています。

Whisperは自分で動かすなら無料で、APIは音声の分数で課金されます。弱点も知られています。無音やノイズの多い区間でテキストを作り出すことがあり、医療や法律の用途では懸念になります。また、基本モデルは話者の区別をせず、追加のツールなしではリアルタイムでも動きません。ライブ字幕や話者ごとに分けた文字起こしには、AssemblyAI、Deepgram、Google Speech-to-Textのようなサービスのほうが合うかもしれません。費用をかけずにプライベートなローカル文字起こしをしたいなら、今でもWhisperが第一候補です。
