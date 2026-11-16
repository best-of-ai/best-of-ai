---
title: 'Whisper'
name: 'Whisper'
subtitle: "Modèle open source de reconnaissance vocale d'OpenAI"
slug: 'whisper'
description: "Whisper est le modèle open source de reconnaissance vocale d'OpenAI. Il transcrit l'audio dans beaucoup de langues, traduit la parole en anglais, et gère bien les accents et le bruit de fond. Tu peux le faire tourner toi-même ou l'utiliser via l'API d'OpenAI."
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
i18n_source: 'bb082e1aec7b'
---

Whisper est un modèle de reconnaissance vocale entraîné sur une très grande collection variée d'audio multilingue. Cet entraînement l'a rendu inhabituellement robuste : il gère les accents, le bruit de fond et le vocabulaire technique mieux que beaucoup de systèmes plus anciens, et il fonctionne dans des dizaines de langues. Il détecte aussi la langue parlée automatiquement, ajoute la ponctuation, et peut traduire la parole d'autres langues en texte anglais.

Le modèle est publié en open source en plusieurs tailles, des petites qui tournent sur un portable aux grandes qui ont besoin d'un bon GPU. Cette ouverture a mené à un large écosystème : des versions plus rapides comme whisper.cpp et faster-whisper, des outils qui ajoutent des horodatages et des étiquettes de locuteur, et beaucoup d'apps de transcription, de sous-titres et de dictée qui l'utilisent en coulisse. OpenAI le propose aussi via son API pour ceux qui ne veulent pas l'héberger.

Whisper est gratuit à faire tourner soi-même, et l'API est facturée à la minute d'audio. Il a des faiblesses connues. Il peut inventer du texte pendant les silences ou les passages bruyants, ce qui est un problème pour le travail médical et juridique, et le modèle de base n'étiquette pas qui parle et ne tourne pas en temps réel sans outils supplémentaires. Pour des sous-titres live ou des transcriptions séparées par locuteur, des services comme AssemblyAI, Deepgram ou Google Speech-to-Text peuvent mieux convenir. Pour une transcription locale et privée sans coût, Whisper reste un premier choix.
