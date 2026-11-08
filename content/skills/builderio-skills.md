---
title: 'skills'
name: 'skills'
slug: 'builderio-skills'
subtitle: 'Small, composable skills from Builder.io for watching, reviewing and shipping agent work.'
description: 'Builder.io''s skill set leans toward supervising agents. Skills can watch another agent''s session, babysit a pull request through checks and review, run a review queue, and send digests of work that needs a human decision. The ''factory'' skills are marked experimental. The repo has about 26 skills.'
author: 'BuilderIO'
skill_type: 'Workflow & Productivity'
source_url: 'https://github.com/BuilderIO/skills'
compatible_with: ['Claude Code', 'Codex']
install: 'Run npx @agent-native/skills@latest add to pick from the recommended skills.'
price: 'Free'
open_source: true
license: 'MIT'
stars: 4651
stars_this_week: 0
stars_updated: '2026-11-08'
rank: 5
date: '2026-11-08'
tags: [workflow, pull-requests, orchestration, code-review]
---
This repository bundles the following skills:

- **agent-watchdog**: Watches, audits or fixes another agent's work from a session ID.
- **efficient-orchestrator**: Runs a larger task with an orchestrating agent, only when explicitly invoked.
- **factory-collect**: Collects and triages feedback, telemetry, errors and issues.
- **factory-babysit-pr**: Follows one authorized pull request through checks and review.
- **factory-review-prs**: Reviews a queue of pull requests with separate reply, approval and merge criteria.
- **factory-human-digest**: Summarizes work that still needs human judgment across configured repos.
