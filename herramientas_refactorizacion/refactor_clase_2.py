#!/usr/bin/env python3
"""Regenera el piloto de clase_2 conservando íntegro el original de Agronomía."""

from pathlib import Path
import hashlib


ROOT = Path(__file__).resolve().parents[1]
CLASS = ROOT / "clase_2"
ORIGINAL = CLASS / "clase_2.qmd"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lines_range(lines: list[str], first: int, last: int) -> str:
    """Devuelve un rango inclusivo usando numeración humana desde uno."""
    return "".join(lines[first - 1:last])


def zootecnia(block: int, text: str) -> str:
    if block == 1:
        changes = {
            "alturas de plantas (en cm) de 100 cultivos de maíz evaluados por estudiantes en un ensayo experimental": "pesos vivos (en kg) de 100 cerdos evaluados en un ejercicio simulado",
            "Las alturas son datos continuos, ya que la altura se mide": "Los pesos son datos continuos, ya que el peso se mide",
            "cuántas alturas caen": "cuántos pesos caen",
            "El intervalo con la mayor frecuencia absoluta es [66-68), con 40 plantas de maíz": "El intervalo con la mayor frecuencia absoluta es [66-68), con 40 cerdos",
            "El 80% de las plantas tienen alturas menores a 70 cm": "El 80% de los cerdos tiene pesos menores a 70 kg",
            "20% restante tienen alturas mayores a 70 cm": "20% restante tiene pesos mayores a 70 kg",
            "La distribución de las alturas": "La distribución de los pesos",
            "la mayoría de las plantas se encuentran": "la mayoría de los cerdos se encuentra",
            "amplitud de 2 cm": "amplitud de 2 kg",
            "60 cm": "60 kg",
            "62 cm": "62 kg",
        }
    elif block == 2:
        changes = {
            "Rendimiento de cultivos (ton/ha) en una finca.": "Ganancia diaria de peso (kg/día) en cuatro lotes de cerdos.",
            'cultivos <- c("Maíz", "Arroz", "Trigo", "Café")': 'lotes <- c("Lote A", "Lote B", "Lote C", "Lote D")',
            "rendimiento <- c(4.5, 5.2, 3.8, 2.1)": "ganancia <- c(0.65, 0.72, 0.68, 0.75)",
            "cultivo = cultivos": "lote = lotes",
            "rendimiento = rendimiento": "ganancia = ganancia",
            "aes(x = cultivo, y = rendimiento, fill = cultivo)": "aes(x = lote, y = ganancia, fill = lote)",
            'title = "Rendimiento por cultivo"': 'title = "Ganancia diaria de peso por lote"',
            'x = "Cultivos"': 'x = "Lotes"',
            'y = "Toneladas por hectárea"': 'y = "kg por día"',
            "Altura de las plantas.": "Peso vivo de los cerdos.",
            "Uso del suelo": "Composición de la dieta",
            "uso_suelo <- c(50, 30, 15, 5)": "proporcion_dieta <- c(50, 30, 15, 5)",
            'tipos <- c("Cultivo", "Pastoreo", "Bosque", "Otros")': 'componentes <- c("Forraje", "Concentrado", "Suplemento", "Otros")',
            "df <- data.frame(tipos, uso_suelo)": "df <- data.frame(componentes, proporcion_dieta)",
            "aes(x = 2, y = uso_suelo, fill = tipos)": "aes(x = 2, y = proporcion_dieta, fill = componentes)",
            "paste0(uso_suelo, \"%\")": "paste0(proporcion_dieta, \"%\")",
            'title = "Distribución del uso del suelo"': 'title = "Composición simulada de la dieta"',
            "Producción anual de maíz.": "Producción anual de leche.",
            "produccion <- c(10, 12, 15, 14, 18)": "leche <- c(10, 12, 15, 14, 18)",
            "df <- data.frame(años, produccion)": "df <- data.frame(años, leche)",
            "aes(x = años, y = produccion)": "aes(x = años, y = leche)",
            "aes(label = produccion)": "aes(label = leche)",
            'title = "Producción de maíz por año"': 'title = "Producción simulada de leche por año"',
            'y = "Toneladas"': 'y = "Miles de litros"',
            "como en las ciencias agrarias": "como en las ciencias pecuarias",
        }
    elif block == 3:
        changes = {
            "altura (en cm) de 100 plantas de maíz en condiciones uniformes de suelo, riego y fertilización": "peso vivo (en kg) de 100 cerdos bajo un manejo alimentario uniforme",
            "altura <- rnorm(100, mean = 150, sd = 10)": "peso <- rnorm(100, mean = 150, sd = 10)",
            "df <- data.frame(altura)": "df <- data.frame(peso)",
            "aes(x = altura)": "aes(x = peso)",
            'title = "Distribución de la altura de plantas de maíz"': 'title = "Distribución simulada del peso de cerdos"',
            'x = "Altura (cm)"': 'x = "Peso vivo (kg)"',
            "La mayoría de las plantas tienen alturas cercanas a 150 cm.": "La mayoría de los cerdos tiene pesos cercanos a 150 kg.",
            "crecimiento uniforme": "pesos relativamente homogéneos",
            "Hay pocas plantas muy pequeñas o muy grandes.": "Hay pocos animales con pesos muy bajos o muy altos.",
            "Esto sugiere que el cultivo está en condiciones homogéneas.": "En estos datos simulados, el lote presenta una dispersión moderada.",
            "Ingresos de una muestra de 80 personas de una empresa.": "Costos simulados de tratamientos veterinarios en un lote de animales.",
            "ingresos <-": "costos <-",
            "data.frame(ingresos)": "data.frame(costos)",
            "aes(x = ingresos)": "aes(x = costos)",
            "mean(ingresos)": "mean(costos)",
            'title = "Distribución de ingresos"': 'title = "Distribución simulada de costos veterinarios"',
            'x = "Ingresos"': 'x = "Costo (miles de pesos)"',
            "Producción de un cultivo (toneladas por hectárea), donde la mayoría de los terrenos tiene alta producción, pero algunos presentan rendimientos bajos": "Producción diaria de leche (litros), donde la mayoría de los animales presenta producción alta, pero algunos tienen valores bajos",
            "produccion <-": "leche <-",
            "data.frame(produccion)": "data.frame(leche)",
            "aes(x = produccion)": "aes(x = leche)",
            "mean(produccion)": "mean(leche)",
            'title = "Producción de cultivo"': 'title = "Producción simulada de leche"',
            'x = "Toneladas"': 'x = "Litros por día"',
            "producciones altas": "producciones de leche altas",
            "la mayoría de los cultivos tiene buen rendimiento": "la mayoría de los animales presenta producción alta",
            "como la agronomía": "como la zootecnia",
        }
    else:
        changes = {
            "peso de la mazorca (g)": "peso vivo de cerdos (kg)",
            "30 plantas de maíz": "30 cerdos",
            "mayor cantidad de mazorcas": "mayor cantidad de animales",
            "porcentaje de plantas produjo mazorcas con peso": "porcentaje de animales presentó peso",
        }
    for old, new in changes.items():
        text = text.replace(old, new)
    return text


