---
title: DVC
name: DVC
subtitle: Open-Source-Versionsverwaltung für ML-Datensätze und Experimente
slug: dvc
description: DVC (Data Version Control) ist ein Open-Source-Werkzeug zur Versionsverwaltung von Datensätzen, Modellen und
  Experimenten zusammen mit Git-Code. Große Dateien in Cloudspeichern lassen sich über eine Git-ähnliche Oberfläche verfolgen.
website: https://dvc.org
logo_url: ''
category: devtools
category_name: Entwicklertools
price: Free
featured: false
rank: 5
alternatives:
- mlflow
- zenml
- metaflow
- clearml
- comet-ml
- weights-biases
- prefect
date: '2025-06-15'
tags:
- developer_tools
- code_generation
- infrastructure
- deployment
- development
- devops
- ci_cd
- cloud
- api
- open_source
- cloud_based
- machine_learning
i18n_source: '18847a8c544f'
---

DVC löst ein Problem, für das Git nicht ausgelegt ist: große Datendateien. Datenwissenschaftler:innen verwalten Datensätze und Modelldateien mit DVC. Kleine Verweisdateien liegen in Git, während die eigentlichen Daten lokal oder in Speichern wie S3 und Google Cloud Storage abgelegt werden. Beim Wechsel zu einem älteren Commit werden die zugehörigen Daten abgerufen.

DVC unterstützt außerdem reproduzierbare Pipelines. Nutzer:innen definieren Schritte mit Eingabedaten und Code sowie den daraus erzeugten Ausgaben; DVC führt nur geänderte Schritte erneut aus. Experimente lassen sich verfolgen und vergleichen, Kennzahlen und Diagramme werden im Repository gespeichert. Das Projekt wird inzwischen unter lakeFS gepflegt.

DVC ist kostenlos und quelloffen. Die Nutzung setzt Vertrautheit mit Git und der Kommandozeile voraus. Alternativen sind lakeFS, Git LFS für einfachere Fälle, MLflow, Weights & Biases Artifacts und Pachyderm. DVC eignet sich für Datenwissenschaftler:innen, die Daten versionieren möchten.
