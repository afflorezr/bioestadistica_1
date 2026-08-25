#!/usr/bin/env python3
"""Genera variantes modulares de la clase 1 sin modificar el original.

Reutiliza el motor (generate_class) y los diccionarios de sustitución de
refactor_clases_4_20.py en vez de duplicarlos.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import refactor_clases_4_20 as base  # noqa: E402


def main() -> None:
    manifest: list[list[str]] = []
    base.generate_class(1, manifest)
    manifest_path = base.ROOT / "MAPA_MODULOS_CLASE_1.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["clase", "indice", "seccion", "tipo", "archivo"])
        writer.writerows(manifest)
    print(f"Mapa escrito en {manifest_path}")


if __name__ == "__main__":
    main()
