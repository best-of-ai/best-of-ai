---
title: 'Como o site funciona'
slug: 'how-the-site-works'
subtitle: 'Hugo, arquivos simples e um pipeline do GitHub Actions. Sem banco de dados.'
order: 8
i18n_source: '2f8d3f5e4878'
---

## Sem banco de dados, apenas arquivos

Cada ferramenta é um arquivo Markdown em `content/tools/`. Cada categoria fica em `data/categories.yaml`. Não há painel administrativo nem back-end para gerenciar: o site inteiro consiste em arquivos simples em um repositório Git. Tudo é compilado com o [Hugo](https://gohugo.io/), um gerador de sites estáticos, para produzir HTML.

## O que o GitHub Actions faz

Três fluxos cuidam das tarefas repetitivas:

- **Implantação** compila e publica o site a cada envio para `main`.
- **Issue para PR** analisa automaticamente issues de envio de ferramentas e abre um pull request para as que seguem o formato.
- **Atualizar README** gera novamente o `README.md` sempre que os dados das ferramentas mudam.

## Por que foi construído assim

Arquivos simples permitem que qualquer pessoa clone o repositório e veja exatamente o que está no site e por quê. Não há um banco de dados oculto em que seja preciso confiar; os dados estão no mesmo arquivo que você editaria para corrigir algo.

## Consulte o código

Todo o código-fonte, os modelos do site, os scripts e os dados estão publicamente disponíveis em [github.com/best-of-ai/best-of-ai](https://github.com/best-of-ai/best-of-ai).