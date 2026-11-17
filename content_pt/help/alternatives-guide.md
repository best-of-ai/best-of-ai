---
title: 'Alternativas: sugestões e qualidade'
slug: 'alternatives-guide'
subtitle: 'Como são criadas as páginas de comparação de alternativas e como sugerir uma.'
order: 3
i18n_source: 'dc055f116fcc'
---

## O que significa “alternativas” aqui

Cada página de ferramenta pode listar algumas alternativas: outras ferramentas que resolvem o mesmo problema de forma semelhante. A Best of AI transforma essa lista em uma página própria em `/alternatives/<tool>/`; assim, se você estiver consultando um criador de sites, pode ver opções parecidas ao lado.

## Como uma ferramenta vira uma alternativa listada

As alternativas são escolhidas por categoria e caso de uso, não pelo tamanho da marca. Uma ferramenta só é listada como alternativa a outra quando realmente concorre pela mesma tarefa. Um aplicativo de anotações não combina com um editor de vídeo só porque ambos usam IA.

## Como sugerir uma alternativa

A lista de alternativas fica no arquivo da própria ferramenta, no campo `alternatives:`, que aponta para os slugs de outras ferramentas. Para sugerir uma inclusão ou correção, abra um pull request no [GitHub](https://github.com/best-of-ai/best-of-ai) que edite esse campo ou abra uma issue descrevendo a ferramenta e a alternativa em questão.

## O padrão de qualidade

Uma alternativa só é adicionada se atender ao mesmo padrão das demais ferramentas do site: precisa funcionar, cumprir o que promete e valer o tempo de alguém. Sites desativados, ferramentas fora da categoria e interfaces simples sobre a API de terceiros não entram, mesmo que estejam em alta em outros lugares.

## Como a página funciona

Nenhuma página é montada manualmente. `/alternatives/<slug>/` é gerada automaticamente com base no campo `alternatives:` no arquivo de cada ferramenta. Adicione o campo e, na próxima compilação do site, aparecerão a página e uma seção correspondente “alternativas a X” na própria página da ferramenta.