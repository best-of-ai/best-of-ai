---
title: LangGraph
name: LangGraph
subtitle: Graphbasiertes Framework für zustandsbehaftete, lang laufende Agenten
slug: langgraph
description: LangGraph ist ein quelloffenes Framework des LangChain-Teams zum Erstellen zustandsbehafteter Agenten als Graphen
  aus einzelnen Schritten. Es unterstützt Verzweigungen, Schleifen, dauerhaftes Gedächtnis, Freigaben durch Menschen und Streaming.
  LangSmith ergänzt Bereitstellung und Überwachung.
website: https://www.langchain.com/langgraph
logo_url: ''
category: ai-agents
category_name: AI Agents
price: Free
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
- collaboration
- model_based
i18n_source: '50181c5f4cd8'
---

LangGraph bildet einen Agenten als Graph ab. Jeder Knoten ist ein Schritt, etwa ein Modell aufzurufen, ein Werkzeug auszuführen oder eine Bedingung zu prüfen. Kanten legen den Ablauf zwischen den Schritten fest, einschließlich Schleifen und Verzweigungen. Ein gemeinsames Zustandsobjekt gibt Informationen weiter. Diese explizite Struktur ermöglicht Entwicklern zu steuern, was der Agent wann tut. Komplexe Agenten lassen sich dadurch besser nachvollziehen als freie Schleifen.

Funktionen für den Produktivbetrieb heben LangGraph hervor. Checkpoints speichern den Zustand. So kann ein Ablauf pausieren, fortgesetzt oder nach einem Fehler wiederhergestellt werden. Bei Schritten mit menschlicher Beteiligung wartet der Agent vor einer Aktion auf Freigabe. Mit Debugging durch Zurückspulen können Entwickler frühere Schritte erneut abspielen und bearbeiten. LangGraph unterstützt Streaming von Zwischenergebnissen, langfristiges Gedächtnis und Entwürfe mit mehreren Agenten in Python und JavaScript.

Die Bibliothek ist kostenlos und quelloffen. Hosting und Überwachung gibt es über LangSmith mit kostenlosem und kostenpflichtigem Tarif. LangGraph erfordert mehr Einarbeitung als Agentenbibliotheken auf höherer Abstraktionsebene. Seine Stärken zahlen sich vor allem bei komplexen Abläufen aus. CrewAI und AutoGen bieten übergeordnete Abstraktionen für mehrere Agenten. OpenAI Agents SDK ist für auf OpenAI ausgerichtete Arbeit einfacher. Visuelle Builder wie n8n und Dify eignen sich für Menschen ohne Programmierkenntnisse. Viele Agenten für den Produktivbetrieb werden mit LangGraph erstellt.
