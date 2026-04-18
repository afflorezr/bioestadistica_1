# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Course materials for **Bioestadística Fundamental** (Universidad Nacional de Colombia, Departamento de Estadística, Sede Bogotá). Each class is a Quarto RevealJS presentation written in Spanish.

## Build commands

Render a single presentation to HTML:
```bash
quarto render clase_2/clase_2.qmd
```

Live preview with hot-reload:
```bash
quarto preview clase_2/clase_2.qmd
```

Replace `clase_2/clase_2.qmd` with any `.qmd` file path. The rendered HTML and a `-speaker.html` (presenter notes view) are output in the same directory.

## Repository structure

- `presentacion.qmd` / `clase_1/presentacion.qmd` — instructor introduction slide deck
- `clase_1/clase_1.qmd`, `clase_2/clase_2.qmd`, `clase_3/clase_3.qmd` — per-class lecture decks
- `clases_estefa/` — supplementary materials (PDFs, LaTeX, images) from a co-instructor; not rendered by Quarto
- Each `clase_N/` directory is self-contained with its own `assets/`, `images/`, `referencias.bib`, and `ieee.csl`
- Root-level `assets/` and per-class `assets/` share the same structure (SCSS theme, CSS, FontAwesome)

## Quarto front matter conventions

All decks share this YAML header pattern:

```yaml
format:
  revealjs:
    multiplex: true          # enables presenter/audience split (generates -speaker.html)
    theme: [simple, assets/monash.scss]
    css: [assets/syntax-highlight.css, assets/custom.css, assets/pacman.css]
    logo: images/logo_unal_3.png
    title-slide: false       # first slide is a custom ## heading, not the auto title slide
execute:
  echo: true                 # R code blocks are shown by default
bibliography: referencias.bib
csl: ieee.csl
```

## R packages used

Slides embed R code chunks. Packages in use: `knitr`, `kableExtra`, `ggplot2`. Install with:
```r
install.packages(c("knitr", "kableExtra", "ggplot2"))
```

## Slide authoring patterns

- Slides use raw HTML extensively for layout (`<div class="twocol">`, `<div class="card ...">`)
- Animations use RevealJS fragment classes: `class="fragment fade-up"` with `data-fragment-index`
- The custom `.twocol` layout and card styles are defined in `assets/custom.css`
- Font size is set inline (`style="font-size: 30px;"`) rather than via CSS classes
- Math is written in LaTeX: `$f_i$`, `$\bar{x}$`, etc.
- The logo is hidden on the title slide via an inline `<script>` block in the YAML header (do not remove it)
