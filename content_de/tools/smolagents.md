---
title: SmolAgents
name: SmolAgents
subtitle: Leichtgewichtiges KI-Agenten-Framework von Hugging Face
slug: smolagents
description: SmolAgents ist eine kleine Open-Source-Python-Bibliothek von Hugging Face zum Erstellen von KI-Agenten. Sie konzentriert
  sich auf Agenten, die Code schreiben und ausführen, unterstützt viele Modelle und Werkzeuge und hält den Kern bewusst schlank.
website: https://huggingface.co/docs/smolagents
company: hugging-face
logo_url: ''
category: ai-agents
category_name: KI-Agenten
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
i18n_source: '2acb38d44046'
---

SmolAgents ist auf einfache Lesbarkeit und Nutzung ausgelegt. Die Kernlogik umfasst wenig Code; ein Agent lässt sich mit wenigen Zeilen erstellen: Modell auswählen, Werkzeuge bereitstellen und Aufgabe starten. Das besondere Konzept ist der Code-Agent. Das Modell schreibt Aktionen als Python-Code statt als strukturierte Werkzeugaufrufe. Dadurch kann es Schritte kombinieren, Schleifen und Variablen verwenden und mehrstufige Probleme effizient lösen. Häufig benötigt diese Methode weniger Schritte als herkömmliche Ansätze.

SmolAgents funktioniert mit vielen Modellen, von gehosteten APIs bis zu lokalen Modellen, und unterstützt Werkzeuge von Hugging Face Hub, LangChain und dem Model Context Protocol. Es gibt Multi-Agenten-Setups, Bildverarbeitungs- und Webbrowser-Agenten sowie Optionen zur Ausführung in einer Sandbox. Da vom Modell geschriebener Code ausgeführt wird, sind Schutzmaßnahmen erforderlich. Die Bibliothek ist mit dem Hugging-Face-Hub verbunden, über den Agenten und Tools geteilt werden können.

SmolAgents ist kostenlos und steht unter der Apache-2.0-Lizenz als Open Source zur Verfügung. Das Ausführen generierten Codes birgt Sicherheitsrisiken; eine sichere Umgebung ist daher unerlässlich. Das Framework ist schlanker als LangGraph oder CrewAI, die mehr Struktur für komplexe Abläufe bieten. Das OpenAI Agents SDK ist eine weitere einfache Option. SmolAgents passt zu Entwickler:innen, die Agenten minimalistisch und transparent ausprobieren möchten.
