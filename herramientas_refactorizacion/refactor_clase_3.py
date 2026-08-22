#!/usr/bin/env python3
"""Genera las variantes modulares de la clase 3 sin modificar el original."""

from pathlib import Path
import hashlib


ROOT = Path(__file__).resolve().parents[1]
CLASS = ROOT / "clase_3"
ORIGINAL = CLASS / "clase_3.qmd"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lines_range(lines: list[str], first: int, last: int) -> str:
    return "".join(lines[first - 1:last])


def clean_separator(text: str) -> str:
    return text.replace(f" {chr(0x2014)} ", ", ").replace(chr(0x2014), ",")


def apply_changes(text: str, changes: dict[str, str]) -> str:
    for old, new in changes.items():
        text = text.replace(old, new)
    return clean_separator(text)


def zootecnia(block: int, text: str) -> str:
    changes = {
        1: {
            "En agronomía, salud, economía e ingeniería": "En zootecnia, salud animal, economía e ingeniería",
            "Determinar la producción por hectárea en un cultivo.": "Determinar la ganancia diaria de peso por animal.",
            "Evaluar la tasa de incidencia de una enfermedad en una región.": "Evaluar la tasa de incidencia de una enfermedad en un hato.",
            "Calcular cuánto insumo se necesita al escalar una producción.": "Calcular cuánto alimento se necesita al aumentar el número de animales.",
            "Comparar el rendimiento entre dos fincas de distinto tamaño.": "Comparar la productividad entre dos explotaciones pecuarias de distinto tamaño.",
        },
        2: {
            "<strong>Agronomía:</strong> producción (kg/ha), consumo de agua (L/planta/día).": "<strong>Zootecnia:</strong> ganancia de peso (kg/animal/día), consumo de agua (L/animal/día).",
            "<strong>Salud pública:</strong> incidencia (casos/100 000 hab), mortalidad (muertes/1 000 hab).": "<strong>Salud animal:</strong> incidencia (casos/100 000 animales), mortalidad (muertes/1 000 animales).",
            "<strong>Transporte:</strong> velocidad (km/h), consumo (L/100 km).": "<strong>Producción animal:</strong> leche (L/vaca/día), alimento (kg/lote/día).",
            "Ejemplo 1: Velocidad": "Ejemplo 1: Consumo de agua",
            "Un vehículo recorre 120 km en 2 horas. ¿Cuál es su velocidad?": "Un grupo de animales consume 120 L de agua en 2 horas. ¿Cuál es la tasa de consumo?",
            "120\\,\\text{km}": "120\\,\\text{L}",
            "2\\,\\text{h}} = 60\\,\\text{km/h}": "2\\,\\text{h}} = 60\\,\\text{L/h}",
            "Interpretación: el vehículo avanza <strong>60 km por cada hora</strong>.": "Interpretación: el grupo consume <strong>60 L de agua por cada hora</strong>.",
            "Ejemplo 2: Rendimiento agrícola": "Ejemplo 2: Producción de leche",
            "En un cultivo de maíz se producen 800 kg en 4 hectáreas. ¿Cuál es el rendimiento?": "En un mes, 4 vacas producen 800 L de leche. ¿Cuál es la producción mensual por vaca?",
            "800\\,\\text{kg}": "800\\,\\text{L}",
            "4\\,\\text{ha}} = 200\\,\\text{kg/ha}": "4\\,\\text{vacas}} = 200\\,\\text{L/vaca}",
            "Interpretación: se producen <strong>200 kg por hectárea</strong>.": "Interpretación: se producen <strong>200 L de leche por vaca durante el mes</strong>.",
            "## Tasas en salud pública": "## Tasas en salud animal",
            "Tasas epidemiológicas": "Tasas epidemiológicas veterinarias",
            "eventos de salud en una población": "eventos de salud en una población animal",
            "población en riesgo": "animales en riesgo",
            "Ejemplo: Dengue en el Tolima": "Ejemplo: enfermedad respiratoria en aves",
            "En un municipio de 50 000 habitantes se registraron 75 casos nuevos de dengue en un mes.": "En una población de 50 000 aves se registraron 75 casos nuevos de enfermedad respiratoria en un mes.",
            "50\\,000} \\times 100\\,000 = 150\\text{ casos por cada 100 000 hab}": "50\\,000} \\times 100\\,000 = 150\\text{ casos por cada 100 000 aves}",
            "Un agricultor recorre 400 km en 8 horas. ¿Cuál es su velocidad?": "Un lote consume 400 kg de alimento en 8 días. ¿Cuál es el consumo diario?",
            "En un cultivo de papa se aplican 250 kg de abono en 5 ha. ¿Cuánto abono se usa por hectárea?": "En una granja se distribuyen 250 kg de suplemento en 5 lotes. ¿Cuánto se usa por lote?",
            "En una vereda con 2 000 habitantes se reportaron 12 casos de malaria en un mes. ¿Cuál es la tasa de incidencia por 1 000 habitantes?": "En una granja con 2 000 aves se reportaron 12 casos de enfermedad en un mes. ¿Cuál es la tasa de incidencia por 1 000 aves?",
            "400\\,\\text{km} / 8\\,\\text{h} = \\mathbf{50\\,\\text{km/h}}": "400\\,\\text{kg} / 8\\,\\text{días} = \\mathbf{50\\,\\text{kg/día}}",
            "250\\,\\text{kg} / 5\\,\\text{ha} = \\mathbf{50\\,\\text{kg/ha}}": "250\\,\\text{kg} / 5\\,\\text{lotes} = \\mathbf{50\\,\\text{kg/lote}}",
            "6\\text{ casos por cada 1 000 hab}": "6\\text{ casos por cada 1 000 aves}",
        },
        3: {
            "Ejemplo 1: Cultivo mixto": "Ejemplo 1: Composición de un hato",
            "En una finca hay 60 plantas de maíz y 30 plantas de fríjol.": "En un hato hay 60 vacas adultas y 30 terneros.",
            "2 plantas de maíz por cada 1 planta de fríjol": "2 vacas adultas por cada 1 ternero",
            "Ejemplo 2: Sexo en un grupo": "Ejemplo 2: Sexo en un hato",
            "En un grupo de 60 estudiantes, 40 son hombres y 20 son mujeres.": "En un hato de 60 animales, 40 son hembras y 20 son machos.",
            "Razón hombres:mujeres": "Razón hembras:machos",
            "2 hombres por cada mujer": "2 hembras por cada macho",
            "En una finca hay 90 plantas de maíz y 30 plantas de fríjol.": "En un hato hay 90 vacas y 30 toros.",
            "Un bulto de fertilizante de 80 kg se distribuye en 40 sacos iguales. ¿Cuántos kg hay por saco?": "Se distribuyen 80 kg de suplemento entre 40 comederos. ¿Cuántos kg hay por comedero?",
            "En un salón hay 60 estudiantes, 20 de ellos son mujeres. ¿Cuál es la razón mujeres:hombres?": "En un lote hay 60 animales, 20 de ellos son machos. ¿Cuál es la razón machos:hembras?",
            "hay 3 plantas de maíz por cada planta de fríjol": "hay 3 vacas por cada toro",
            "hay 2 kg de fertilizante por saco": "hay 2 kg de suplemento por comedero",
            "Mujeres: 20, Hombres: 40. Razón": "Machos: 20, Hembras: 40. Razón",
            "hay 1 mujer por cada 2 hombres": "hay 1 macho por cada 2 hembras",
        },
        4: {
            "Problema \u2014 Fertilizante y plantas": "Problema, suplemento y animales",
            "En un cultivo, 4 kg de fertilizante son suficientes para 8 plantas. ¿Cuántos kg se necesitan para 20 plantas, manteniendo la misma proporción?": "En una granja, 4 kg de suplemento son suficientes para 8 animales. ¿Cuántos kg se necesitan para 20 animales, manteniendo la misma proporción?",
            "8\\,\\text{plantas}": "8\\,\\text{animales}",
            "20\\,\\text{plantas}": "20\\,\\text{animales}",
            "10 kg de fertilizante": "10 kg de suplemento",
            "para 20 plantas": "para 20 animales",
            "Problema \u2014 Estudiantes que aprueban": "Problema, animales que alcanzan la meta",
            "En una encuesta, 15 de cada 30 estudiantes aprueban un examen. Si se mantiene la misma proporción, ¿cuántos aprobarían en un grupo de 80?": "En un lote, 15 de cada 30 terneros alcanzan la meta de peso. Si se mantiene la misma proporción, ¿cuántos la alcanzarían en un lote de 80?",
            "x = 40\\,\\text{estudiantes}": "x = 40\\,\\text{terneros}",
            "Aprobarían <strong>40 estudiantes</strong>. La razón de aprobación": "Alcanzarían la meta <strong>40 terneros</strong>. La razón de cumplimiento",
            "3\\,\\text{kg} \\longrightarrow 9\\,\\text{plantas}, \\quad x \\longrightarrow 18\\,\\text{plantas}": "3\\,\\text{kg} \\longrightarrow 9\\,\\text{animales}, \\quad x \\longrightarrow 18\\,\\text{animales}",
            "9\\,\\text{plantas}": "9\\,\\text{animales}",
            "5\\,\\text{L} \\longrightarrow 10\\,\\text{m}^2, \\quad x \\longrightarrow 20\\,\\text{m}^2": "5\\,\\text{L} \\longrightarrow 10\\,\\text{corrales}, \\quad x \\longrightarrow 20\\,\\text{corrales}",
        },
        5: {
            "Ejemplo 1: aprobación en un examen": "Ejemplo 1: animales con ganancia esperada",
            "De 30 estudiantes, 18 aprobaron.": "De 30 animales, 18 alcanzaron la ganancia de peso esperada.",
            "de los estudiantes aprobó el examen": "de los animales alcanzó la ganancia esperada",
            "Ejemplo 2: plantas sanas": "Ejemplo 2: animales sanos",
            "En un cultivo se inspeccionan 50 plantas; 20 resultan sanas.": "En un hato se inspeccionan 50 animales, 20 resultan sanos.",
            "de las plantas se encontró en buen estado fitosanitario": "de los animales se encontró en buen estado de salud",
            "200 kg/ha": "200 L/vaca",
            "3:1 (maíz:fríjol)": "3:1 (vacas:terneros)",
        },
        6: {
            "Problema \u2014 Edades de un grupo": "Problema, producción de leche",
            "Se registraron las edades (años) de 15 personas:": "Se registró la producción diaria de leche (L) de 15 vacas:",
            "Calcule la edad promedio del grupo.": "Calcule la producción diaria promedio.",
            "20{,}87\\,\\text{años}": "20{,}87\\,\\text{L}",
            "La edad promedio del grupo es aproximadamente <strong>21 años</strong>.": "La producción promedio es aproximadamente <strong>21 L por vaca y día</strong>.",
            "A 50 estudiantes se les preguntó cuántas horas dormían por noche. Los resultados se agruparon así:": "Se registró el consumo diario de alimento de 50 animales. Los resultados se agruparon así:",
            "$x_i$ (horas)": "$x_i$ (kg)",
            "7{,}28\\,\\text{horas}": "7{,}28\\,\\text{kg}",
            "En promedio, los estudiantes duermen aproximadamente <strong>7 horas y 17 minutos</strong> por noche.": "En promedio, cada animal consume aproximadamente <strong>7,28 kg de alimento</strong> por día.",
            "edades <-": "leche <-",
            "mean(edades)": "mean(leche)",
        },
        7: {
            "Horas de estudio de 13 estudiantes": "Producción diaria de leche de 13 vacas",
            "6\\,\\text{horas}": "6\\,\\text{L}",
            "El 50 % de los estudiantes estudia <strong>6 horas o menos</strong>, y el otro 50 % estudia 6 horas o más.": "El 50 % de las vacas produce <strong>6 L o menos</strong>, y el otro 50 % produce 6 L o más.",
            "Producción de 14 parcelas agrícolas (kg)": "Ganancia mensual de peso de 14 terneros (kg)",
            "La mitad de las parcelas produce <strong>17,5 kg o menos</strong> y la otra mitad produce 17,5 kg o más.": "La mitad de los terneros gana <strong>17,5 kg o menos</strong> y la otra mitad gana 17,5 kg o más.",
            "Ejemplo: frutos por planta": "Ejemplo: crías por hembra",
            "**$Me = 4$ frutos.**": "**$Me = 4$ crías.**",
        },
        8: {
            "Tiempo (min) en completar una rutina de ejercicio": "Tiempo (min) requerido para el ordeño de un animal",
            "La mitad de las personas completa la rutina": "La mitad de los animales completa el ordeño",
            "horas <-": "leche <-",
            "sort(horas)": "sort(leche)",
            "median(horas)": "median(leche)",
            "parcelas <-": "ganancia <-",
            "median(parcelas)": "median(ganancia)",
        },
        9: {
            "Edades de 15 personas": "Producción diaria de leche de 15 vacas",
            "20\\,\\text{años}": "20\\,\\text{L}",
            "La edad más frecuente en el grupo es 20 años.": "La producción de leche más frecuente es 20 L por vaca y día.",
            "Número de trabajos entregados por 16 estudiantes": "Número de controles sanitarios realizados a 16 animales",
            "3 trabajos": "3 controles",
            "Los estudiantes entregan": "Los animales reciben",
            "Los estudiantes entregan, con mayor frecuencia, <strong>3 trabajos</strong>.": "Los animales reciben, con mayor frecuencia, <strong>3 controles</strong>.",
            "Gasto semanal (miles de pesos) de 35 estudiantes": "Consumo semanal de alimento (kg) de 35 animales",
            "Gasto ($×10^3$)": "Consumo (kg)",
            "El gasto más frecuente es aproximadamente <strong>52 000 pesos semanales</strong>.": "El consumo más frecuente es aproximadamente <strong>52 kg semanales</strong>.",
            "edades <-": "leche <-",
            "table(edades)": "table(leche)",
        },
        10: {
            "## Ejercicio: cacao en Santander": "## Ejercicio: producción porcina",
            "En una finca cacaotera del Magdalena Medio santandereano se recolectó información durante una jornada de cosecha.": "En una granja porcina se recolectó información productiva durante un período de seguimiento.",
            "En 7 hectáreas se obtuvieron <strong>1 260 kg de cacao fresco</strong> en <strong>9 días</strong>.": "En 7 corrales se obtuvo una <strong>ganancia total de 1 260 kg de peso vivo</strong> en <strong>9 días</strong>.",
            "En el lote hay <strong>420 plantas productivas</strong> y <strong>140 plantas jóvenes</strong>.": "En la granja hay <strong>420 cerdos en finalización</strong> y <strong>140 cerdos jóvenes</strong>.",
            "De <strong>280 mazorcas</strong> revisadas, <strong>196 estaban sanas</strong> y <strong>84 presentaban daño leve por insectos</strong>.": "De <strong>280 cerdos</strong> revisados, <strong>196 estaban sanos</strong> y <strong>84 presentaban lesiones leves</strong>.",
            "Además, se seleccionaron 20 mazorcas y se registró su <strong>peso en gramos</strong>": "Además, se seleccionaron 20 cerdos y se registró su <strong>ganancia diaria de peso en gramos</strong>",
            "producción en kg/ha": "ganancia de peso en kg/corral",
            "razón</strong> entre plantas productivas y plantas jóvenes": "razón</strong> entre cerdos en finalización y cerdos jóvenes",
            "proporción</strong> de mazorcas sanas": "proporción</strong> de cerdos sanos",
            "peso de las mazorcas": "ganancia diaria de peso",
            "peso típico de las mazorcas": "ganancia diaria típica de peso",
        },
    }[block]
    return apply_changes(text, changes)


