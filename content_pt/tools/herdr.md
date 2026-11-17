---
title: Herdr
name: Herdr
subtitle: Aplicativo de computador de código aberto que mantém agentes de programação
  em execução em segundo plano
slug: herdr
description: O Herdr é um aplicativo nativo de código aberto para computador que executa
  terminais e agentes de programação, como Claude Code e Codex, em um só lugar. Ele
  usa um ambiente de execução chamado herdr-core, permitindo que as sessões continuem
  mesmo quando você fecha ou atualiza o aplicativo.
website: https://herdr.dev/
company: herdr
logo_url: ''
category: devtools
category_name: Ferramentas para desenvolvedores
price: Free
featured: false
rank: 5
alternatives:
- warp
- claude-code
- cursor
- cline
date: '2026-10-29'
tags:
- developer_tools
- terminal
- coding_agents
- open_source
- desktop_app
- multiplexer
- agent_management
- productivity
- cross_platform
- automation
i18n_source: '3491a22de0f6'
---

O Herdr gerencia a quantidade crescente de sessões de agentes executadas por desenvolvedores. Em vez de várias janelas de terminal, ele exibe os agentes em uma interface com abas e indica se cada um está trabalhando, terminou ou aguarda uma entrada, conforme o status informado pelo agente. Dá suporte a qualquer agente executado em um terminal.

A principal decisão de design é o ambiente de execução herdr-core, um pequeno servidor na sua máquina que mantém as sessões ativas. O aplicativo é apenas a interface, então fechá-lo ou atualizá-lo não interrompe os agentes. A versão de terminal do Herdr, a original, continua disponível como um programa separado com seu próprio servidor.

O Herdr é gratuito e de código aberto sob a licença Apache 2.0 e funciona em macOS, Linux e Windows. O aplicativo para computador é recente, então espere mudanças. Se a máquina reiniciar ou o núcleo parar, os programas em execução serão encerrados. Entre as alternativas estão tmux, Zellij, Warp, Conductor e multiplexadores de terminal integrados a ferramentas de agentes. O Herdr é indicado para desenvolvedores que executam vários agentes de programação ao mesmo tempo.
