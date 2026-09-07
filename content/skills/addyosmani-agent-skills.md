---
title: 'agent-skills'
name: 'agent-skills'
slug: 'addyosmani-agent-skills'
subtitle: '25 Claude skills covering a full engineering lifecycle from requirements to shipping.'
description: 'This repository packages Agent Skills covering stages of a software project (define, plan, build, verify, review, ship), plus one meta skill for choosing among them. Each skill encodes a specific workflow, such as writing a PRD, running a red-green-refactor test cycle, or building a staged rollout plan.'
author: 'addyosmani'
skill_type: 'Development & Engineering'
source_url: 'https://github.com/addyosmani/agent-skills'
compatible_with: ['Claude Code', 'Cursor', 'Codex', 'GitHub Copilot', 'Gemini CLI']
install: 'Install with npx skills add addyosmani/agent-skills, or via the Claude Code plugin marketplace.'
price: 'Free'
open_source: true
license: 'MIT'
stars: 92684
stars_this_week: 215
stars_updated: '2026-09-07'
rank: 9
date: '2026-09-07'
tags: [development, engineering, lifecycle]
---
This repository bundles the following skills:

- **interview-me**: Draws out requirements by asking targeted questions.
- **spec-driven-development**: Writes a PRD before any code is written.
- **constraint-driven-development**: Sets and enforces quality standards for a project.
- **planning-and-task-breakdown**: Splits a spec into tasks that can each be verified on its own.
- **incremental-implementation**: Delivers work in thin, tested vertical slices.
- **test-driven-development**: Applies the red-green-refactor cycle.
- **context-engineering**: Manages what information reaches the agent and when.
- **doubt-driven-development**: Runs an adversarial code review pass.
- **frontend-ui-engineering**: Guides component and interface design decisions.
- **api-and-interface-design**: Applies contract-first design to APIs and interfaces.
- **browser-testing-with-devtools**: Uses Chrome DevTools to inspect an app at runtime.
- **code-review-and-quality**: Reviews code against five separate quality gates.
- **security-and-hardening**: Checks code against the OWASP Top 10.
- **git-workflow-and-versioning**: Enforces a trunk-based git workflow.
- **shipping-and-launch**: Runs a staged rollout when releasing a change.
