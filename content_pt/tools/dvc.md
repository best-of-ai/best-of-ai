---
title: 'DVC'
name: 'DVC'
subtitle: "Controle de versão de código aberto para conjuntos de dados e experimentos de aprendizado de máquina"
slug: 'dvc'
description: "DVC, abreviação de Data Version Control, é uma ferramenta de código aberto para versionar conjuntos de dados, modelos e experimentos junto com o código no Git. Acompanha arquivos grandes armazenados na nuvem usando uma interface semelhante ao Git."
website: 'https://dvc.org'
logo_url: ''
category: 'devtools'
category_name: "Ferramentas para desenvolvedores"
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

DVC resolve um problema para o qual o Git não foi projetado: arquivos de dados grandes. Cientistas de dados acompanham conjuntos de dados e arquivos de modelos com DVC, que armazena pequenos arquivos de referência no Git e mantém os dados reais na nuvem ou em armazenamento local, como S3 ou Google Cloud Storage. Ao selecionar um commit antigo, recuperam-se os dados correspondentes.

A ferramenta também oferece suporte a pipelines reproduzíveis. Usuários definem etapas que recebem dados e código como entrada e produzem saídas; DVC executa novamente apenas as etapas que mudaram. Experimentos podem ser acompanhados e comparados, e métricas e gráficos são armazenados com o repositório. O projeto agora é mantido sob o lakeFS.

DVC é gratuito e de código aberto. É necessário ter familiaridade com Git e linha de comando. Entre as alternativas estão lakeFS, Git LFS para casos mais simples, MLflow, Weights & Biases Artifacts e Pachyderm. DVC é indicado para cientistas de dados que querem controle de versão para dados.