def economia(block: int, text: str) -> str:
    changes = {
        1: {
            "En agronomía, salud, economía e ingeniería": "En economía, administración, finanzas e ingeniería",
            "Determinar la producción por hectárea en un cultivo.": "Determinar las ventas por trabajador en una empresa.",
            "Evaluar la tasa de incidencia de una enfermedad en una región.": "Evaluar la tasa de creación de empresas en una región.",
            "Calcular cuánto insumo se necesita al escalar una producción.": "Calcular cuántos recursos se necesitan al escalar una operación.",
            "Comparar el rendimiento entre dos fincas de distinto tamaño.": "Comparar el rendimiento entre dos empresas de distinto tamaño.",
        },
        2: {
            "<strong>Agronomía:</strong> producción (kg/ha), consumo de agua (L/planta/día).": "<strong>Economía:</strong> ventas (pesos/trabajador), producción (unidades/hora).",
            "<strong>Salud pública:</strong> incidencia (casos/100 000 hab), mortalidad (muertes/1 000 hab).": "<strong>Mercado laboral:</strong> contrataciones (personas/mes), productividad (unidades/trabajador).",
            "<strong>Transporte:</strong> velocidad (km/h), consumo (L/100 km).": "<strong>Finanzas:</strong> rendimiento (pesos invertidos/mes), costos (pesos/unidad).",
            "Ejemplo 1: Velocidad": "Ejemplo 1: Productividad",
            "Un vehículo recorre 120 km en 2 horas. ¿Cuál es su velocidad?": "Una línea produce 120 unidades en 2 horas. ¿Cuál es su productividad?",
            "120\\,\\text{km}": "120\\,\\text{unidades}",
            "2\\,\\text{h}} = 60\\,\\text{km/h}": "2\\,\\text{h}} = 60\\,\\text{unidades/h}",
            "Interpretación: el vehículo avanza <strong>60 km por cada hora</strong>.": "Interpretación: la línea produce <strong>60 unidades por cada hora</strong>.",
            "Ejemplo 2: Rendimiento agrícola": "Ejemplo 2: Ventas por sucursal",
            "En un cultivo de maíz se producen 800 kg en 4 hectáreas. ¿Cuál es el rendimiento?": "Una empresa registra ventas de 800 millones de pesos en 4 sucursales. ¿Cuál es la venta promedio por sucursal?",
            "800\\,\\text{kg}": "800\\,\\text{millones}",
            "4\\,\\text{ha}} = 200\\,\\text{kg/ha}": "4\\,\\text{sucursales}} = 200\\,\\text{millones/sucursal}",
            "Interpretación: se producen <strong>200 kg por hectárea</strong>.": "Interpretación: se registran <strong>200 millones de pesos por sucursal</strong>.",
            "## Tasas en salud pública": "## Tasas en economía",
            "Tasas epidemiológicas": "Tasas de creación empresarial",
            "En epidemiología, las tasas miden la frecuencia de eventos de salud en una población": "En economía, las tasas pueden medir la frecuencia de creación de empresas en una población empresarial",
            "Tasa de incidencia": "Tasa de creación",
            "casos nuevos en un período": "empresas nuevas en un período",
            "población en riesgo": "empresas registradas",
            "Ejemplo: Dengue en el Tolima": "Ejemplo: creación empresarial",
            "En un municipio de 50 000 habitantes se registraron 75 casos nuevos de dengue en un mes.": "En una región con 50 000 empresas registradas se crearon 75 empresas en un mes.",
            "150\\text{ casos por cada 100 000 hab}": "150\\text{ empresas nuevas por cada 100 000 registradas}",
            "Un agricultor recorre 400 km en 8 horas. ¿Cuál es su velocidad?": "Una planta produce 400 unidades en 8 horas. ¿Cuál es su productividad?",
            "En un cultivo de papa se aplican 250 kg de abono en 5 ha. ¿Cuánto abono se usa por hectárea?": "Una empresa distribuye 250 millones de pesos entre 5 sucursales. ¿Cuánto corresponde a cada sucursal?",
            "En una vereda con 2 000 habitantes se reportaron 12 casos de malaria en un mes. ¿Cuál es la tasa de incidencia por 1 000 habitantes?": "En una región con 2 000 empresas se crearon 12 empresas en un mes. ¿Cuál es la tasa de creación por 1 000 empresas?",
            "400\\,\\text{km} / 8\\,\\text{h} = \\mathbf{50\\,\\text{km/h}}": "400\\,\\text{unidades} / 8\\,\\text{h} = \\mathbf{50\\,\\text{unidades/h}}",
            "250\\,\\text{kg} / 5\\,\\text{ha} = \\mathbf{50\\,\\text{kg/ha}}": "250\\,\\text{millones} / 5\\,\\text{sucursales} = \\mathbf{50\\,\\text{millones/sucursal}}",
            "6\\text{ casos por cada 1 000 hab}": "6\\text{ empresas nuevas por cada 1 000 registradas}",
        },
        3: {
            "Ejemplo 1: Cultivo mixto": "Ejemplo 1: Mezcla de productos",
            "En una finca hay 60 plantas de maíz y 30 plantas de fríjol.": "En una tienda hay 60 productos de tipo A y 30 productos de tipo B.",
            "2 plantas de maíz por cada 1 planta de fríjol": "2 productos de tipo A por cada 1 de tipo B",
            "Ejemplo 2: Sexo en un grupo": "Ejemplo 2: Tamaño empresarial",
            "En un grupo de 60 estudiantes, 40 son hombres y 20 son mujeres.": "En un grupo de 60 empresas, 40 son pequeñas y 20 son medianas.",
            "Razón hombres:mujeres": "Razón pequeñas:medianas",
            "2 hombres por cada mujer": "2 empresas pequeñas por cada empresa mediana",
            "En una finca hay 90 plantas de maíz y 30 plantas de fríjol.": "En un inventario hay 90 productos de tipo A y 30 de tipo B.",
            "Un bulto de fertilizante de 80 kg se distribuye en 40 sacos iguales. ¿Cuántos kg hay por saco?": "Un presupuesto de 80 millones se distribuye entre 40 proyectos. ¿Cuánto corresponde a cada proyecto?",
            "En un salón hay 60 estudiantes, 20 de ellos son mujeres. ¿Cuál es la razón mujeres:hombres?": "En un mercado hay 60 empresas, 20 son medianas. ¿Cuál es la razón medianas:pequeñas?",
            "hay 3 plantas de maíz por cada planta de fríjol": "hay 3 productos de tipo A por cada producto de tipo B",
            "hay 2 kg de fertilizante por saco": "hay 2 millones de pesos por proyecto",
            "Mujeres: 20, Hombres: 40. Razón": "Medianas: 20, Pequeñas: 40. Razón",
            "hay 1 mujer por cada 2 hombres": "hay 1 empresa mediana por cada 2 pequeñas",
        },
        4: {
            "Problema \u2014 Fertilizante y plantas": "Problema, inversión y unidades productivas",
            "En un cultivo, 4 kg de fertilizante son suficientes para 8 plantas. ¿Cuántos kg se necesitan para 20 plantas, manteniendo la misma proporción?": "Una inversión de 4 millones de pesos cubre 8 unidades productivas. ¿Cuántos millones se necesitan para 20 unidades, manteniendo la misma proporción?",
            "4\\,\\text{kg}": "4\\,\\text{millones}",
            "8\\,\\text{plantas}": "8\\,\\text{unidades}",
            "20\\,\\text{plantas}": "20\\,\\text{unidades}",
            "10\\,\\text{kg}": "10\\,\\text{millones}",
            "10 kg de fertilizante": "10 millones de pesos",
            "para 20 plantas": "para 20 unidades productivas",
            "Problema \u2014 Estudiantes que aprueban": "Problema, empresas que cumplen la meta",
            "En una encuesta, 15 de cada 30 estudiantes aprueban un examen. Si se mantiene la misma proporción, ¿cuántos aprobarían en un grupo de 80?": "En una muestra, 15 de cada 30 empresas cumplen la meta de ventas. Si se mantiene la misma proporción, ¿cuántas la cumplirían en un grupo de 80?",
            "x = 40\\,\\text{estudiantes}": "x = 40\\,\\text{empresas}",
            "Aprobarían <strong>40 estudiantes</strong>. La razón de aprobación": "Cumplirían la meta <strong>40 empresas</strong>. La razón de cumplimiento",
            "3\\,\\text{kg} \\longrightarrow 9\\,\\text{plantas}, \\quad x \\longrightarrow 18\\,\\text{plantas}": "3\\,\\text{millones} \\longrightarrow 9\\,\\text{unidades}, \\quad x \\longrightarrow 18\\,\\text{unidades}",
            "3\\,\\text{kg} \\longrightarrow 9\\,\\text{plantas}": "3\\,\\text{millones} \\longrightarrow 9\\,\\text{unidades}",
            "5\\,\\text{L} \\longrightarrow 10\\,\\text{m}^2, \\quad x \\longrightarrow 20\\,\\text{m}^2": "5\\,\\text{empleados} \\longrightarrow 10\\,\\text{locales}, \\quad x \\longrightarrow 20\\,\\text{locales}",
            "lote de 200 aves, 30 presentan una enfermedad": "cartera de 200 créditos, 30 presentan mora",
            "aves enfermas se esperan en un lote de 500": "créditos en mora se esperan en una cartera de 500",
            "75\\,\\text{aves enfermas}": "75\\,\\text{créditos en mora}",
        },
        5: {
            "Ejemplo 1: aprobación en un examen": "Ejemplo 1: empresas rentables",
            "De 30 estudiantes, 18 aprobaron.": "De 30 empresas, 18 fueron rentables.",
            "de los estudiantes aprobó el examen": "de las empresas fue rentable",
            "Ejemplo 2: plantas sanas": "Ejemplo 2: productos con precio estable",
            "En un cultivo se inspeccionan 50 plantas; 20 resultan sanas.": "En un mercado se observan 50 productos, 20 mantienen un precio estable.",
            "de las plantas se encontró en buen estado fitosanitario": "de los productos mantuvo un precio estable",
            "200 kg/ha": "200 millones/sucursal",
            "3:1 (maíz:fríjol)": "3:1 (producto A:producto B)",
        },
        6: {
            "Problema \u2014 Edades de un grupo": "Problema, ventas mensuales",
            "Se registraron las edades (años) de 15 personas:": "Se registraron las ventas mensuales (millones de pesos) de 15 tiendas:",
            "Calcule la edad promedio del grupo.": "Calcule la venta mensual promedio.",
            "20{,}87\\,\\text{años}": "20{,}87\\,\\text{millones}",
            "La edad promedio del grupo es aproximadamente <strong>21 años</strong>.": "La venta mensual promedio es aproximadamente <strong>21 millones de pesos</strong>.",
            "A 50 estudiantes se les preguntó cuántas horas dormían por noche. Los resultados se agruparon así:": "A 50 hogares se les preguntó cuántas compras realizaban por semana. Los resultados se agruparon así:",
            "$x_i$ (horas)": "$x_i$ (compras)",
            "7{,}28\\,\\text{horas}": "7{,}28\\,\\text{compras}",
            "En promedio, los estudiantes duermen aproximadamente <strong>7 horas y 17 minutos</strong> por noche.": "En promedio, los hogares realizan aproximadamente <strong>7,28 compras</strong> por semana.",
            "Se registró el peso (kg) de 20 animales en intervalos:": "Se registró el precio (miles de pesos) de 20 productos en intervalos:",
            "Intervalo (kg)": "Intervalo (miles de pesos)",
            "71{,}5\\,\\text{kg}": "71{,}5\\,\\text{mil pesos}",
            "El peso promedio de los animales es <strong>71,5 kg</strong>.": "El precio promedio de los productos es <strong>71,5 mil pesos</strong>.",
            "edades <-": "ventas <-",
            "mean(edades)": "mean(ventas)",
        },
        7: {
            "Horas de estudio de 13 estudiantes": "Ventas diarias de 13 tiendas",
            "6\\,\\text{horas}": "6\\,\\text{millones}",
            "El 50 % de los estudiantes estudia <strong>6 horas o menos</strong>, y el otro 50 % estudia 6 horas o más.": "El 50 % de las tiendas vende <strong>6 millones o menos</strong>, y el otro 50 % vende 6 millones o más.",
            "Producción de 14 parcelas agrícolas (kg)": "Ingresos mensuales de 14 empresas (millones de pesos)",
            "17{,}5\\,\\text{kg}": "17{,}5\\,\\text{millones}",
            "La mitad de las parcelas produce <strong>17,5 kg o menos</strong> y la otra mitad produce 17,5 kg o más.": "La mitad de las empresas registra <strong>17,5 millones o menos</strong> y la otra mitad registra 17,5 millones o más.",
            "Ejemplo: frutos por planta": "Ejemplo: compras por cliente",
            "**$Me = 4$ frutos.**": "**$Me = 4$ compras.**",
        },
        8: {
            "Tiempo (min) en completar una rutina de ejercicio": "Tiempo (min) de atención a un cliente",
            "La mitad de las personas completa la rutina": "La mitad de los clientes recibe atención",
            "horas <-": "ventas <-",
            "sort(horas)": "sort(ventas)",
            "median(horas)": "median(ventas)",
            "parcelas <-": "ingresos <-",
            "median(parcelas)": "median(ingresos)",
        },
        9: {
            "Edades de 15 personas": "Transacciones diarias de 15 tiendas",
            "20\\,\\text{años}": "20\\,\\text{transacciones}",
            "La edad más frecuente en el grupo es 20 años.": "El número de transacciones más frecuente es 20 por día.",
            "Número de trabajos entregados por 16 estudiantes": "Número de compras realizadas por 16 clientes",
            "3 trabajos": "3 compras",
            "Los estudiantes entregan": "Los clientes realizan",
            "Los estudiantes entregan, con mayor frecuencia, <strong>3 trabajos</strong>.": "Los clientes realizan, con mayor frecuencia, <strong>3 compras</strong>.",
            "Gasto semanal (miles de pesos) de 35 estudiantes": "Gasto semanal (miles de pesos) de 35 hogares",
            "edades <-": "transacciones <-",
            "table(edades)": "table(transacciones)",
        },
        10: {
            "## Ejercicio: cacao en Santander": "## Ejercicio: operación comercial",
            "En una finca cacaotera del Magdalena Medio santandereano se recolectó información durante una jornada de cosecha.": "En una cadena comercial se recolectó información durante un período de operación.",
            "En 7 hectáreas se obtuvieron <strong>1 260 kg de cacao fresco</strong> en <strong>9 días</strong>.": "En 7 sucursales se vendieron <strong>1 260 unidades</strong> en <strong>9 días</strong>.",
            "En el lote hay <strong>420 plantas productivas</strong> y <strong>140 plantas jóvenes</strong>.": "La cadena tiene <strong>420 clientes recurrentes</strong> y <strong>140 clientes nuevos</strong>.",
            "De <strong>280 mazorcas</strong> revisadas, <strong>196 estaban sanas</strong> y <strong>84 presentaban daño leve por insectos</strong>.": "De <strong>280 pedidos</strong> revisados, <strong>196 llegaron a tiempo</strong> y <strong>84 presentaron retraso leve</strong>.",
            "Además, se seleccionaron 20 mazorcas y se registró su <strong>peso en gramos</strong>": "Además, se seleccionaron 20 transacciones y se registró su <strong>valor en miles de pesos</strong>",
            "producción en kg/ha": "ventas en unidades/sucursal",
            "razón</strong> entre plantas productivas y plantas jóvenes": "razón</strong> entre clientes recurrentes y clientes nuevos",
            "proporción</strong> de mazorcas sanas": "proporción</strong> de pedidos entregados a tiempo",
            "peso de las mazorcas": "valor de las transacciones",
            "peso típico de las mazorcas": "valor típico de las transacciones",
        },
    }[block]
    return apply_changes(text, changes)


