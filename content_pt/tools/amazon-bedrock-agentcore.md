---
title: 'Amazon Bedrock AgentCore'
name: 'Amazon Bedrock AgentCore'
subtitle: 'Infraestrutura gerenciada para levar agentes de IA de protótipos à produção'
slug: 'amazon-bedrock-agentcore'
description: 'AgentCore cuida do trabalho de infraestrutura necessário para levar um agente de protótipo à produção. Um ambiente de execução hospeda agentes com isolamento de sessões para separar o trabalho de cada usuário e gerencia a escala. Recursos de identidade permitem que agentes se autentiquem em outros serviços em nome do usuário; um gateway transforma APIs e serviços existentes em ferramentas que os agentes podem chamar; e a observabilidade rastreia as ações dos agentes. Desenvolvedores podem usar frameworks como LangGraph, CrewAI e Strands Agents SDK, com modelos do Bedrock ou de outros provedores.'
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
AgentCore trata do trabalho de infraestrutura necessário para levar um agente do protótipo à produção. Um ambiente de execução hospeda agentes com isolamento de sessão, mantendo separado o trabalho de cada usuário, e cuida da escalabilidade. Recursos de identidade permitem que agentes se autentiquem em outros serviços em nome de um usuário; um gateway transforma APIs e serviços existentes em ferramentas que agentes podem chamar; e a observabilidade rastreia as ações dos agentes. Desenvolvedores podem usar frameworks como LangGraph, CrewAI e Strands Agents SDK, com modelos do Bedrock ou de outros provedores.

A memória é um componente central. AgentCore armazena contexto de curto prazo em uma sessão e memórias de longo prazo entre sessões, inclusive memória episódica, que permite ao agente recordar interações anteriores. Um recurso de políticas, atualmente em prévia, permite que equipes definam limites para as ações dos agentes. Ferramentas de interpretação de código e navegador dão aos agentes meios de executar código e usar a web em ambientes isolados e seguros.

AgentCore cobra pelo uso de seus componentes, sem compromisso inicial. Destina-se a equipes que já desenvolvem na AWS e querem infraestrutura gerenciada para agentes. As alternativas incluem o serviço de agentes do Azure AI Foundry, o Vertex AI Agent Engine do Google e pilhas de código aberto ou autogerenciadas sobre Kubernetes. A escolha costuma depender da nuvem que a empresa já usa. Consulte a entrada Amazon Bedrock para conhecer o serviço de modelos que está por trás dele.