---
title: 'Amazon Bedrock AgentCore'
name: 'Amazon Bedrock AgentCore'
subtitle: 'Plataforma de AWS para crear, desplegar y ejecutar agentes de IA en producción'
slug: 'amazon-bedrock-agentcore'
description: 'Amazon Bedrock AgentCore es la plataforma de AWS para crear y ejecutar agentes de IA en producción. Ofrece entorno de ejecución gestionado, identidad, memoria, herramientas de pasarela y controles de políticas, y funciona con agentes creados con cualquier framework o modelo.'
website: 'https://aws.amazon.com/bedrock/agentcore/'
company: 'amazon'
logo_url: ''
category: 'ai-agents'
category_name: 'Agentes de IA'
price: 'Paid'
featured: false
rank: 7
alternatives:
  - azure-ai-foundry
  - vertex-ai
  - databricks-agent-bricks
  - salesforce-agentforce
date: '2026-11-05'
tags: [ai, assistant, automation, productivity, enterprise, agent]
i18n_source: '27c7992a821e'
---

AgentCore se ocupa del trabajo de infraestructura necesario para llevar un agente del prototipo a producción. Un entorno de ejecución aloja los agentes con aislamiento de sesión, de modo que el trabajo de cada usuario se mantiene separado, y gestiona el escalado. Las funciones de identidad permiten que los agentes se autentiquen en otros servicios en nombre de un usuario, una pasarela convierte las API y servicios existentes en herramientas que los agentes pueden llamar, y la observabilidad registra lo que hacen los agentes. Los desarrolladores pueden usarlo con frameworks como LangGraph, CrewAI y el Strands Agents SDK, y con modelos de Bedrock o de otros proveedores.

La memoria es un componente importante. AgentCore almacena contexto a corto plazo dentro de una sesión y recuerdos a largo plazo entre sesiones, incluida una memoria episódica que permite al agente recordar interacciones anteriores. Una capacidad de políticas, actualmente en versión preliminar, permite a los equipos fijar límites a lo que pueden hacer los agentes. Las herramientas de intérprete de código y de navegador dan a los agentes formas de ejecutar código y usar la web en entornos aislados seguros.

AgentCore se cobra según el uso de sus componentes, sin compromiso inicial. Está dirigido a equipos que ya construyen sobre AWS y quieren infraestructura gestionada para agentes. Entre las alternativas están el servicio de agentes de Azure AI Foundry, Vertex AI Agent Engine de Google y pilas de código abierto o autogestionadas basadas en Kubernetes. La elección adecuada suele depender de qué nube use ya la empresa. Consulta la ficha de Amazon Bedrock para el servicio de modelos en el que se apoya.
