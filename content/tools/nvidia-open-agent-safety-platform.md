---
title: 'NVIDIA Open Agent Safety Platform'
name: 'NVIDIA Open Agent Safety Platform'
subtitle: 'An open-source security layer that can quarantine a misbehaving AI agent within milliseconds'
slug: 'nvidia-open-agent-safety-platform'
description: 'NVIDIA''s Open Agent Safety Platform pairs OpenShell, an open runtime that sandboxes agents, with Sentry, a monitoring layer on BlueField DPUs that runs separately from the agent''s computer and can quarantine it.'
website: 'https://developer.nvidia.com/'
company: 'nvidia'
logo_url: ''
category: 'cybersecurity'
category_name: 'Cybersecurity'
price: 'Free'
featured: false
rank: 5
alternatives:
  - lakera
  - patronus-ai
  - giskard
  - nightfall
date: '2026-09-28'
tags: [ai_powered, intelligent, platform, tool, service, solution, saas, online]
---

The platform responds to a security worry: autonomous agents that can run commands and access data need limits that a compromised agent cannot disable. OpenShell is an open-source runtime that places each agent in its own sandbox with policy-based permissions, and a prover checks that granted permissions cannot combine into something the operator did not intend.

Sentry adds enforcement outside the agent's machine. It runs on BlueField data processing units, which sit apart from the host, so it can watch behavior and isolate an agent quickly even if the host is compromised. NVIDIA has described it as a reference design, with many partners integrating the pieces.

The software is open source and the hardware component requires NVIDIA infrastructure. Analysts note that proving permissions are consistent does not prove an agent is safe in every sense, and reviews of agent actions remain important. Alternatives include sandboxing tools such as E2B and Daytona, Anthropic's and OpenAI's sandboxing, and security startups focused on agents. NVIDIA's platform suits organizations deploying agents with strong isolation needs.
