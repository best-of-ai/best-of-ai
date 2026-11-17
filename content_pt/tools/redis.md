---
title: Redis
name: Redis
subtitle: Banco de dados em memória para cache e busca vetorial
slug: redis
description: Redis é um armazenamento de dados em memória usado para cache, filas,
  sessões e recursos em tempo real. Também oferece busca vetorial, JSON e cache semântico,
  por isso equipes o utilizam em aplicativos de IA que precisam de consultas rápidas.
website: https://redis.io
logo_url: ''
category: devtools
category_name: Ferramentas para desenvolvedores
price: Freemium
featured: false
rank: 8
alternatives:
- pinecone
- qdrant
- weaviate
- mongodb-atlas
- elasticsearch
date: '2026-11-05'
tags:
- developer_tools
- code_generation
- infrastructure
- deployment
- development
- devops
- ci_cd
- cloud
- api
- collaboration
- fast
i18n_source: 294da6bd62ae
---

Redis armazena dados em memória, o que torna a leitura e a gravação extremamente rápidas. Desenvolvedores o usam como cache diante de um banco de dados mais lento, armazenamento de sessão para usuários conectados, fila de mensagens e para placares, limitação de taxa e contadores. Tipos de dados como listas, conjuntos, conjuntos ordenados, hashes e streams facilitam esses padrões com comandos simples. É uma das infraestruturas mais amplamente implantadas na web.

Para IA, Redis acrescentou busca vetorial, permitindo armazenar embeddings e encontrar itens semelhantes para geração aumentada por recuperação, recomendações e busca semântica. O cache semântico guarda respostas a perguntas anteriores e as retorna para novas perguntas semelhantes, reduzindo custo e latência ao chamar modelos de linguagem. Redis também armazena a memória de conversas de agentes. Pode ser executado como software de código aberto, Redis Cloud ou em implantações corporativas.

O licenciamento foi tema de debate: Redis mudou sua licença, o que levou a uma bifurcação comunitária chamada Valkey, apoiada por provedores de nuvem; depois, voltou a oferecer uma opção de licença de código aberto. Memória custa mais que disco, então grandes conjuntos de dados podem sair caros, e a durabilidade exige configuração. Entre as alternativas estão Valkey, Memcached para cache simples, DragonflyDB e serviços de nuvem como Amazon ElastiCache. Redis atende aplicativos em que velocidade é essencial.
