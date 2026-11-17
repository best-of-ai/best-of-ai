---
title: 'A Best of AI agora é de código aberto!'
slug: 'best-of-ai-is-now-open-source'
subtitle: 'Um ano selecionando ferramentas de IA — agora o repositório, o ranking e o pipeline de implantação estão no GitHub para todos.'
date: '2026-06-25'
related_categories:
  - ai-directories
related_tools:
  - best-of-ai
i18n_source: 'd8ce6e206afa'
---

Há cerca de um ano, começamos a Best of AI como uma lista selecionada de ferramentas de IA que vale a pena usar. Hoje, o projeto inteiro está [no GitHub e é de código aberto](https://github.com/best-of-ai/best-of-ai): dados, site, scripts e CI. Daqui em diante, a comunidade pode participar.

## Arquivos simples, sem banco de dados

Cada ferramenta é um arquivo Markdown em `content/tools/`. As categorias ficam em `data/categories.yaml`. O [ranking](/leaderboard/) usa os dados de `data/leaderboard.yaml`. Sem Postgres, CMS headless ou dependência de fornecedor. Clone o repositório, use `git grep` para encontrar o que procura e envie um PR quando algo estiver errado. Esse é o modelo.

O site é compilado estaticamente com o [Hugo](https://gohugo.io/). HTML, CSS e um pouco de JavaScript puro. Ao enviar alterações para `main`, uma GitHub Action executa `hugo --minify` e publica o resultado no GitHub Pages. Não há servidor para manter.

## O GitHub Actions cuida das tarefas repetitivas

Três fluxos que vale conhecer:

- **Implantação** — compila e publica a cada envio para `main`
- **Issue → PR** — recebe uma issue de envio de ferramenta com o modelo adequado, valida com `issue-review.py`, abre uma branch e cria um PR
- **Atualizar README** — gera novamente o `README.md` com base nos arquivos de ferramentas sempre que os dados mudam

Envie uma ferramenta por issue ou PR. Corrija uma descrição editando um único arquivo Markdown. Discuta as posições do ranking em `data/leaderboard.yaml`. Tudo pode ser revisado e fica no histórico do Git.

## Ranking, profissões e muito mais

O [ranking](/leaderboard/) é uma seleção classificada de ferramentas que consideramos realmente boas, não apenas populares. As posições vêm dos dados, não de impressões: edite o YAML, abra um PR e explique seu argumento.

As [páginas por profissão](/professionals/) organizam ferramentas por função — desenvolvedores, designers, profissionais de marketing, escritores e mais de 200 outras. Cada arquivo de profissão lista os slugs das categorias; o Hugo seleciona as ferramentas correspondentes automaticamente. Para adicionar uma profissão, basta criar um arquivo Markdown e enviar um PR.

A busca funciona no navegador. O modal no cabeçalho consulta [`/index.json`](/index.json), um índice JSON gerado durante a compilação. Faça um fork dos dados, crie sua própria interface e conecte-a ao que quiser. Não é necessária uma chave de API.

## Venha contribuir

Se você gosta de diretórios no Git, sites estáticos que se publicam sozinhos e projetos para os quais é possível enviar correções, este projeto é para você.

- [Contribuir](/contribute/) — como enviar ferramentas, corrigir listagens e melhorar classificações
- [Repositório no GitHub](https://github.com/best-of-ai/best-of-ai) — clone, explore, corrija e envie um PR

O diretório é gratuito para explorar. O código e os dados são seus para copiar e adaptar. Preferimos cem pessoas melhorando a lista a uma pessoa controlando quem pode contribuir.