def economia(block: int, text: str) -> str:
    if block == 1:
        changes = {
            "alturas de plantas (en cm) de 100 cultivos de maíz evaluados por estudiantes en un ensayo experimental": "precios unitarios (en miles de pesos) de 100 productos observados en un ejercicio simulado",
            "Las alturas son datos continuos, ya que la altura se mide": "Los precios son datos continuos, ya que su valor se mide",
            "cuántas alturas caen": "cuántos precios caen",
            "El intervalo con la mayor frecuencia absoluta es [66-68), con 40 plantas de maíz": "El intervalo con la mayor frecuencia absoluta es [66-68), con 40 productos",
            "El 80% de las plantas tienen alturas menores a 70 cm": "El 80% de los productos tiene precios menores a 70 mil pesos",
            "20% restante tienen alturas mayores a 70 cm": "20% restante tiene precios mayores a 70 mil pesos",
            "La distribución de las alturas": "La distribución de los precios",
            "la mayoría de las plantas se encuentran": "la mayoría de los productos se encuentra",
            "amplitud de 2 cm": "amplitud de 2 mil pesos",
            "60 cm": "60 mil pesos",
            "62 cm": "62 mil pesos",
        }
    elif block == 2:
        changes = {
            "Rendimiento de cultivos (ton/ha) en una finca.": "Ventas mensuales (millones de pesos) en cuatro sectores. Datos simulados.",
            'cultivos <- c("Maíz", "Arroz", "Trigo", "Café")': 'sectores <- c("Comercio", "Industria", "Servicios", "Construcción")',
            "rendimiento <- c(4.5, 5.2, 3.8, 2.1)": "ventas <- c(4.5, 5.2, 3.8, 2.1)",
            "cultivo = cultivos": "sector = sectores",
            "rendimiento = rendimiento": "ventas = ventas",
            "aes(x = cultivo, y = rendimiento, fill = cultivo)": "aes(x = sector, y = ventas, fill = sector)",
            'title = "Rendimiento por cultivo"': 'title = "Ventas simuladas por sector"',
            'x = "Cultivos"': 'x = "Sectores"',
            'y = "Toneladas por hectárea"': 'y = "Millones de pesos"',
            "Altura de las plantas.": "Precio unitario de productos.",
            "Uso del suelo": "Composición del gasto del hogar",
            "uso_suelo <- c(50, 30, 15, 5)": "proporcion_gasto <- c(50, 30, 15, 5)",
            'tipos <- c("Cultivo", "Pastoreo", "Bosque", "Otros")': 'rubros <- c("Alimentos", "Vivienda", "Transporte", "Otros")',
            "df <- data.frame(tipos, uso_suelo)": "df <- data.frame(rubros, proporcion_gasto)",
            "aes(x = 2, y = uso_suelo, fill = tipos)": "aes(x = 2, y = proporcion_gasto, fill = rubros)",
            "paste0(uso_suelo, \"%\")": "paste0(proporcion_gasto, \"%\")",
            'title = "Distribución del uso del suelo"': 'title = "Composición simulada del gasto"',
            "Producción anual de maíz.": "Índice de precios anual.",
            "produccion <- c(10, 12, 15, 14, 18)": "indice <- c(100, 102, 105, 104, 108)",
            "df <- data.frame(años, produccion)": "df <- data.frame(años, indice)",
            "aes(x = años, y = produccion)": "aes(x = años, y = indice)",
            "aes(label = produccion)": "aes(label = indice)",
            'title = "Producción de maíz por año"': 'title = "Índice de precios simulado por año"',
            'y = "Toneladas"': 'y = "Índice (base 2018 = 100)"',
            "como en las ciencias agrarias": "como en las ciencias económicas",
        }
    elif block == 3:
        changes = {
            "altura (en cm) de 100 plantas de maíz en condiciones uniformes de suelo, riego y fertilización": "precio (en miles de pesos) de 100 productos comparables en un mercado simulado",
            "altura <- rnorm(100, mean = 150, sd = 10)": "precio <- rnorm(100, mean = 150, sd = 10)",
            "df <- data.frame(altura)": "df <- data.frame(precio)",
            "aes(x = altura)": "aes(x = precio)",
            'title = "Distribución de la altura de plantas de maíz"': 'title = "Distribución simulada de precios"',
            'x = "Altura (cm)"': 'x = "Precio (miles de pesos)"',
            "La mayoría de las plantas tienen alturas cercanas a 150 cm.": "La mayoría de los productos tiene precios cercanos a 150 mil pesos.",
            "crecimiento uniforme": "precios relativamente homogéneos",
            "Hay pocas plantas muy pequeñas o muy grandes.": "Hay pocos productos con precios muy bajos o muy altos.",
            "Esto sugiere que el cultivo está en condiciones homogéneas.": "En estos datos simulados, los precios presentan dispersión moderada.",
            "Ingresos de una muestra de 80 personas de una empresa.": "Ingresos simulados de una muestra de hogares.",
            "Producción de un cultivo (toneladas por hectárea), donde la mayoría de los terrenos tiene alta producción, pero algunos presentan rendimientos bajos": "Ventas mensuales (millones de pesos), donde la mayoría de las unidades presenta valores altos, pero algunas registran valores bajos",
            "produccion <-": "ventas <-",
            "data.frame(produccion)": "data.frame(ventas)",
            "aes(x = produccion)": "aes(x = ventas)",
            "mean(produccion)": "mean(ventas)",
            'title = "Producción de cultivo"': 'title = "Ventas mensuales simuladas"',
            'x = "Toneladas"': 'x = "Millones de pesos"',
            "producciones altas": "ventas altas",
            "la mayoría de los cultivos tiene buen rendimiento": "la mayoría de las unidades presenta ventas altas",
            "como la agronomía": "como la economía",
        }
    else:
        changes = {
            "peso de la mazorca (g)": "gasto mensual en alimentos (miles de pesos)",
            "30 plantas de maíz": "30 hogares",
            "mayor cantidad de mazorcas": "mayor cantidad de hogares",
            "porcentaje de plantas produjo mazorcas con peso": "porcentaje de hogares presentó gasto",
        }
    for old, new in changes.items():
        text = text.replace(old, new)
    return text


