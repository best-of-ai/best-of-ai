---
title: 'Kalanos Grader'
name: 'Kalanos Grader'
subtitle: 'Auditoria de qualidade de código aberto para gravações de treinamento de robôs'
slug: 'kalanos-grader'
description: 'O Kalanos Grader é uma ferramenta de linha de comando gratuita, com licença Apache-2.0, que audita localmente gravações de treinamento de robôs e IA física. Ele pontua problemas de tempo, movimento, integridade, visão e anotação e gera um relatório em HTML ou JSON.'
website: 'https://kalanos.ai/grader'
logo_url: ''
category: 'robotics'
category_name: 'Robótica'
price: 'Free'
featured: false
rank: 5
alternatives:
  - foxglove
  - cleanlab
  - formant
date: '2026-11-24'
tags: [robotics, data_quality, dataset_audit, imitation_learning, physical_ai, open_source, cli, python, lerobot, free_tier]
i18n_source: 'cadc52e004d3'
---

O Kalanos Grader verifica os episódios gravados de um robô antes de você treinar com eles. Você instala com pip e roda `kalanos grade ./my_recordings --report audit.html`. Ele procura problemas de tempo, sinal e movimento, mostra quais episódios precisam de revisão e por quê, e grava o resultado como relatório HTML ou JSON. Não é preciso conta, e as auditorias locais rodam na sua própria máquina.

Cada gravação recebe uma nota de 0 a 100 em cinco áreas: integridade, tempo, movimento, visão e anotação. Por padrão, a integridade tem peso 3, tempo, movimento e visão têm peso 2 cada, e a anotação tem peso 1. A nota mede a qualidade dentro do que foi avaliado. A Kalanos diz que ela não é uma taxa de aprovação nem uma previsão de como um modelo treinado vai se comportar. A página mostra uma auditoria de exemplo com 50 episódios do ALOHA, dos quais 39 passaram e 11 precisaram de revisão.

Exige Python 3.10 ou mais recente. Conjuntos de dados LeRobot v2.0, v2.1 e v3.0, além de arquivos CSV e JSON ou JSONL, funcionam com o pacote base. Gravações HDF5 e MCAP ou ROS 2 precisam de extras, as verificações de câmera precisam do extra de vídeo, e layouts HDF5 arbitrários podem não ser mapeados. Um relatório completo de 1.000 episódios levou cerca de 52 minutos na execução da própria Kalanos, que diz não ser um benchmark. Serve para equipes de aprendizado por imitação que querem checar rápido a qualidade de um conjunto de dados.
