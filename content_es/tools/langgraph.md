---
title: 'LangGraph'
name: 'LangGraph'
subtitle: 'Framework basado en grafos para agentes con estado y de larga duración'
slug: 'langgraph'
description: 'LangGraph es un framework de código abierto del equipo de LangChain para crear agentes con estado como grafos de pasos. Admite ramificaciones, bucles, memoria persistente, pasos de aprobación humana y streaming, y se combina con LangSmith para el despliegue y la monitorización.'
website: 'https://www.langchain.com/langgraph'
logo_url: ''
category: 'ai-agents'
category_name: 'Agentes de IA'
price: 'Free'
featured: false
rank: 8
alternatives:
  - langchain
  - crewai
  - autogen-ai
  - llamaindex
  - smolagents
  - mastra
date: '2026-11-05'
tags: [ai_agent, automation, autonomous, ai_assistants, agents, multi_agent, task_automation, orchestration, agentic, collaboration, model_based]
i18n_source: '50181c5f4cd8'
---

LangGraph modela un agente como un grafo. Cada nodo es un paso, como llamar a un modelo, ejecutar una herramienta o comprobar una condición, y las aristas definen el flujo entre pasos, con bucles y ramificaciones. Un objeto de estado compartido transmite la información. Esta estructura explícita da a los desarrolladores control sobre lo que hace el agente y cuándo, y hace que los agentes complejos sean más fáciles de entender que un bucle libre.

Lo distinguen funciones pensadas para producción. Los checkpoints guardan el estado para poder pausar y reanudar una ejecución, o recuperarse de un fallo. Los pasos con intervención humana permiten que un agente espere una aprobación antes de actuar, y la depuración con viaje en el tiempo deja repetir y editar pasos anteriores. Admite streaming de resultados intermedios, memoria a largo plazo y diseños multiagente, en Python y JavaScript.

La biblioteca es gratuita y de código abierto. El alojamiento y la monitorización se ofrecen a través de LangSmith, que tiene un nivel gratuito y planes de pago. LangGraph tiene una curva de aprendizaje más pronunciada que las bibliotecas de agentes de alto nivel, y su potencia se aprovecha más en flujos de trabajo complejos. CrewAI y AutoGen ofrecen abstracciones multiagente de más alto nivel, el OpenAI Agents SDK es más sencillo para trabajar con OpenAI y creadores visuales como n8n y Dify convienen a quienes no programan. Muchos agentes en producción se construyen con LangGraph.
