---
title: 'Whisper'
name: 'Whisper'
subtitle: 'Modelo de código aberto da OpenAI para transcrição de fala em texto'
slug: 'whisper'
description: 'O Whisper é o modelo de reconhecimento de fala de código aberto da OpenAI. Ele transcreve áudio em vários idiomas, traduz fala para o inglês e lida bem com sotaques e ruído de fundo. Você pode executá-lo por conta própria ou usá-lo pela API da OpenAI.'
website: 'https://openai.com/research/whisper'
company: 'openai'
logo_url: ''
category: 'transcription'
category_name: 'Transcrição'
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

O Whisper é um modelo de conversão de fala em texto treinado com uma coleção muito grande e variada de áudio multilíngue. Esse treinamento o tornou excepcionalmente robusto: ele lida com sotaques, ruído de fundo e vocabulário técnico melhor do que muitos sistemas anteriores, e funciona em dezenas de idiomas. Também identifica automaticamente o idioma falado, adiciona pontuação e pode traduzir para texto em inglês falas em outros idiomas.

O modelo é disponibilizado como código aberto em vários tamanhos: alguns rodam em um laptop, enquanto os maiores exigem uma boa GPU. Essa abertura levou à criação de um amplo ecossistema: versões mais rápidas, como whisper.cpp e faster-whisper, ferramentas que adicionam marcações de tempo e identificação de falantes, além de muitos aplicativos de transcrição, legendagem e ditado que o utilizam nos bastidores. A OpenAI também oferece acesso pela API para quem não quer hospedá-lo.

Executar o Whisper por conta própria é gratuito; a API é cobrada por minuto de áudio. O modelo tem limitações conhecidas. Ele pode inventar texto durante silêncios ou trechos ruidosos, o que preocupa em trabalhos médicos e jurídicos, e a versão básica não identifica quem está falando nem funciona em tempo real sem ferramentas adicionais. Para legendas ao vivo ou transcrições com separação de falantes, serviços como AssemblyAI, Deepgram ou Google Speech-to-Text podem ser mais adequados. Para transcrição privada e local sem custo, o Whisper continua sendo uma das principais opções.
