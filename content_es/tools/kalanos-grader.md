---
title: 'Kalanos Grader'
name: 'Kalanos Grader'
subtitle: 'Auditoría de calidad de código abierto para grabaciones de entrenamiento de robots'
slug: 'kalanos-grader'
description: 'Kalanos Grader es una herramienta de línea de comandos gratuita y con licencia Apache-2.0 que audita en local grabaciones de entrenamiento de robots e IA física. Puntúa problemas de tiempos, movimiento, integridad, visión y anotación y genera un informe en HTML o JSON.'
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

Kalanos Grader revisa los episodios grabados de un robot antes de entrenar con ellos. Se instala con pip y se ejecuta con `kalanos grade ./my_recordings --report audit.html`. Busca problemas de tiempos, de señal y de movimiento, muestra qué episodios hay que revisar y por qué, y guarda el resultado como informe HTML o como JSON. No hace falta cuenta, y las auditorías locales se ejecutan en tu propio equipo.

Cada grabación recibe una puntuación de 0 a 100 en cinco familias: integridad, tiempos, movimiento, visión y anotación. Por defecto, la integridad pesa 3, tiempos, movimiento y visión pesan 2 cada una, y la anotación pesa 1. La puntuación mide la calidad dentro de lo evaluado. Kalanos aclara que no es una tasa de aprobados ni una predicción de cómo se comportará un modelo entrenado. La página muestra una auditoría de ejemplo de 50 episodios de ALOHA, de los que 39 pasaron y 11 necesitaron revisión.

Requiere Python 3.10 o superior. Los conjuntos de datos LeRobot v2.0, v2.1 y v3.0, y los archivos CSV y JSON o JSONL funcionan con el paquete base. Las grabaciones HDF5 y MCAP o ROS 2 necesitan extras, las comprobaciones de cámara necesitan el extra de vídeo, y es posible que algunos diseños HDF5 arbitrarios no se puedan mapear. Un informe completo de 1000 episodios tardó unos 52 minutos en la prueba propia de Kalanos, que según la empresa no es un benchmark. Es útil para equipos de aprendizaje por imitación que quieren revisar rápido la calidad de un conjunto de datos.
