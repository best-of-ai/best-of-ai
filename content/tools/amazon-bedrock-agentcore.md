---
title: 'Amazon Bedrock AgentCore'
name: 'Amazon Bedrock AgentCore'
subtitle: 'AWS platform for building, deploying and running production AI agents'
slug: 'amazon-bedrock-agentcore'
description: 'Amazon Bedrock AgentCore is AWS''s platform for building and running AI agents in production. It provides managed runtime, identity, memory, gateway tools, and policy controls, and works with agents built on any framework or model.'
website: 'https://aws.amazon.com/bedrock/agentcore/'
company: 'amazon'
logo_url: ''
category: 'ai-agents'
category_name: 'AI Agents'
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
---

AgentCore addresses the infrastructure work of taking an agent from prototype to production. A runtime hosts agents with session isolation so each user's work is kept separate, and handles scaling. Identity features let agents authenticate to other services on a user's behalf, a gateway turns existing APIs and services into tools agents can call, and observability traces what agents do. Developers can use it with frameworks such as LangGraph, CrewAI, and the Strands Agents SDK, and with models on Bedrock or from other providers.

Memory is a major component. AgentCore stores short-term context within a session and long-term memories across sessions, including episodic memory that lets an agent recall earlier interactions. A policy capability, currently in preview, lets teams set boundaries on what agents may do. Code interpreter and browser tools give agents ways to run code and use the web in secure sandboxes.

AgentCore is priced on usage of its components, with no upfront commitment. It is aimed at teams already building on AWS and wanting managed infrastructure for agents. Alternatives include Azure AI Foundry's agent service, Google's Vertex AI Agent Engine, and open-source or self-managed stacks built on Kubernetes. The right choice often depends on which cloud a company already uses. See the Amazon Bedrock entry for the model service that underlies it.