SHARED_SEGMENTS = [
    ("_01_apertura.qmd", 43, 82),
    ("_02_definicion_tasas.qmd", 120, 154),
    ("_03_definicion_razones.qmd", 231, 249),
    ("_04_definicion_proporciones.qmd", 295, 314),
    ("_05_proporcion_estadistica.qmd", 377, 401),
    ("_06_introduccion_media.qmd", 441, 525),
    ("_07_introduccion_mediana.qmd", 622, 670),
    ("_08_mediana_agrupada.qmd", 747, 762),
    ("_09_introduccion_moda.qmd", 804, 845),
    ("_10_cierre.qmd", 933, 1037),
]

CONTEXT_SEGMENTS = [
    ("_01_contexto.qmd", 83, 119),
    ("_02_tasas.qmd", 155, 230),
    ("_03_razones.qmd", 250, 294),
    ("_04_proporciones.qmd", 315, 376),
    ("_05_porcentajes.qmd", 402, 440),
    ("_06_media.qmd", 526, 621),
    ("_07_mediana.qmd", 671, 746),
    ("_08_mediana_intervalos.qmd", 763, 803),
    ("_09_moda.qmd", 846, 932),
    ("_10_taller.qmd", 1038, 1070),
]


def yaml_for(context: str, original_yaml: str) -> str:
    label = {"agronomia": "Agronomía", "zootecnia": "Zootecnia", "economia": "Economía"}[context]
    yaml = original_yaml.replace('title: "Bioestadística Fundamental"', f'title: "Bioestadística, {label}"', 1)
    yaml = yaml.replace(f'title: "Bioestadística, {label}"\n', f'title: "Bioestadística, {label}"\nsubtitle: "Tasas, razones, proporciones y tendencia central"\n', 1)
    yaml = yaml.replace("bibliography: referencias.bib\n", "bibliography: ../referencias.bib\n", 1)
    yaml = yaml.replace("csl: ieee.csl\n", f"csl: ../ieee.csl\noutput-file: clase_3_{context}.html\n", 1)
    yaml = yaml.replace("logo: images/", "logo: ../images/", 1)
    yaml = yaml.replace("../assets/", "../../assets/")
    return clean_separator(yaml)


