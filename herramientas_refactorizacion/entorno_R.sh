#!/usr/bin/env bash

# Biblioteca local y escribible para renderizar el curso sin privilegios de administrador.
CURSO_BIOESTADISTICA="/home/afflorezr/Documents/unal/docencia/cursos/bioestadistica"
LIBRERIA_R_CURSO="${CURSO_BIOESTADISTICA}/.quarto-cache-refactor/R-library"
CACHE_QUARTO_CURSO="${CURSO_BIOESTADISTICA}/.quarto-cache-refactor"
LIBRERIA_R_USUARIO="/home/afflorezr/R/x86_64-pc-linux-gnu-library/4.6"

mkdir -p "${LIBRERIA_R_CURSO}" "${CACHE_QUARTO_CURSO}"
chmod -R u+rwX "${CACHE_QUARTO_CURSO}"

export R_LIBS="${LIBRERIA_R_CURSO}:${LIBRERIA_R_USUARIO}"
export XDG_CACHE_HOME="${CACHE_QUARTO_CURSO}"

instalar_paquetes_r() {
  if [ "$#" -eq 0 ]; then
    echo "Uso: instalar_paquetes_r paquete [paquete ...]" >&2
    return 2
  fi

  Rscript -e '
    paquetes <- commandArgs(trailingOnly = TRUE)
    faltantes <- paquetes[!vapply(paquetes, requireNamespace, logical(1), quietly = TRUE)]
    if (length(faltantes)) {
      install.packages(faltantes, lib = Sys.getenv("R_LIBS") |> strsplit(":") |> unlist() |> head(1), repos = "https://cloud.r-project.org", dependencies = NA)
    }
  ' "$@"
}
