---
title: Whisper
name: Whisper
subtitle: Open-Source-Modell von OpenAI zur Umwandlung von Sprache in Text
slug: whisper
description: Whisper ist das quelloffene Spracherkennungsmodell von OpenAI. Es transkribiert Audio in vielen Sprachen, übersetzt
  Gesprochenes ins Englische und kommt gut mit Akzenten und Hintergrundgeräuschen zurecht. Du kannst es selbst betreiben oder
  über die API von OpenAI nutzen.
website: https://openai.com/research/whisper
company: openai
logo_url: ''
category: transcription
category_name: Transcription
price: Free
featured: false
rank: 9
alternatives:
- assemblyai
- deepgram
- speechmatics
- gladia
- azure-ai-speech
date: '2026-07-17'
tags:
- transcription
- speech_to_text
- audio
- text
- conversion
- captions
- subtitles
- accuracy
- real_time
- open_source
- free_tier
- voice_enabled
i18n_source: 'bb082e1aec7b'
---

Whisper ist ein Modell zur Umwandlung von Sprache in Text, das mit einer sehr großen und vielfältigen Sammlung mehrsprachiger Audiodaten trainiert wurde. Dadurch ist es ungewöhnlich robust: Es kommt mit Akzenten, Hintergrundgeräuschen und Fachbegriffen besser zurecht als viele frühere Systeme und funktioniert in Dutzenden Sprachen. Außerdem erkennt es die gesprochene Sprache automatisch, ergänzt Satzzeichen und kann Sprache aus anderen Sprachen in englischen Text übersetzen.

Das quelloffene Modell gibt es in mehreren Größen. Kleinere Varianten laufen auf einem Laptop, größere benötigen eine leistungsfähige GPU. Die Offenheit hat ein großes Ökosystem hervorgebracht: schnellere Varianten wie whisper.cpp und faster-whisper, Werkzeuge für Zeitstempel und Sprecherkennzeichnung sowie zahlreiche Transkriptions-, Untertitel- und Diktier-Apps, die Whisper im Hintergrund nutzen. OpenAI bietet das Modell auch über eine API an, falls du es nicht selbst hosten möchtest.

Whisper ist kostenlos, wenn du es selbst betreibst. Die API wird pro Audiominute abgerechnet. Das Modell hat bekannte Schwächen: Bei Stille oder verrauschten Abschnitten kann es Text erfinden. Das ist bei medizinischen und juristischen Anwendungen problematisch. Das Basismodell kennzeichnet nicht, wer gerade spricht, und funktioniert ohne zusätzliche Werkzeuge nicht in Echtzeit. Für Live-Untertitel oder nach Sprecher getrennte Transkripte eignen sich möglicherweise AssemblyAI, Deepgram oder Google Speech-to-Text besser. Für private, lokale Transkription ohne Kosten bleibt Whisper eine der ersten Optionen.
