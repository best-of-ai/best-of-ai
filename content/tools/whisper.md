---
title: 'Whisper'
name: 'Whisper'
slug: 'whisper'
subtitle: 'OpenAI''s open-source speech recognition model'
description: 'Whisper is OpenAI''s open-source automatic speech recognition system, trained on 680,000 hours of multilingual audio from the web. It transcribes and translates speech in 99 languages with near-human accuracy, even handling accents, background noise, and technical vocabulary robustly. Developers embed Whisper in everything from voice assistants to interview transcription tools, and it underpins many commercial transcription services.'
website: 'https://openai.com/research/whisper'
logo_url: ''
category: 'transcription'
category_name: 'Transcription'
price: 'Free'
featured: false
rank: 9
date: '2025-01-01'
tags: [transcription, speech_to_text, audio, text, conversion, captions, subtitles, accuracy, real_time, open_source, voice_enabled, training]
---

Whisper was trained on 680,000 hours of diverse audio from the internet — lectures, podcasts, interviews, phone calls, TV broadcasts — which gives it robustness to accents, background noise, and domain-specific vocabulary that earlier speech recognition models lacked. The result is accuracy that holds up in conditions where other models degrade: a doctor speaking quickly with medical terminology, a non-native English speaker with a strong accent, or audio recorded on a laptop microphone in a noisy room.

The open-source model comes in five sizes (tiny, base, small, medium, large) that trade accuracy for speed. The tiny model runs on a CPU and produces acceptable quality for clear speech; the large model requires a GPU and produces near-professional transcription quality. Developers download Whisper from its GitHub repository and run it locally, which keeps audio private — nothing is sent to an API. For applications where audio data can't leave the organisation, local Whisper is often the practical choice.

Many commercial transcription services use Whisper under the hood — AssemblyAI, Otter.ai, and others have built their pipelines on top of Whisper models. OpenAI also exposes Whisper through its API at $0.006 per minute of audio, which gives cloud access without managing the model yourself. Developers building features like podcast transcription, accessibility tools (captions for recorded content), interview analysis, and language-learning applications use Whisper because its accuracy across languages and audio conditions is genuinely hard to replicate with other freely available models.