def yaml_for(context: str, original_yaml: str) -> str:
    label = {"agronomia": "Agronomía", "zootecnia": "Zootecnia", "economia": "Economía"}[context]
    yaml = original_yaml.replace('title: "Bioestadística Fundamental"', f'title: "Bioestadística, {label}"', 1)
    yaml = yaml.replace(f'title: "Bioestadística, {label}"\n', f'title: "Bioestadística, {label}"\nsubtitle: "Presentación tabular y gráfica"\n', 1)
    yaml = yaml.replace("bibliography: referencias.bib\n", "bibliography: ../referencias.bib\n", 1)
    yaml = yaml.replace("csl: ieee.csl\n", f"csl: ../ieee.csl\noutput-file: clase_2_{context}.html\n", 1)
    yaml = yaml.replace("logo: images/", "logo: ../images/", 1)
    yaml = yaml.replace("../assets/", "../../assets/")
    return yaml


def main_file(context: str, original_yaml: str) -> str:
    includes = []
    for index in range(1, 5):
        shared_name = {
            1: "_01_presentacion_tabular.qmd",
            2: "_02_presentacion_grafica.qmd",
            3: "_03_formas_distribucion.qmd",
            4: "_04_conclusiones.qmd",
        }[index]
        if shared_name:
            includes.append(f"{{{{< include ../contenido/{shared_name} >}}}}")
        context_name = {
            1: "_01_tablas.qmd",
            2: "_02_graficas.qmd",
            3: "_03_distribuciones.qmd",
            4: "_04_ejercicio.qmd",
        }[index]
        includes.append(f"{{{{< include ../ejemplos/{context}/{context_name} >}}}}")
    return yaml_for(context, original_yaml) + "\n\n" + "\n\n".join(includes) + "\n"


