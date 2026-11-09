---
title: 'Temporal'
name: 'Temporal'
subtitle: 'Plataforma de ejecución duradera para flujos de trabajo de larga duración'
slug: 'temporal'
description: 'Temporal es una plataforma de código abierto para ejecutar flujos de trabajo como código con ejecución duradera. Conserva el estado si un servidor se cae, de modo que los trabajos largos se reanudan donde se quedaron, y se usa en pagos, incorporación de clientes, pipelines de datos y agentes de IA.'
website: 'https://temporal.io'
logo_url: ''
category: 'devtools'
category_name: 'Herramientas para desarrolladores'
price: 'Freemium'
featured: false
rank: 7
alternatives:
  - inngest
  - trigger-dev
  - prefect
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, collaboration]
i18n_source: 'db4f201d9543'
---

Temporal aborda una parte difícil de crear software fiable: lograr que los procesos largos y de varios pasos sobrevivan a los fallos. Los desarrolladores escriben los flujos de trabajo en un lenguaje de programación normal como Go, Java, Python o TypeScript, y Temporal registra cada paso y su estado, de modo que si un servidor se cae o falla una llamada de red, el flujo continúa desde donde se detuvo sin perder progreso. Los reintentos, los tiempos de espera y los temporizadores vienen incluidos.

Eso lo hace adecuado para procesos que duran de minutos a meses, como flujos de pago, gestión de pedidos, incorporación de clientes, aprovisionamiento de infraestructura y procesamiento de datos. Cada vez más equipos lo usan para orquestar agentes de IA, cuyas tareas llaman a modelos y herramientas durante largos periodos y necesitan fiabilidad y observabilidad. Temporal Cloud ofrece un servicio gestionado, y el servidor de código abierto se puede alojar por cuenta propia.

Temporal es gratuito y de código abierto con licencia MIT, y Temporal Cloud se cobra según el uso. Su modelo tiene una curva de aprendizaje, y los equipos deben ejecutar el servicio o pagar por él. Entre las alternativas están AWS Step Functions, Apache Airflow para flujos de datos, Inngest, Restate, Camunda y colas como Celery. Temporal sirve para equipos de ingeniería que construyen procesos críticos y de larga duración.
