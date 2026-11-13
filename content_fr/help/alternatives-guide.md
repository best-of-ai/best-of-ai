---
title: 'Alternatives : suggestions et qualité'
slug: 'alternatives-guide'
subtitle: 'Comment les pages de comparaison se construisent, et comment en proposer une.'
order: 3
i18n_source: 'dc055f116fcc'
---

## Ce que « alternatives » veut dire ici

Chaque page d'outil peut lister une poignée d'alternatives : d'autres outils qui traitent le même problème de façon proche. Best of AI transforme cette liste en une page dédiée, à `/alternatives/<tool>/`. Tu es sur un créateur de sites web, tu vois tout de suite des options proches à côté.

## Comment un outil devient une alternative listée

Les alternatives se choisissent selon la catégorie et l'usage, pas selon la taille de la marque. Un outil n'est listé comme alternative d'un autre que s'il vise vraiment le même travail. Une app de prise de notes n'a rien à faire à côté d'un éditeur vidéo juste parce que les deux utilisent l'IA.

## Comment en proposer une

La liste d'alternatives vit dans le fichier de l'outil, dans un champ `alternatives:` qui pointe vers d'autres slugs d'outils. Pour proposer un ajout ou une correction, ouvre un pull request sur [GitHub](https://github.com/best-of-ai/best-of-ai) qui modifie ce champ, ou ouvre un issue qui décrit l'outil et l'alternative que tu as en tête.

## Le seuil de qualité

Une alternative n'est ajoutée que si elle passe le même seuil que n'importe quel autre outil du site : elle doit marcher, faire ce qu'elle annonce, et valoir qu'on y passe du temps. Les sites morts, les outils hors catégorie et les surcouches bâclées ne passent pas, même en tant qu'« alternative ».

## Comment la page fonctionne

Rien n'est monté à la main page par page. `/alternatives/<slug>/` est généré tout seul à partir du champ `alternatives:` dans le fichier de chaque outil. Tu ajoutes le champ, et la page, avec une section « alternatives à X » sur la page de l'outil, apparaît à la prochaine construction du site.
