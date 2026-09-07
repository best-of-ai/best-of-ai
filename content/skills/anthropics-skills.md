---
title: 'skills'
name: 'skills'
slug: 'anthropics-skills'
subtitle: 'Anthropic''s official repository of Agent Skills for Claude, organized by category.'
description: 'This is Anthropic''s own repository of Agent Skills: folders of instructions and supporting files that Claude loads to handle specialized tasks such as document creation or web app testing. Most skills use the Apache 2.0 license, but the document skills (docx, pdf, pptx, xlsx) are source-available rather than open source, since they double as the reference implementations behind Claude''s built-in document features.'
author: 'anthropics'
skill_type: 'Document Automation'
source_url: 'https://github.com/anthropics/skills'
compatible_with: ['Claude Code', 'Claude.ai', 'Claude API']
install: 'In Claude Code, add the marketplace with /plugin marketplace add anthropics/skills, then install a set such as /plugin install document-skills@anthropic-agent-skills.'
price: 'Free'
open_source: true
license: 'Apache-2.0 (most skills); source-available for the document skills'
stars: 174950
stars_this_week: 322
stars_updated: '2026-09-07'
rank: 10
date: '2026-09-07'
tags: [anthropic, official, document-automation]
---
This repository bundles the following skills:

- **docx**: Creates and edits Word documents.
- **pdf**: Creates, reads, and edits PDF files.
- **pptx**: Creates and edits PowerPoint presentations.
- **xlsx**: Creates and edits Excel spreadsheets.
- **mcp-builder**: Guides building a Model Context Protocol server.
- **webapp-testing**: Helps Claude test a web application.
- **skill-creator**: A meta skill for creating new Agent Skills.
- **brand-guidelines**: Applies Anthropic's brand guidelines to generated output.
- **canvas-design**: Supports building visual canvas-style layouts.
- **frontend-design**: Gives guidance on frontend visual design choices.
- **algorithmic-art**: Generates algorithmic or generative art.
- **slack-gif-creator**: Creates GIFs for use in Slack.
- **doc-coauthoring**: Supports collaborative document writing and editing.
- **internal-comms**: Drafts internal memos and team announcements.