def main_file(context: str, original_yaml: str) -> str:
    includes = []
    for index, ((shared_name, _, _), (context_name, _, _)) in enumerate(zip(SHARED_SEGMENTS, CONTEXT_SEGMENTS), start=1):
        includes.append(f"{{{{< include ../contenido/{shared_name} >}}}}")
        includes.append(f"{{{{< include ../ejemplos/{context}/{context_name} >}}}}")
    return yaml_for(context, original_yaml) + "\n" + "\n\n".join(includes) + "\n"


def main() -> None:
    before = sha256(ORIGINAL)
    lines = ORIGINAL.read_text(encoding="utf-8").splitlines(keepends=True)
    if len(lines) != 1070:
        raise RuntimeError(f"Se esperaban 1070 líneas; se encontraron {len(lines)}")

    original_yaml = "".join(lines[:41])
    (CLASS / "contenido").mkdir(parents=True, exist_ok=True)
    for context in ("agronomia", "zootecnia", "economia"):
        (CLASS / "ejemplos" / context).mkdir(parents=True, exist_ok=True)
        (CLASS / context).mkdir(parents=True, exist_ok=True)

    for name, first, last in SHARED_SEGMENTS:
        source = clean_separator(lines_range(lines, first, last))
        (CLASS / "contenido" / name).write_text(source, encoding="utf-8")

    agronomy_blocks = []
    for index, (name, first, last) in enumerate(CONTEXT_SEGMENTS, start=1):
        raw_source = lines_range(lines, first, last)
        source = clean_separator(raw_source)
        agronomy_blocks.append(source)
        (CLASS / "ejemplos" / "agronomia" / name).write_text(source, encoding="utf-8")
        (CLASS / "ejemplos" / "zootecnia" / name).write_text(zootecnia(index, raw_source), encoding="utf-8")
        (CLASS / "ejemplos" / "economia" / name).write_text(economia(index, raw_source), encoding="utf-8")

    for context in ("agronomia", "zootecnia", "economia"):
        (CLASS / context / f"clase_3_{context}.qmd").write_text(main_file(context, original_yaml), encoding="utf-8")

    reconstructed_parts = []
    for (shared_name, first_s, last_s), (_, first_c, last_c), agronomy in zip(SHARED_SEGMENTS, CONTEXT_SEGMENTS, agronomy_blocks):
        reconstructed_parts.append(clean_separator(lines_range(lines, first_s, last_s)))
        reconstructed_parts.append(agronomy)
    reconstructed = "".join(reconstructed_parts)
    expected = clean_separator(lines_range(lines, 43, 1070))
    if reconstructed != expected:
        raise RuntimeError("La reconstrucción de Agronomía no coincide con el cuerpo original normalizado")
    if sha256(ORIGINAL) != before:
        raise RuntimeError("El archivo original fue modificado")

    for path in [CLASS / "contenido", CLASS / "ejemplos"]:
        for file in path.rglob("*.qmd"):
            if chr(0x2014) in file.read_text(encoding="utf-8"):
                raise RuntimeError(f"Separador no permitido en {file}")

    print(f"Original intacto: {before}")
    print("Variantes de clase 3 generadas")


if __name__ == "__main__":
    main()
