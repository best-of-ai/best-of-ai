---
title: 'DVC'
name: 'DVC'
subtitle: 'Open-source version control for ML datasets and experiments'
slug: 'dvc'
description: 'DVC, short for Data Version Control, is an open-source tool for versioning datasets, models, and experiments alongside code in Git. It tracks large files stored in cloud storage using a Git-like interface.'
website: 'https://dvc.org'
logo_url: ''
category: 'devtools'
category_name: 'DevTools'
price: 'Free'
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
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, open_source, cloud_based, machine_learning]
---

DVC solves a problem Git was not designed for: large data files. Data scientists track datasets and model files with DVC, which stores small pointer files in Git and keeps the actual data in cloud or local storage such as S3 or Google Cloud Storage. Checking out an old commit retrieves the matching data.

It also supports reproducible pipelines. Users define stages that take data and code as inputs and produce outputs, and DVC reruns only what changed. Experiments can be tracked and compared, and metrics and plots are stored with the repository. The project is now maintained under lakeFS.

DVC is free and open source. It requires comfort with Git and the command line. Alternatives include lakeFS, Git LFS for simpler cases, MLflow, Weights & Biases Artifacts, and Pachyderm. DVC suits data scientists who want version control for data.
