---
title: 'DVC'
name: 'DVC'
subtitle: 'Control de versiones de código abierto para conjuntos de datos y experimentos de ML'
slug: 'dvc'
description: 'DVC, siglas de Data Version Control, es una herramienta de código abierto para versionar conjuntos de datos, modelos y experimentos junto al código en Git. Hace seguimiento de archivos grandes almacenados en la nube con una interfaz similar a la de Git.'
website: 'https://dvc.org'
logo_url: ''
category: 'devtools'
category_name: 'Herramientas para desarrolladores'
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
i18n_source: '18847a8c544f'
---

DVC resuelve un problema para el que Git no se diseñó: los archivos de datos grandes. Quienes trabajan con datos siguen conjuntos de datos y archivos de modelos con DVC, que guarda pequeños archivos de referencia en Git y deja los datos reales en almacenamiento local o en la nube, como S3 o Google Cloud Storage. Al volver a un commit antiguo, recupera los datos que le corresponden.

También admite pipelines reproducibles. Se definen etapas que toman datos y código como entradas y generan salidas, y DVC vuelve a ejecutar solo lo que ha cambiado. Los experimentos se pueden registrar y comparar, y las métricas y los gráficos se guardan con el repositorio. Hoy el proyecto lo mantiene lakeFS.

DVC es gratuito y de código abierto. Exige cierta soltura con Git y la línea de comandos. Entre las alternativas están lakeFS, Git LFS para casos más simples, MLflow, Weights & Biases Artifacts y Pachyderm. DVC encaja con científicos de datos que quieren control de versiones para sus datos.
