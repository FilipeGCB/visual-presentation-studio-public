# Visual Presentation Studio

**Sistema local-first para projetar, construir, renderizar, inspecionar e validar apresentações e narrativas visuais de alta qualidade com workflows assistidos por IA.**

**EN:** A local-first engineering system for designing, building, rendering, inspecting, and validating high-quality AI-assisted presentations and visual narratives.

[English version](README.en.md)

## Em 10 segundos

O Visual Presentation Studio trata uma apresentação como um **produto de engenharia visual**, não como uma sequência de slides gerada por um modelo.

Ele organiza o ciclo completo: tese, narrativa, direção visual, assets, implementação, renderização real no navegador, inspeção, correção e QA antes de considerar uma entrega final.

> **Princípio central:** a complexidade pode variar; o rigor de produção não.

## Por que existe

Geradores de apresentação podem produzir algo visualmente aceitável rapidamente, mas isso não garante coerência narrativa, qualidade de layout, legibilidade, comportamento responsivo ou consistência entre versões.

O Studio existe para separar **geração** de **validação** e transformar produção visual em um processo reproduzível e revisável.

## Diferenciais

- ciclo de produção com **dois gates explícitos**;
- renderização e inspeção do resultado real, não apenas validação de código;
- QA separado em conteúdo, narrativa, visual, experiência e técnica;
- suporte a apresentações 16:9, scrollytelling, experiências exploratórias e híbridos deliberados;
- entrega local/downloadable como saída de primeira classe;
- exemplos e metodologia públicos sanitizados, sem expor entregas privadas.

## Lifecycle

```text
brief → proposta → Gate 1 → storyboard/specs → build → render/inspect/correct → QA → Gate 2 → FINAL → aprendizado controlado opcional
```

- **Gate 1:** congela tese, narrativa principal, formato, direção visual, interação principal, stack e destino antes da implementação.
- **Gate 2:** aprova o build exato somente depois de inspeção renderizada e ausência de issues conhecidas BLOCKER ou MAJOR.

## Estado atual

**Desenvolvimento ativo.** A rota de produção atual prioriza **qualidade visual, reprodutibilidade e reviewabilidade**, não latência mínima ou menor custo de tokens.

Um caminho futuro pode explorar um modo rápido de rascunho, mas **Fast/Draft mode não é apresentado aqui como capacidade existente**.

## Como explorar

O repositório público contém metodologia, skill operacional, patterns, templates, regras de qualidade, exemplos sintéticos/sanitizados e testes.

```text
skill/visual-presentation-studio/   Skill operacional
methodology/                        contratos e raciocínio duráveis
quality/                            regras observáveis de QA
patterns/                           padrões positivos e negativos
templates/                          starters técnicos/local-first
examples/                           evidências sintéticas ou sanitizadas
```

## Validação

A partir da raiz:

```bash
python -m unittest discover -s tests -v
python scripts/validate_repo.py
python scripts/public_safety_check.py .
cd templates/exploratory-react && npm install && npm run build
```

Sucesso automatizado é necessário, mas não suficiente: a apresentação final continua exigindo **inspeção visual renderizada**.

## O que é público aqui

Esta distribuição é propositalmente menor e mais segura que o laboratório privado. Ela contém capacidade reutilizável e documentação generalizada, não apresentações reais confidenciais, material bruto de projeto ou evidência operacional privada.

Aprendizados provenientes de trabalho privado só entram aqui quando podem ser generalizados e sanitizados de forma segura.

## Aplicação real

O blog pessoal do autor é um dos ambientes reais usados para aplicar e refinar princípios do Studio — da direção narrativa e composição visual ao QA renderizado. Isso demonstra uso iterativo, não geração one-shot automática do site inteiro.

## Limites

Este repositório não promete geração instantânea perfeita, não substitui revisão editorial/visual e não publica o laboratório privado completo.

Veja também `SECURITY.md` e `AGENTS.md` antes de contribuir.

## Direitos de uso

Este repositório é público para portfólio e estudo. Visibilidade pública **não concede automaticamente uma licença open source**. Se uma licença for adicionada no futuro, o arquivo correspondente definirá os termos aplicáveis.