def main() -> None:
    before = sha256(ORIGINAL)
    lines = ORIGINAL.read_text(encoding="utf-8").splitlines(keepends=True)
    if len(lines) != 1480:
        raise RuntimeError(f"Se esperaban 1480 líneas; se encontraron {len(lines)}")

    original_yaml = "".join(lines[:46])
    shared_ranges = [(48, 381), (800, 868), (1110, 1139)]
    context_ranges = [(382, 799), (869, 1109), (1140, 1432), (1433, 1480)]
    shared_names = [
        "_01_presentacion_tabular.qmd",
        "_02_presentacion_grafica.qmd",
        "_03_formas_distribucion.qmd",
    ]

    (CLASS / "contenido").mkdir(parents=True, exist_ok=True)
    for context in ("agronomia", "zootecnia", "economia"):
        (CLASS / "ejemplos" / context).mkdir(parents=True, exist_ok=True)
        (CLASS / context).mkdir(parents=True, exist_ok=True)

    for name, (first, last) in zip(shared_names, shared_ranges):
        shared = lines_range(lines, first, last).replace('src="images/', 'src="../images/')
        (CLASS / "contenido" / name).write_text(shared, encoding="utf-8")
    (CLASS / "contenido" / "_04_conclusiones.qmd").write_text("", encoding="utf-8")

    agronomy_blocks = []
    for index, (first, last) in enumerate(context_ranges, start=1):
        agronomy = lines_range(lines, first, last)
        agronomy_blocks.append(agronomy)
        context_name = {
            1: "_01_tablas.qmd",
            2: "_02_graficas.qmd",
            3: "_03_distribuciones.qmd",
            4: "_04_ejercicio.qmd",
        }[index]
        (CLASS / "ejemplos" / "agronomia" / context_name).write_text(agronomy, encoding="utf-8")
        (CLASS / "ejemplos" / "zootecnia" / context_name).write_text(zootecnia(index, agronomy), encoding="utf-8")
        (CLASS / "ejemplos" / "economia" / context_name).write_text(economia(index, agronomy), encoding="utf-8")

    for context in ("agronomia", "zootecnia", "economia"):
        (CLASS / context / f"clase_2_{context}.qmd").write_text(main_file(context, original_yaml), encoding="utf-8")

    reconstructed = "".join(
        [
            lines_range(lines, 48, 381), agronomy_blocks[0],
            lines_range(lines, 800, 868), agronomy_blocks[1],
            lines_range(lines, 1110, 1139), agronomy_blocks[2], agronomy_blocks[3],
        ]
    )
    expected = lines_range(lines, 48, 1480)
    if reconstructed != expected:
        raise RuntimeError("La secuencia modular de Agronomía no reconstruye el cuerpo original")
    if sha256(ORIGINAL) != before:
        raise RuntimeError("El QMD original cambió durante la generación")

    print(f"Original intacto: {before}")
    print("Agronomía reconstruye exactamente las líneas 48–1480 del original")


if __name__ == "__main__":
    main()
