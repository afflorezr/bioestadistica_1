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

## Repository Structure

```text
bioestadistica_1/              # Course materials for Bioestadistica Fundamental
├── CLAUDE.md                  # Guidance for Claude Code when editing this repo
├── presentacion.qmd           # Instructor introduction slide deck
├── presentacion.html          # Rendered introduction deck
├── referencias.bib            # Shared bibliography
├── ieee.csl                   # Shared citation style
├── plan_asignatura.pdf        # Official course plan
├── assets/                    # Shared RevealJS/Quarto theme assets
│   ├── custom.css             # Custom slide layout and component styles
│   ├── monash.scss            # Main RevealJS theme
│   ├── kdd.scss               # Alternate RevealJS theme
│   ├── pacman.css             # Extra CSS utilities
│   ├── syntax-highlight.css   # Code highlighting styles
│   └── fontawesome-free-6.1.1-web/ # Font Awesome vendor files
├── images/                    # Shared logos and course graphics
├── clase_N/                   # One directory per class session (N = 1..11)
│   ├── clase_N.qmd            # Main Quarto RevealJS slide deck
│   ├── clase_N.html           # Rendered student-facing slides
│   ├── clase_N-speaker.html   # Rendered presenter notes view
│   ├── clase_N_files/         # Quarto generated assets for rendered slides
│   ├── images/                # Class-specific figures and logos
│   ├── assets/                # Class-local style/vendor assets when needed
│   ├── referencias.bib        # Class-local bibliography
│   └── ieee.csl               # Class-local citation style
├── clases_estefa/             # Supplementary co-instructor materials, use this book as knowledge source
│   ├── clase_*/               # Legacy LaTeX/PDF class files and figures
│   └── talleres/              # Practice workshop materials
├── libro_inferencia/          # Quarto book project for inference notes, use this book as knowledge source
├── prob_inf/                  # External probability and inference Quarto book, use this book as knowledge source
└── .claude/                   # Local Claude settings
```

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

Slides embed R code chunks. Packages in use: `knitr`, `kableExtra`, `ggplot2`,`tidyverse`. Install with:
```r
install.packages(c("knitr", "kableExtra", "ggplot2","tidyverse"))
```

### Mandatory Slide Structure

Each class must include:

1. Motivation / problem context
2. Conceptual explanation (intuitive)
3. Applied example in colombian agricultural field (realistic dataset or scenario)
4. Code implementation (Python and/or R when appropriate)
5. Interpretation of results
6. Common mistakes
7. Practice exercise

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

### Style Constraints

- Write in Spanish
- Use clear, concise academic language
- Avoid verbosity
- Prioritize clarity over completeness
