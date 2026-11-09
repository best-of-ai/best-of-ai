---
title: '¡Best of AI ya es de código abierto!'
slug: 'best-of-ai-is-now-open-source'
subtitle: 'Un año eligiendo herramientas de IA a mano. Ahora el repositorio, el ranking y el pipeline de despliegue están en GitHub para quien quiera usarlos.'
date: '2026-06-25'
related_categories:
  - ai-directories
related_tools:
  - best-of-ai
i18n_source: 'd8ce6e206afa'
---

Empezamos Best of AI hace cerca de un año como una lista seleccionada de herramientas de IA que merecen usarse. Hoy todo el proyecto es [código abierto en GitHub](https://github.com/best-of-ai/best-of-ai): datos, sitio, scripts y CI. A partir de aquí lo mueve la comunidad.

## Archivos planos, sin base de datos

Cada herramienta es un archivo Markdown en `content/tools/`. Las categorías viven en `data/categories.yaml`. El [ranking](/leaderboard/) ordena las herramientas a partir de `data/leaderboard.yaml`. No hay Postgres, ni CMS headless, ni dependencia de un proveedor. Clonas el repositorio, haces `git grep` de lo que necesites y envías un PR cuando algo esté mal. Ese es todo el modelo.

El sitio es una build estática de [Hugo](https://gohugo.io/). HTML, CSS y un poco de JS sin frameworks. Un push a `main` lanza una GitHub Action que ejecuta `hugo --minify`, y el resultado acaba en GitHub Pages. No hay un servidor al que cuidar.

## GitHub Actions hace el trabajo aburrido

Hay tres flujos de trabajo que conviene conocer:

- **Deploy**: construye y publica en cada push a `main`
- **Issue → PR**: si abres un issue de envío de herramienta con la plantilla correcta, `issue-review.py` lo valida, abre una rama y crea un PR
- **Update README**: regenera `README.md` a partir de los archivos de herramientas cuando cambian los datos

Envías una herramienta por issue o por PR. Corriges una descripción editando un archivo Markdown. Discutes los puestos del ranking en `data/leaderboard.yaml`. Todo se puede revisar y todo queda en el historial de git.

## Ranking, profesiones y el resto

El [ranking](/leaderboard/) es una lista corta ordenada: herramientas que nos parecen realmente buenas, no solo populares. Los puestos son datos, no una intuición: editas el YAML, abres un PR y argumentas.

Las [páginas de profesiones](/professionals/) agrupan herramientas por oficio: desarrollo, diseño, marketing, redacción y más de 200. Cada archivo de profesión lista slugs de categoría; Hugo trae las herramientas que encajan. Añadir una profesión es igual que añadir una herramienta: archivo Markdown, PR, listo.

La búsqueda ocurre en el navegador. El modal de la cabecera pide [`/index.json`](/index.json), un índice JSON generado al compilar. Puedes bifurcar los datos, construir tu propia interfaz y conectarla a lo que quieras. Sin clave de API.

## Ven a trastear

Si te gustan los directorios que viven en git, los sitios estáticos que se despliegan solos y los directorios a los que de verdad puedes mandar un parche, esto es para ti.

- [Contribuir](/contribute/): cómo enviar herramientas, corregir fichas y mejorar el ranking
- [Repositorio de GitHub](https://github.com/best-of-ai/best-of-ai): clónalo, rómpelo, arréglalo y manda un PR

El directorio se puede consultar gratis. El código y los datos se pueden bifurcar. Preferimos que cien personas mejoren la lista a que una sola decida quién entra.
