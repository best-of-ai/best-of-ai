---
title: 'Deepgram'
name: 'Deepgram'
slug: 'deepgram'
subtitle: 'Real-time speech recognition API built for production'
description: 'Deepgram is a speech recognition platform engineered for high-volume, low-latency production use cases, offering real-time and batch transcription through a simple API. Its Nova models rank among the most accurate available and its infrastructure delivers transcripts in under 300ms for live audio streams. Call centre platforms, meeting tools, and voice AI products use Deepgram as the transcription layer behind their services.'
website: 'https://deepgram.com'
logo_url: ''
category: 'transcription'
category_name: 'Transcription'
price: 'Paid'
featured: false
rank: 8
date: '2025-01-01'
tags: [transcription, speech_to_text, audio, text, conversion, captions, subtitles, accuracy, real_time, api_available, voice_enabled, model_based]
---

Deepgram is built for applications where transcription is a production dependency rather than an occasional feature. Its Nova-2 model delivers word error rates that benchmark favourably against Google, AWS, and Azure speech services, at latency under 300 milliseconds for live audio streams. This matters for applications like real-time meeting transcription, live captioning, voice AI, and conversational agents where a few seconds of processing delay breaks the product experience.

The API design is straightforward: send audio via WebSocket for streaming or via POST request for batch transcription, receive JSON with word-level timestamps, confidence scores, speaker labels, and punctuation. Additional features include topic detection, sentiment analysis, and intent recognition that can be applied on the transcription pass — useful for call analytics platforms that need to categorise conversations without a separate NLP step. The model handles accented speech, telephone audio quality, and technical vocabulary reasonably well.

Deepgram charges per hour of audio transcribed, with pricing that's competitive with major cloud providers and often significantly cheaper at volume. A free tier provides $200 in credit for new accounts. Enterprise customers get custom models trained on domain-specific vocabulary (medical terminology, legal language, product-specific terms) that reduce errors in specialised use cases. Call centres, podcast hosting platforms, meeting intelligence tools, and voice AI developers are the main enterprise customers — anywhere that speech-to-text accuracy and throughput are core infrastructure concerns rather than nice-to-have features.