---
title: 'SmolAgents'
name: 'SmolAgents'
subtitle: 'Biblioteca ligera de agentes de IA de Hugging Face'
slug: 'smolagents'
description: 'SmolAgents es una pequeña biblioteca de Python de código abierto de Hugging Face para crear agentes de IA. Se centra en agentes que escriben y ejecutan código para resolver tareas, admite muchos modelos y herramientas, y mantiene el núcleo simple.'
website: 'https://huggingface.co/docs/smolagents'
company: 'hugging-face'
logo_url: ''
category: 'ai-agents'
category_name: 'Agentes de IA'
price: 'Free'
featured: false
rank: 8
alternatives:
  - langgraph
  - crewai
  - agno-ai
  - mastra
  - autogen-ai
  - langchain
  - llamaindex
date: '2025-09-21'
tags: [ai_agent, automation, autonomous, ai_assistants, agents, multi_agent, task_automation, orchestration, agentic, integrations, model_based]
i18n_source: '2acb38d44046'
---

SmolAgents está pensada para ser fácil de leer y de usar. La lógica central cabe en poco código y crear un agente lleva unas pocas líneas: eliges un modelo, le das herramientas y lanzas una tarea. Su idea distintiva es el agente de código, en el que el modelo escribe sus acciones como código Python en lugar de llamadas estructuradas a herramientas. Así puede combinar pasos, usar bucles y variables y resolver problemas de varios pasos con eficiencia, y este enfoque suele necesitar menos pasos que los métodos tradicionales.

Funciona con una gran variedad de modelos, desde API alojadas hasta modelos locales, y admite herramientas del Hub de Hugging Face, de LangChain y del Model Context Protocol. Hay configuraciones multiagente, agentes de visión y de navegación web y opciones de ejecución en entorno aislado, ya que ejecutar código escrito por un modelo exige medidas de protección. La biblioteca se integra con el Hub de Hugging Face para compartir agentes y herramientas.

SmolAgents es gratuita y de código abierto, con licencia Apache 2.0. Ejecutar código generado conlleva riesgos de seguridad, por lo que es imprescindible un entorno seguro. Es más ligera que frameworks como LangGraph o CrewAI, que ofrecen más estructura para flujos de trabajo complejos, y el SDK de OpenAI Agents es otra opción sencilla. SmolAgents encaja con desarrolladores que quieren una forma mínima y transparente de experimentar con agentes.
