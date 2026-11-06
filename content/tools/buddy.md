---
title: 'Buddy'
name: 'Buddy'
subtitle: 'CI/CD platform that runs AI coding agents in pipelines and sandboxes'
slug: 'buddy'
description: 'Buddy is a CI/CD and deployment platform that can run AI coding agents such as Claude Code, Codex CLI, and Cursor as pipeline actions or inside isolated cloud sandboxes. Agents on a developer''s machine can also control Buddy through a remote MCP server or the bdy CLI.'
website: 'https://buddy.works'
logo_url: ''
category: 'devtools'
category_name: 'DevTools'
price: 'Freemium'
featured: false
rank: 5
alternatives:
  - gitlab-duo
  - github-agent-hq
  - daytona
  - e2b-ai
date: '2026-11-06'
tags: [developer_tools, devops, ci_cd, deployment, infrastructure, automation, ai_agent, agentic, cloud]
---

Buddy builds, tests, and deploys code through pipelines that can be set up in the web UI or defined in YAML. Pipelines start on a push, a pull request, a schedule, or a webhook. Deployment actions cover cloud providers, Kubernetes, servers over SSH, and static hosting.

AI coding agents can run as regular pipeline actions. Claude Code, Codex CLI, Cursor, Antigravity, and Grok Build are available as built-in actions, and they get the same code, variables, and integrations as other steps in the pipeline. Typical uses are reviewing a pull request when it opens, writing PR descriptions, generating release notes, or trying to fix a new Sentry error. Work that does not fit a pipeline step can run in a sandbox, an isolated Ubuntu environment with Node, Python, Go, and Docker preinstalled. Buddy fetches the repository into the sandbox, and the agent works on that copy instead of a developer's machine. Sandboxes can be managed with the bdy CLI or a TypeScript SDK.

An agent running locally can also control Buddy through a remote MCP server or an installable skill. It can then run pipelines, read build logs, deploy to environments, and manage sandboxes on request. The free plan has one seat, two concurrent runs, and $1 of usage credit per month, and paid plans add seats and pay-as-you-go usage. A self-hosted version is also available. Alternatives include GitHub Actions with Copilot agents, GitLab Duo, CircleCI, and sandbox providers such as E2B and Daytona.
