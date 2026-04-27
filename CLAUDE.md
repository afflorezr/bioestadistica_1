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

## Slide de Contenido (obligatorio)

**Toda clase debe tener un slide de Contenido inmediatamente después del slide de título.** El slide usa un grid de dos columnas con los temas de la clase, animados con `fragment fade-in`. Estructura exacta:

```html
## Contenido

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 42px; margin-top: 20px; font-size: 30px; align-items: start;">
<div>
<h3 class="fragment fade-in" data-fragment-index="1" style="font-size: 34px; margin-bottom: 14px; color: #1b4d2e;">Parte I: Nombre de la parte</h3>
<ul>
<li class="fragment fade-in" data-fragment-index="2">Tema 1.</li>
<li class="fragment fade-in" data-fragment-index="3">Tema 2.</li>
<li class="fragment fade-in" data-fragment-index="4">Tema 3.</li>
</ul>
</div>

<div>
<h3 class="fragment fade-in" data-fragment-index="5" style="font-size: 34px; margin-bottom: 14px; color: #1a3a6b;">Parte II: Nombre de la parte</h3>
<ul>
<li class="fragment fade-in" data-fragment-index="6">Tema 4.</li>
<li class="fragment fade-in" data-fragment-index="7">Tema 5.</li>
<li class="fragment fade-in" data-fragment-index="8">Tema 6.</li>
</ul>
</div>
</div>
```

Reglas:
- El encabezado es siempre `## Contenido` (sin clases adicionales).
- El grid es siempre `1fr 1fr` con `gap: 42px`, `margin-top: 20px`, `font-size: 30px`, `align-items: start`.
- Los `<h3>` usan `font-size: 34px` y `margin-bottom: 14px`. Color verde `#1b4d2e` para la primera columna, azul `#1a3a6b` para la segunda.
- Si la clase tiene una sola parte temática, se puede usar una sola columna (pero se mantiene el mismo `<div>` externo con el `display: grid`).
- Los `data-fragment-index` son consecutivos de 1 en adelante.

## Slide authoring patterns

- Slides use raw HTML extensively for layout (`<div class="twocol">`, `<div class="card ...">`)
- Animations use RevealJS fragment classes: `class="fragment fade-up"` with `data-fragment-index`
- The custom `.twocol` layout and card styles are defined in `assets/custom.css`
- Font size is set inline (`style="font-size: 30px;"`) rather than via CSS classes
- Math is written in LaTeX: `$f_i$`, `$\bar{x}$`, etc.
- The logo is hidden on the title slide via an inline `<script>` block in the YAML header (do not remove it)
- **Slide titles NEVER use hyphens (`-`) or em dashes (`—`) to separate words or phrases.** Use a colon (`:`) or restructure the title. Correct: `## Ejemplo: Boxplot`. Wrong: `## Ejemplo — Boxplot` or `## Ejemplo - Boxplot`.
- Slide titles must always be non-empty (`##` with no text is forbidden). Every slide needs a descriptive `## Título` heading.

## Block color convention

All blocks follow the Beamer-style pattern defined in `assets/monash.scss`. Each block has a `.block-title` header and a `.block-body` content area. Structure:

```html
<div class="block-TIPO fragment fade-up" data-fragment-index="1">
  <div class="block-title">Etiqueta: Nombre</div>
  <div class="block-body">
    Contenido del bloque...
  </div>
</div>
```

### Color assignments

| Clase CSS | Color | Usar para |
|---|---|---|
| `block-theorem` | **Azul** (`#1a3a6b` título, `#dce9f7` cuerpo) | Teoremas |
| `block-lemma` | **Azul** (igual que teorema) | Lemas |
| `block-corollary` | **Azul** (igual que teorema) | Corolarios |
| `block-proposition` | **Azul** (igual que teorema) | Proposiciones |
| `block-definition` | **Verde** (`#1b4d2e` título, `#d6f0dd` cuerpo) | Definiciones |
| `block-example` | **Verde claro** (variante más clara que definición) | Ejemplos prácticos |
| `block-alert` / `block-warning` | **Rojo** (`#7a1515` título, `#fad8d8` cuerpo) | Advertencias, conceptos clave |
| `block-proof` | **Gris** (`#374151` título, `#f3f4f6` cuerpo) | Demostraciones (agrega ∎ al final automáticamente) |
| `block-note` | **Azul UNAL** (borde izquierdo `#006DAE`, fondo `#e8f4f8`) | Notas y observaciones sin título |

### Regla mnemotécnica

- **Azul** → resultados formales (teoremas, lemas, corolarios, proposiciones)
- **Verde** → definiciones y ejemplos
- **Rojo** → alertas y advertencias
- **Gris** → demostraciones
- **Azul UNAL** → notas y observaciones informales
