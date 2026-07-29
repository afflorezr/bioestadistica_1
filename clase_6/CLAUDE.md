# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Context

This is the **Clase 6** deck for Bioestadística Fundamental. See the [parent CLAUDE.md](../CLAUDE.md) for repo-wide conventions (build commands, front matter patterns, R packages, slide authoring).

## Build

```bash
quarto render clase_6/clase_6.qmd   # from repo root
quarto preview clase_6/clase_6.qmd  # live reload
```

## Topic

Probability fundamentals: random experiments (*experimento aleatorio*), sample spaces (*espacio muestral*), and events (*eventos*) — including set operations (union, intersection, complement) illustrated with Venn diagrams.

## Local asset layout

CSS/SCSS files exist at **two levels** in this directory:

- `assets/` — canonical copies referenced in the YAML front matter (`assets/monash.scss`, `assets/custom.css`, etc.)
- Root level — duplicate copies (`monash.scss`, `custom.css`, etc.) that are **not** referenced by the deck; edit only the `assets/` versions.

## Images

Venn diagram images (`venn_*.png/jpg`) and `moneda.jpg` are in `images/`. The deck references them with relative paths (`images/filename`).
