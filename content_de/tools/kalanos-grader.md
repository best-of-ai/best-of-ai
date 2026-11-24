---
title: 'Kalanos Grader'
name: 'Kalanos Grader'
subtitle: 'Open-Source-Qualitätsprüfung für Trainingsaufnahmen von Robotern'
slug: 'kalanos-grader'
description: 'Kalanos Grader ist ein kostenloses Kommandozeilen-Tool unter Apache-2.0, das Trainingsaufnahmen von Robotern und Physical AI lokal prüft. Es bewertet Probleme bei Timing, Bewegung, Integrität, Vision und Annotation und schreibt einen HTML- oder JSON-Bericht.'
website: 'https://kalanos.ai/grader'
logo_url: ''
category: 'robotics'
category_name: 'Robotik'
price: 'Free'
featured: false
rank: 5
alternatives:
  - foxglove
  - cleanlab
  - formant
date: '2026-11-24'
tags: [robotics, data_quality, dataset_audit, imitation_learning, physical_ai, open_source, cli, python, lerobot, free_tier]
i18n_source: 'cadc52e004d3'
---

Kalanos Grader prüft aufgezeichnete Roboter-Episoden, bevor du damit trainierst. Du installierst es mit pip und führst `kalanos grade ./my_recordings --report audit.html` aus. Es sucht nach Problemen bei Timing, Signal und Bewegung, zeigt, welche Episoden überprüft werden müssen und warum, und schreibt das Ergebnis als HTML-Bericht oder als JSON. Ein Konto ist nicht nötig, und lokale Prüfungen laufen auf deinem eigenen Rechner.

Jede Aufnahme bekommt eine Punktzahl von 0 bis 100 in fünf Bereichen: Integrität, Timing, Bewegung, Vision und Annotation. Standardmäßig hat die Integrität das Gewicht 3, Timing, Bewegung und Vision je 2 und die Annotation 1. Die Punktzahl misst die Qualität im bewerteten Umfang. Kalanos sagt, dass sie weder eine Bestehensquote noch eine Vorhersage dafür ist, wie sich ein trainiertes Modell verhält. Die Seite zeigt eine Beispielprüfung von 50 ALOHA-Episoden, von denen 39 bestanden und 11 zur Überprüfung markiert wurden.

Es braucht Python 3.10 oder neuer. LeRobot-Datensätze in v2.0, v2.1 und v3.0 sowie CSV- und JSON- oder JSONL-Dateien funktionieren mit dem Basispaket. HDF5- und MCAP- oder ROS-2-Aufnahmen brauchen Extras, Kameraprüfungen brauchen das Video-Extra, und beliebige HDF5-Strukturen lassen sich womöglich nicht zuordnen. Ein vollständiger Bericht über 1.000 Episoden dauerte in Kalanos' eigenem Lauf etwa 52 Minuten, was laut Kalanos kein Benchmark ist. Es eignet sich für Teams, die Imitation Learning betreiben und die Qualität eines Datensatzes schnell prüfen wollen.
