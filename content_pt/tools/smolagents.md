---
title: SmolAgents
name: SmolAgents
subtitle: Biblioteca leve de agentes de IA da Hugging Face
slug: smolagents
description: SmolAgents é uma pequena biblioteca Python de código aberto da Hugging
  Face para criar agentes de IA. Prioriza agentes que escrevem e executam código para
  resolver tarefas, oferece suporte a vários modelos e ferramentas e mantém o núcleo
  simples.
website: https://huggingface.co/docs/smolagents
company: hugging-face
logo_url: ''
category: ai-agents
category_name: Agentes de IA
price: Free
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
tags:
- ai_agent
- automation
- autonomous
- ai_assistants
- agents
- multi_agent
- task_automation
- orchestration
- agentic
- integrations
- model_based
i18n_source: 2acb38d44046
---

SmolAgents foi projetada para ser fácil de ler e usar. A lógica central cabe em pouco código, e criar um agente leva poucas linhas: você escolhe um modelo, fornece ferramentas e executa uma tarefa. Sua ideia característica é o agente de código, em que o modelo escreve ações como código Python em vez de chamadas estruturadas de ferramentas. Isso permite combinar etapas, usar loops e variáveis e lidar com problemas de várias etapas com eficiência; essa abordagem muitas vezes exige menos etapas que métodos tradicionais.

A biblioteca funciona com vários modelos, de APIs hospedadas a modelos locais, e oferece suporte a ferramentas do Hugging Face Hub, LangChain e Model Context Protocol. Há configurações multiagente, agentes de visão e navegação na web e opções de execução em ambiente isolado, pois a execução de código escrito pelo modelo exige proteções. A biblioteca se integra ao Hub da Hugging Face para compartilhar agentes e ferramentas.

SmolAgents é gratuita e de código aberto sob a licença Apache 2.0. Executar código gerado envolve riscos de segurança, portanto é essencial usar um ambiente seguro. É mais leve que frameworks como LangGraph ou CrewAI, que oferecem mais estrutura para fluxos complexos; OpenAI Agents SDK é outra opção simples. SmolAgents atende desenvolvedores que querem experimentar agentes com uma ferramenta mínima e transparente.
