---
title: 'LangGraph'
name: 'LangGraph'
subtitle: 'Framework baseado em grafos para agentes com estado e execução prolongada'
slug: 'langgraph'
description: 'LangGraph é um framework de código aberto da equipe LangChain para criar agentes com estado como grafos de etapas. Oferece ramificações, ciclos, memória persistente, etapas de aprovação humana e transmissão de resultados e se integra ao LangSmith para implantação e monitoramento.'
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

LangGraph representa um agente como um grafo. Cada nó é uma etapa, como chamar um modelo, executar uma ferramenta ou verificar uma condição, e as arestas definem o fluxo entre etapas, incluindo ciclos e ramificações. Um objeto de estado compartilhado transporta informações. Essa estrutura explícita dá aos desenvolvedores controle sobre o que o agente faz e quando, facilitando entender agentes complexos em comparação com ciclos sem controle.

Recursos voltados à produção o diferenciam. Pontos de verificação salvam o estado para que uma execução possa pausar e continuar ou se recuperar de uma falha. Etapas com participação humana permitem que um agente aguarde aprovação antes de agir, e a depuração por viagem no tempo permite reproduzir e editar etapas anteriores. O framework oferece transmissão de resultados intermediários, memória de longo prazo e projetos multiagentes em Python e JavaScript.

A biblioteca é gratuita e de código aberto. Hospedagem e monitoramento estão disponíveis pelo LangSmith, que tem uma faixa gratuita e planos pagos. LangGraph tem uma curva de aprendizado mais íngreme que bibliotecas de agentes de alto nível, e suas vantagens são maiores em fluxos complexos. CrewAI e AutoGen oferecem abstrações multiagentes de nível mais alto; OpenAI Agents SDK é mais simples para trabalhos centrados na OpenAI; construtores visuais como n8n e Dify atendem pessoas sem programação. Muitos agentes de produção são criados com LangGraph.
