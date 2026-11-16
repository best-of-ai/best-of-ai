---
title: 'Whisper'
name: 'Whisper'
subtitle: "OpenAI's open-source speech-to-text model"
slug: 'whisper'
description: 'Whisper is OpenAI''s open-source speech recognition model. It transcribes audio in many languages, translates speech into English, and handles accents and background noise well. You can run it yourself or use it through OpenAI''s API.'
website: 'https://openai.com/research/whisper'
company: 'openai'
logo_url: ''
category: 'transcription'
category_name: 'Transcription'
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
---

Whisper is a speech-to-text model trained on a very large and varied collection of multilingual audio. That training made it unusually robust: it copes with accents, background noise, and technical vocabulary better than many earlier systems, and it works across dozens of languages. It also detects the spoken language automatically, adds punctuation, and can translate speech from other languages into English text.

The model is released as open source with several sizes, from small ones that run on a laptop to large ones that need a good GPU. That openness led to a wide ecosystem: faster versions such as whisper.cpp and faster-whisper, tools that add timestamps and speaker labels, and many apps for transcription, subtitles, and dictation that use it behind the scenes. OpenAI also offers it through its API for people who do not want to host it.

Whisper is free to run yourself, and the API is billed by the minute of audio. It has known weaknesses. It can invent text during silence or noisy sections, which is a concern for medical and legal work, and the base model does not label who is speaking or run in real time without extra tools. For live captions or speaker-separated transcripts, services like AssemblyAI, Deepgram, or Google Speech-to-Text may fit better. For private, local transcription at no cost, Whisper remains a first choice.
