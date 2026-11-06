---
title: 'DeepSeek Harness'
name: 'DeepSeek Harness'
subtitle: 'Open-source, plugin-first framework for building coding agents on DeepSeek models'
slug: 'deepseek-harness'
description: 'DeepSeek Harness is an open-source agent runtime for coding agents. Models, tools, sandboxes, and orchestration are swappable plugins, and it works with DeepSeek''s models and other providers.'
website: 'https://deepseek.com/harness/en/'
company: 'deepseek'
logo_url: ''
category: 'devtools'
category_name: 'DevTools'
price: 'Free'
featured: false
rank: 5
alternatives:
  - claude-code
  - cline
  - continue-dev
  - aider
  - opencode
  - gemini-cli
date: '2026-08-17'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, open_source, autonomous, model_based]
---

DeepSeek Harness is a framework for running agents that work on code. It provides the loop that lets a model plan, call tools, read and edit files, run shell commands, and report back, similar in purpose to terminal agents from other labs. Its notable design choice is that nearly every part is a plugin: the model adapter, tool registry, session log, and the agent loop itself can be replaced.

It includes presets for common setups, such as a standard coding agent with filesystem and shell tools, web search, subagents, and a planning mode, and a mode for building custom presets. Sandboxing uses the operating system's own mechanisms to limit what the agent can touch. Although DeepSeek made it, it can connect to models from other providers.

The project is open source under the MIT license and still in early preview, with warnings that compatibility may break and limited outside contributions so far. DeepSeek has not published evaluations of the runtime itself. Alternatives include Claude Code, OpenAI Codex, Gemini CLI, OpenCode, and Aider. DeepSeek Harness suits developers who want a hackable agent runtime.
