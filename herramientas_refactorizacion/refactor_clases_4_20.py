#!/usr/bin/env python3
"""Genera variantes modulares de las clases 4 a 20 sin modificar originales."""

from __future__ import annotations

from pathlib import Path
import csv
import hashlib
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
CONTEXTS = ("agronomia", "zootecnia", "economia")
LABELS = {"agronomia": "Agronomía", "zootecnia": "Zootecnia", "economia": "Economía"}

DOMAIN_PATTERN = re.compile(
    r"agron|agr[ií]col|cultiv|cosech|ma[ií]z|caf[eé]|papa|arroz|trigo|cacao|"
    r"semilla|planta|parcela|suelo|fertiliz|plaga|insect|riego|hect[aá]rea|finca|"
    r"germin|rendimiento|fitosanit|variedad|mora|fresa|ca[nñ]a|fr[ií]jol|"
    r"tub[eé]rculo|abono|herbicida|fungicida|pesticida|plaguicida|mazorca|grano|nitr[oó]geno",
    re.IGNORECASE,
)

EXAMPLE_HEADING_PATTERN = re.compile(
    r"ejempl|ejerc|taller|aplic|soluci|interpret|resultado|datos experimentales|"
    r"c[aá]lculo|simulaci|estudio completo|reporte t[eé]cnico|experimento|"
    r"producci[oó]n de|diagn[oó]stico de|control de calidad|ensayo|muestrear",
    re.IGNORECASE,
)


PHRASES_ZOOTECNIA = [
    ("IR8, FEDEARROZ, ORYZICA, COLOMBIA", "Dieta A, Dieta B, Dieta C, Dieta D"),
    ("peso de sacos de café", "peso de animales del hato"),
    ("peso de sacos", "peso de animales"),
    ("materia orgánica del suelo", "contenido proteico de la dieta"),
    ("materia orgánica", "contenido proteico"),
    ("precipitación mensual (mm)", "consumo mensual de alimento (kg)"),
    ("precipitación (mm)", "consumo de alimento (kg)"),
    ("kg/árbol", "L/animal"),
    ("kg por árbol", "L por animal"),
    ("toneladas/ha", "kg/animal"),
    ("sacos por hectárea", "L por animal"),
    ("sacos por finca", "L por granja"),
    ("<em>Coffea arabica</em>", "<em>Bos taurus</em>"),
    ("roya del café", "mastitis bovina"),
    ("roya en café", "mastitis en bovinos"),
    ("resistencia genética a la roya", "resistencia genética a mastitis"),
    ("presencia de roya", "presencia de mastitis"),
    ("con roya", "con mastitis"),
    ("tenga roya", "tenga mastitis"),
    ("tener roya", "tener mastitis"),
    ("manchas foliares", "signos clínicos"),
    ("rendimiento de café pergamino seco", "producción diaria de leche"),
    ("café pergamino seco", "leche producida"),
    ("fertilización nitrogenada", "suplementación proteica"),
    ("dosis de nitrógeno", "nivel de proteína"),
    ("Castillo, Colombia, Cenicafé 1, Tabi, Bourbon", "Dieta A, Dieta B, Dieta C, Dieta D, Dieta E"),
    ("Diacol Capiro", "Dieta A"),
    ("Pastusa Suprema", "Dieta B"),
    ("Criolla Colombia", "Dieta C"),
    ("Parda Pastusa", "Dieta D"),
    ("Fedearroz 60", "Dieta A"),
    ("Fedearroz 67", "Dieta B"),
    ("Fedearroz 2000", "Dieta C"),
    ("Coprosem", "Dieta D"),
    ("tratamientos de fertilización", "tratamientos de suplementación"),
    ("tratamiento de fertilización", "tratamiento de suplementación"),
    ("fertilidad del suelo", "calidad de la dieta"),
    ("fecha de siembra", "fecha de ingreso"),
    ("densidad de siembra", "densidad animal"),
    ("densidades de siembra", "densidades animales"),
    ("sistema de siembra", "sistema de manejo"),
    ("sistemas de siembra", "sistemas de manejo"),
    ("ingeniero agrónomo", "profesional en zootecnia"),
    ("un agrónomo", "un profesional en zootecnia"),
    ("una agrónoma", "una profesional en zootecnia"),
    ("grupo de agrónomos", "grupo de profesionales en zootecnia"),
    ("región cafetera", "región ganadera"),
    ("regiones cafeteras", "regiones ganaderas"),
    ("Eje Cafetero", "región ganadera"),
    ("Centro Nacional de Investigaciones de Café", "Centro Nacional de Investigación Pecuaria"),
    ("variedades de papa", "dietas para cerdos"),
    ("variedades de arroz", "dietas para aves"),
    ("variedades de café", "dietas para ganado"),
    ("variedades de maíz", "dietas para bovinos"),
    ("semillas de maíz", "terneros"),
    ("semillas de papa", "lechones"),
    ("semillas de café", "animales del hato"),
    ("semillas de arroz", "pollitos"),
    ("proveedores de semillas", "proveedores de alimento"),
    ("lote de semillas", "grupo de animales"),
    ("lotes de semillas", "grupos de animales"),
    ("cultivo de café", "hato bovino"),
    ("cultivo de papa", "granja porcina"),
    ("cultivo de arroz", "granja avícola"),
    ("cultivo de maíz", "hato bovino"),
    ("cultivo de trigo", "rebaño ovino"),
    ("cultivo de cacao", "granja porcina"),
    ("cultivo de fresa", "rebaño caprino"),
    ("cultivo de mora", "rebaño ovino"),
    ("plantas de café", "animales del hato"),
    ("plantas de maíz", "bovinos"),
    ("plantas de arroz", "aves"),
    ("plantas de papa", "cerdos"),
    ("producción de café", "producción de leche"),
    ("producción de papa", "ganancia de peso porcina"),
    ("producción de arroz", "producción de huevos"),
    ("producción de maíz", "ganancia de peso bovina"),
    ("rendimiento de café", "producción de leche"),
    ("rendimiento de papa", "ganancia de peso porcina"),
    ("rendimiento de arroz", "producción de huevos"),
    ("rendimiento de maíz", "ganancia de peso bovina"),
    ("peso de la mazorca", "ganancia diaria de peso"),
    ("peso de mazorca", "ganancia diaria de peso"),
    ("peso del grano", "peso del animal"),
    ("peso de grano", "peso animal"),
    ("altura de planta", "peso animal"),
    ("altura de las plantas", "peso de los animales"),
    ("control fitosanitario", "control sanitario"),
    ("tratamiento fitosanitario", "tratamiento veterinario"),
    ("enfermedad en maíz", "enfermedad en bovinos"),
    ("enfermedad del cultivo", "enfermedad del hato"),
    ("tipo de suelo", "tipo de dieta"),
    ("zonas de cultivo", "sistemas de producción"),
    ("zona de cultivo", "sistema de producción"),
    ("condiciones ambientales", "condiciones de manejo"),
    ("kg/ha", "kg/animal"),
    ("kg ha⁻¹", "kg animal⁻¹"),
    ("kg ha^-1", "kg animal^-1"),
    ("ton/ha", "kg/animal"),
    ("t/ha", "kg/animal"),
    ("sacos/ha", "kg/animal"),
    ("toneladas por hectárea", "kg por animal"),
    ("toneladas por ha", "kg por animal"),
    ("L/planta/día", "L/animal/día"),
    ("L/planta", "L/animal"),
]

PHRASES_ECONOMIA = [
    ("IR8, FEDEARROZ, ORYZICA, COLOMBIA", "Estrategia A, Estrategia B, Estrategia C, Estrategia D"),
    ("peso de sacos de café", "valor de transacciones comerciales"),
    ("peso de sacos", "valor de transacciones"),
    ("materia orgánica del suelo", "disponibilidad de capital del mercado"),
    ("materia orgánica", "disponibilidad de capital"),
    ("precipitación mensual (mm)", "demanda mensual (índice)"),
    ("precipitación (mm)", "demanda (índice)"),
    ("kg/árbol", "millones/empresa"),
    ("kg por árbol", "millones por empresa"),
    ("toneladas/ha", "millones/sucursal"),
    ("sacos por hectárea", "millones por sucursal"),
    ("sacos por finca", "millones por empresa"),
    ("<em>Coffea arabica</em>", "sector comercio"),
    ("roya del café", "incumplimiento comercial"),
    ("roya en café", "incumplimiento comercial"),
    ("resistencia genética a la roya", "resistencia financiera al incumplimiento"),
    ("presencia de roya", "presencia de incumplimiento"),
    ("con roya", "con incumplimiento"),
    ("tenga roya", "tenga incumplimiento"),
    ("tener roya", "tener incumplimiento"),
    ("manchas foliares", "señales de incumplimiento"),
    ("rendimiento de café pergamino seco", "rentabilidad comercial"),
    ("café pergamino seco", "ventas comerciales"),
    ("fertilización nitrogenada", "inversión publicitaria"),
    ("dosis de nitrógeno", "nivel de publicidad"),
    ("Castillo, Colombia, Cenicafé 1, Tabi, Bourbon", "Estrategia A, Estrategia B, Estrategia C, Estrategia D, Estrategia E"),
    ("Diacol Capiro", "Estrategia A"),
    ("Pastusa Suprema", "Estrategia B"),
    ("Criolla Colombia", "Estrategia C"),
    ("Parda Pastusa", "Estrategia D"),
    ("Fedearroz 60", "Estrategia A"),
    ("Fedearroz 67", "Estrategia B"),
    ("Fedearroz 2000", "Estrategia C"),
    ("Coprosem", "Estrategia D"),
    ("tratamientos de fertilización", "estrategias de inversión"),
    ("tratamiento de fertilización", "estrategia de inversión"),
    ("fertilidad del suelo", "dinamismo del mercado"),
    ("fecha de siembra", "fecha de implementación"),
    ("densidad de siembra", "escala de operación"),
    ("densidades de siembra", "escalas de operación"),
    ("sistema de siembra", "sistema de operación"),
    ("sistemas de siembra", "sistemas de operación"),
    ("ingeniero agrónomo", "analista económico"),
    ("un agrónomo", "un analista económico"),
    ("una agrónoma", "una analista económica"),
    ("grupo de agrónomos", "grupo de analistas económicos"),
    ("región cafetera", "región comercial"),
    ("regiones cafeteras", "regiones comerciales"),
    ("Eje Cafetero", "región comercial"),
    ("Centro Nacional de Investigaciones de Café", "Centro de Estudios Económicos"),
    ("variedades de papa", "estrategias de la industria"),
    ("variedades de arroz", "estrategias de servicios"),
    ("variedades de café", "estrategias comerciales"),
    ("variedades de maíz", "estrategias de producto"),
    ("semillas de maíz", "proyectos comerciales"),
    ("semillas de papa", "proyectos industriales"),
    ("semillas de café", "proyectos de comercio"),
    ("semillas de arroz", "proyectos de servicios"),
    ("proveedores de semillas", "proveedores de insumos"),
    ("lote de semillas", "cartera de proyectos"),
    ("lotes de semillas", "carteras de proyectos"),
    ("cultivo de café", "sector comercio"),
    ("cultivo de papa", "sector industrial"),
    ("cultivo de arroz", "sector servicios"),
    ("cultivo de maíz", "mercado de productos"),
    ("cultivo de trigo", "cartera de inversiones"),
    ("cultivo de cacao", "operación de ventas"),
    ("cultivo de fresa", "sector minorista"),
    ("cultivo de mora", "cartera de crédito"),
    ("plantas de café", "empresas comerciales"),
    ("plantas de maíz", "empresas de productos"),
    ("plantas de arroz", "empresas de servicios"),
    ("plantas de papa", "empresas industriales"),
    ("producción de café", "ventas del sector comercio"),
    ("producción de papa", "producción industrial"),
    ("producción de arroz", "ventas del sector servicios"),
    ("producción de maíz", "ventas de productos"),
    ("rendimiento de café", "rentabilidad comercial"),
    ("rendimiento de papa", "rentabilidad industrial"),
    ("rendimiento de arroz", "rentabilidad de servicios"),
    ("rendimiento de maíz", "rentabilidad de productos"),
    ("peso de la mazorca", "valor de la transacción"),
    ("peso de mazorca", "valor de la transacción"),
    ("peso del grano", "precio del producto"),
    ("peso de grano", "precio del producto"),
    ("altura de planta", "precio del producto"),
    ("altura de las plantas", "precio de los productos"),
    ("control fitosanitario", "control de calidad"),
    ("tratamiento fitosanitario", "política de calidad"),
    ("enfermedad en maíz", "incumplimiento en empresas"),
    ("enfermedad del cultivo", "incumplimiento empresarial"),
    ("tipo de suelo", "tipo de mercado"),
    ("zonas de cultivo", "segmentos de mercado"),
    ("zona de cultivo", "segmento de mercado"),
    ("condiciones ambientales", "condiciones de mercado"),
    ("kg/ha", "millones/sucursal"),
    ("kg ha⁻¹", "millones sucursal⁻¹"),
    ("kg ha^-1", "millones sucursal^-1"),
    ("ton/ha", "millones/sucursal"),
    ("t/ha", "millones/sucursal"),
    ("sacos/ha", "millones/sucursal"),
    ("toneladas por hectárea", "millones por sucursal"),
    ("toneladas por ha", "millones por sucursal"),
    ("L/planta/día", "millones/empresa/día"),
    ("L/planta", "millones/empresa"),
]

WORDS_ZOOTECNIA = {
    "agronomía": "zootecnia", "agronomia": "zootecnia",
    "agronómica": "zootécnica", "agronómico": "zootécnico",
    "agronómicas": "zootécnicas", "agronómicos": "zootécnicos",
    "agrícola": "pecuario", "agrícolas": "pecuarios",
    "agricola": "pecuario", "agricolas": "pecuarios",
    "cultivo": "lote", "cultivos": "lotes",
    "café": "ganado", "cafe": "ganado", "papa": "cerdos",
    "arroz": "aves", "maíz": "bovinos", "maiz": "bovinos",
    "trigo": "ovinos", "cacao": "porcinos", "fresa": "caprinos",
    "mora": "ovinos", "caña": "avicultura", "fríjol": "terneros", "frijol": "terneros",
    "semilla": "animal", "semillas": "animales",
    "planta": "animal", "plantas": "animales",
    "parcela": "corral", "parcelas": "corrales",
    "finca": "granja", "fincas": "granjas",
    "suelo": "dieta", "suelos": "dietas",
    "fertilizante": "suplemento", "fertilizantes": "suplementos",
    "abono": "suplemento", "abonos": "suplementos",
    "plaga": "enfermedad", "plagas": "enfermedades",
    "insecto": "parásito", "insectos": "parásitos",
    "riego": "alimentación", "hectárea": "animal", "hectáreas": "animales",
    "hectarea": "animal", "hectareas": "animales",
    "germinación": "supervivencia", "germinacion": "supervivencia",
    "rendimiento": "productividad", "rendimientos": "productividades",
    "fitosanitario": "sanitario", "fitosanitarios": "sanitarios",
    "fitosanitaria": "sanitaria", "fitosanitarias": "sanitarias",
    "variedad": "dieta", "variedades": "dietas",
    "tubérculo": "animal", "tubérculos": "animales",
    "tuberculo": "animal", "tuberculos": "animales",
    "cosecha": "producción", "cosechas": "producciones",
    "mazorca": "animal", "mazorcas": "animales",
    "grano": "animal", "granos": "animales",
    "herbicida": "tratamiento veterinario", "herbicidas": "tratamientos veterinarios",
    "fungicida": "tratamiento veterinario", "fungicidas": "tratamientos veterinarios",
    "pesticida": "tratamiento veterinario", "pesticidas": "tratamientos veterinarios",
    "plaguicida": "tratamiento veterinario", "plaguicidas": "tratamientos veterinarios",
    "nitrógeno": "proteína", "nitrogeno": "proteina",
    "fertilización": "suplementación", "fertilizacion": "suplementacion",
    "fertilizada": "suplementada", "fertilizadas": "suplementadas",
    "fertilizado": "suplementado", "fertilizados": "suplementados",
    "biofertilizante": "suplemento", "biofertilizantes": "suplementos",
    "insecticida": "antiparasitario", "insecticidas": "antiparasitarios",
    "germina": "sobrevive", "germinan": "sobreviven",
    "germine": "sobreviva", "germinen": "sobrevivan",
    "germinó": "sobrevivió", "germino": "sobrevivio",
    "germinar": "sobrevivir", "germinarán": "sobrevivirán",
    "germinaron": "sobrevivieron", "germinada": "sobreviviente",
    "germinadas": "sobrevivientes", "germinado": "sobreviviente",
    "germinados": "sobrevivientes", "germinaciones": "supervivencias",
    "pregerminación": "evaluación inicial", "pregerminacion": "evaluacion inicial",
    "cafetera": "ganadera", "cafeteras": "ganaderas",
    "cafetero": "ganadero", "cafeteros": "ganaderos",
    "cafetal": "hato", "cafetales": "hatos", "cafetos": "animales",
    "cacaotero": "porcícola", "cacaotera": "porcícola",
    "riegos": "suministros", "moras": "ovinos", "fresas": "caprinos",
    "plantar": "criar", "plantan": "crían", "plantada": "criada", "plantadas": "criadas",
    "sembrar": "asignar", "siembra": "manejo", "sembrada": "asignada", "sembradas": "asignadas",
    "cultiva": "cría", "cosechan": "producen",
    "agronómicamente": "zootécnicamente", "agronomicamente": "zootecnicamente",
    "agrónomo": "zootecnista", "agronomo": "zootecnista",
    "agrónomos": "zootecnistas", "agronomos": "zootecnistas",
    "cenicafé": "Cenizoo", "fedepapa": "Porkcolombia", "fedearroz": "Dieta",
    "tomate": "cerdos", "tomates": "cerdos",
    "aguacate": "ternero", "aguacates": "terneros",
    "uchuva": "corderos", "uchuvas": "corderos",
    "mango": "bovinos", "mangos": "bovinos",
    "flores": "aves", "flor": "ave", "claveles": "aves", "clavel": "ave",
    "girasol": "ovinos", "girasoles": "ovinos",
    "árbol": "animal", "árboles": "animales", "arbol": "animal", "arboles": "animales",
    "vivero": "criadero", "viveros": "criaderos",
    "invernadero": "instalación", "invernaderos": "instalaciones",
    "hongo": "enfermedad", "hongos": "enfermedades",
    "roya": "mastitis", "broca": "parásito", "trips": "parásitos",
    "sacos": "animales", "saco": "animal",
    "hilera": "corral", "hileras": "corrales", "surco": "corral", "surcos": "corrales",
    "helada": "estrés térmico", "heladas": "episodios de estrés térmico",
    "sombra": "refugio", "sombras": "refugios",
    "agricultor": "productor", "agricultores": "productores",
    "semillero": "criadero", "semilleros": "criaderos",
    "foliar": "proteico", "foliares": "proteicos", "npk": "mineral",
}

WORDS_ECONOMIA = {
    "agronomía": "economía", "agronomia": "economia",
    "agronómica": "económica", "agronómico": "económico",
    "agronómicas": "económicas", "agronómicos": "económicos",
    "agrícola": "económico", "agrícolas": "económicos",
    "agricola": "economico", "agricolas": "economicos",
    "cultivo": "empresa", "cultivos": "empresas",
    "café": "comercio", "cafe": "comercio", "papa": "industria",
    "arroz": "servicios", "maíz": "productos", "maiz": "productos",
    "trigo": "inversiones", "cacao": "ventas", "fresa": "comercio minorista",
    "mora": "cartera", "caña": "manufactura", "fríjol": "productoB", "frijol": "productoB",
    "semilla": "proyecto", "semillas": "proyectos",
    "planta": "empresa", "plantas": "empresas",
    "parcela": "sucursal", "parcelas": "sucursales",
    "finca": "empresa", "fincas": "empresas",
    "suelo": "mercado", "suelos": "mercados",
    "fertilizante": "inversión", "fertilizantes": "inversiones",
    "abono": "inversión", "abonos": "inversiones",
    "plaga": "incumplimiento", "plagas": "incumplimientos",
    "insecto": "defecto", "insectos": "defectos",
    "riego": "financiación", "hectárea": "sucursal", "hectáreas": "sucursales",
    "hectarea": "sucursal", "hectareas": "sucursales",
    "germinación": "éxito", "germinacion": "exito",
    "rendimiento": "rentabilidad", "rendimientos": "rentabilidades",
    "fitosanitario": "calidad", "fitosanitarios": "calidad",
    "fitosanitaria": "calidad", "fitosanitarias": "calidad",
    "variedad": "estrategia", "variedades": "estrategias",
    "tubérculo": "producto", "tubérculos": "productos",
    "tuberculo": "producto", "tuberculos": "productos",
    "cosecha": "ventas", "cosechas": "ventas",
    "mazorca": "producto", "mazorcas": "productos",
    "grano": "producto", "granos": "productos",
    "herbicida": "política", "herbicidas": "políticas",
    "fungicida": "política", "fungicidas": "políticas",
    "pesticida": "política", "pesticidas": "políticas",
    "plaguicida": "política", "plaguicidas": "políticas",
    "nitrógeno": "publicidad", "nitrogeno": "publicidad",
    "fertilización": "inversión", "fertilizacion": "inversion",
    "fertilizada": "financiada", "fertilizadas": "financiadas",
    "fertilizado": "financiado", "fertilizados": "financiados",
    "biofertilizante": "programa", "biofertilizantes": "programas",
    "insecticida": "control", "insecticidas": "controles",
    "germina": "tiene éxito", "germinan": "tienen éxito",
    "germine": "tenga éxito", "germinen": "tengan éxito",
    "germinó": "tuvo éxito", "germino": "tuvo exito",
    "germinar": "tener éxito", "germinarán": "tendrán éxito",
    "germinaron": "tuvieron éxito", "germinada": "exitosa",
    "germinadas": "exitosas", "germinado": "exitoso",
    "germinados": "exitosos", "germinaciones": "éxitos",
    "pregerminación": "evaluación inicial", "pregerminacion": "evaluacion inicial",
    "cafetera": "comercial", "cafeteras": "comerciales",
    "cafetero": "comercial", "cafeteros": "comerciales",
    "cafetal": "mercado", "cafetales": "mercados", "cafetos": "empresas",
    "cacaotero": "comercial", "cacaotera": "comercial",
    "riegos": "evaluaciones", "moras": "créditos", "fresas": "tiendas",
    "plantar": "iniciar", "plantan": "inician", "plantada": "iniciada", "plantadas": "iniciadas",
    "sembrar": "implementar", "siembra": "operación", "sembrada": "implementada", "sembradas": "implementadas",
    "cultiva": "administra", "cosechan": "venden",
    "agronómicamente": "económicamente", "agronomicamente": "economicamente",
    "agrónomo": "economista", "agronomo": "economista",
    "agrónomos": "economistas", "agronomos": "economistas",
    "cenicafé": "Centroeco", "fedepapa": "ANDI", "fedearroz": "Estrategia",
    "tomate": "comercio", "tomates": "comercios",
    "aguacate": "producto", "aguacates": "productos",
    "uchuva": "proyecto", "uchuvas": "proyectos",
    "mango": "cartera", "mangos": "carteras",
    "flores": "transacciones", "flor": "transacción", "claveles": "productos", "clavel": "producto",
    "girasol": "inversiones", "girasoles": "inversiones",
    "árbol": "empresa", "árboles": "empresas", "arbol": "empresa", "arboles": "empresas",
    "vivero": "incubadora", "viveros": "incubadoras",
    "invernadero": "mercado", "invernaderos": "mercados",
    "hongo": "incumplimiento", "hongos": "incumplimientos",
    "roya": "incumplimiento", "broca": "fraude", "trips": "incumplimientos",
    "sacos": "millones", "saco": "millón",
    "hilera": "secuencia", "hileras": "secuencias", "surco": "segmento", "surcos": "segmentos",
    "helada": "recesión", "heladas": "recesiones",
    "sombra": "competencia", "sombras": "competencias",
    "agricultor": "gestor", "agricultores": "gestores",
    "semillero": "incubadora", "semilleros": "incubadoras",
    "foliar": "directa", "foliares": "directas", "npk": "diversificada",
}

CODE_IDENTIFIERS_ZOOTECNIA = {
    "dat_papa": "dat_cerdos", "dat_arroz": "dat_aves", "trt_arroz": "trt_aves",
    "fertilizacion": "suplementacion", "insecticida": "antiparasitario",
    "Fedearroz_": "Dieta_", "fedearroz_": "dieta_",
    "helada": "estres_termico", "Helada": "Estres_termico",
}

CODE_IDENTIFIERS_ECONOMIA = {
    "dat_papa": "dat_industria", "dat_arroz": "dat_servicios", "trt_arroz": "trt_servicios",
    "fertilizacion": "inversion", "insecticida": "control",
    "Fedearroz_": "Estrategia_", "fedearroz_": "estrategia_",
    "helada": "recesion", "Helada": "Recesion",
}

CLEANUP_ZOOTECNIA = [
    ("una animal", "un animal"), ("Una animal", "Un animal"),
    ("la animal", "el animal"), ("La animal", "El animal"),
    ("las animales", "los animales"), ("Las animales", "Los animales"),
    ("una animales", "unos animales"), ("la cerdos", "los cerdos"),
    ("de la cerdos", "de los cerdos"), ("la bovinos", "los bovinos"),
    ("de la bovinos", "de los bovinos"), ("productividad alto", "productividad alta"),
    ("animales de ovinos", "ovinos"), ("animales de caprinos", "caprinos"),
    ("animal de cerdos", "cerdo"), ("animales de cerdos", "cerdos"),
    ("animal de ternero", "ternero"), ("animales de terneros", "terneros"),
    ("la caprinos", "los caprinos"), ("las caprinos", "los caprinos"),
    ("la ovinos", "los ovinos"), ("las ovinos", "los ovinos"),
    ("las bovinos", "los bovinos"),
    ("una ovinos", "unos ovinos"), ("una caprinos", "unos caprinos"),
    ("empresa pecuario", "empresa pecuaria"),
    ("del alimentación", "de la alimentación"),
    ("productividad promedio diferente", "productividad promedio diferente"),
    ("práctica pecuario", "práctica pecuaria"),
    ("región ganado", "región ganadera"),
    ("toneladas por animal", "kg por animal"), ("sacos/animal", "kg/animal"),
    ("sembradas", "asignadas"), ("sembrada", "asignada"),
]

CLEANUP_ECONOMIA = [
    ("una proyecto", "un proyecto"), ("Una proyecto", "Un proyecto"),
    ("la proyecto", "el proyecto"), ("La proyecto", "El proyecto"),
    ("las proyectos", "los proyectos"), ("Las proyectos", "Los proyectos"),
    ("una proyectos", "unos proyectos"), ("rentabilidad alto", "rentabilidad alta"),
    ("empresa económico", "empresa económica"),
    ("proyectos de inversiones", "proyectos de inversión"),
    ("empresas de industria", "empresas industriales"),
    ("empresa de industria", "empresa industrial"),
    ("las créditos", "los créditos"), ("el inversión", "la inversión"),
    ("un inversión", "una inversión"), ("del financiación", "de la financiación"),
    ("el rentabilidad", "la rentabilidad"),
    ("práctica económico", "práctica económica"),
    ("empresas fríos", "empresas industriales"),
    ("empresa fríos", "empresa industrial"),
    ("toneladas por sucursal", "millones por sucursal"), ("sacos/sucursal", "millones/sucursal"),
    ("sembradas", "implementadas"), ("sembrada", "implementada"),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean_separator(text: str) -> str:
    mark = chr(0x2014)
    return text.replace(f" {mark} ", ", ").replace(mark, ",")


def adjust_body_paths(text: str) -> str:
    text = text.replace('src="images/', 'src="../images/')
    text = text.replace("src='images/", "src='../images/")
    text = text.replace("](images/", "](../images/")
    return text


def preserve_initial_case(source: str, replacement: str) -> str:
    if source and source[0].isupper() and replacement:
        return replacement[0].upper() + replacement[1:]
    return replacement


def replace_phrase(text: str, source: str, replacement: str) -> str:
    pattern = re.compile(re.escape(source), re.IGNORECASE)
    return pattern.sub(lambda match: preserve_initial_case(match.group(0), replacement), text)


def replace_word(text: str, source: str, replacement: str) -> str:
    pattern = re.compile(rf"(?<![\w]){re.escape(source)}(?![\w])", re.IGNORECASE)
    return pattern.sub(lambda match: preserve_initial_case(match.group(0), replacement), text)


def adapt(text: str, context: str) -> str:
    if context == "agronomia":
        return clean_separator(adjust_body_paths(text))
    phrases = PHRASES_ZOOTECNIA if context == "zootecnia" else PHRASES_ECONOMIA
    words = WORDS_ZOOTECNIA if context == "zootecnia" else WORDS_ECONOMIA
    result = text
    identifiers = CODE_IDENTIFIERS_ZOOTECNIA if context == "zootecnia" else CODE_IDENTIFIERS_ECONOMIA
    for source, replacement in identifiers.items():
        result = result.replace(source, replacement)
    for source, replacement in phrases:
        result = replace_phrase(result, source, replacement)
    for source, replacement in sorted(words.items(), key=lambda item: len(item[0]), reverse=True):
        result = replace_word(result, source, replacement)
    cleanup = CLEANUP_ZOOTECNIA if context == "zootecnia" else CLEANUP_ECONOMIA
    for source, replacement in cleanup:
        result = replace_phrase(result, source, replacement)
    return clean_separator(adjust_body_paths(result))


def slugify(heading: str) -> str:
    heading = re.sub(r"^##\s+", "", heading).split("{")[0].strip()
    normalized = unicodedata.normalize("NFKD", heading).encode("ascii", "ignore").decode("ascii")
    normalized = re.sub(r"[^a-zA-Z0-9]+", "_", normalized).strip("_").lower()
    return normalized[:60] or "seccion"


def split_yaml_and_body(text: str) -> tuple[str, str]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise RuntimeError("El archivo no comienza con YAML")
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "".join(lines[: index + 1]), "".join(lines[index + 1 :])
    raise RuntimeError("No se encontró el cierre del YAML")


def split_sections(body: str) -> list[str]:
    lines = body.splitlines(keepends=True)
    starts = [index for index, line in enumerate(lines) if line.startswith("## ")]
    if not starts:
        return [body]
    sections = []
    if starts[0] > 0:
        sections.append("".join(lines[: starts[0]]))
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        sections.append("".join(lines[start:end]))
    return sections


def is_contextual(section: str) -> bool:
    heading = section.splitlines()[0] if section.strip() else ""
    return bool(EXAMPLE_HEADING_PATTERN.search(heading) or DOMAIN_PATTERN.search(section))


def yaml_for(class_number: int, context: str, original_yaml: str) -> str:
    label = LABELS[context]
    yaml = original_yaml.replace('title: "Bioestadística Fundamental"', f'title: "Bioestadística, {label}"', 1)
    yaml = yaml.replace("bibliography: referencias.bib", "bibliography: ../referencias.bib", 1)
    yaml = yaml.replace("csl: ieee.csl", f"csl: ../ieee.csl\noutput-file: clase_{class_number}_{context}.html", 1)
    yaml = yaml.replace("logo: images/", "logo: ../images/", 1)
    yaml = yaml.replace("../assets/", "../../assets/")
    yaml = yaml.replace('href="fontawesome-', 'href="../fontawesome-')
    yaml = yaml.replace('src="fontawesome-', 'src="../fontawesome-')
    return clean_separator(yaml)


def generate_class(class_number: int, manifest: list[list[str]]) -> None:
    class_dir = ROOT / f"clase_{class_number}"
    original = class_dir / f"clase_{class_number}.qmd"
    before = sha256(original)
    original_text = original.read_text(encoding="utf-8")
    original_yaml, body = split_yaml_and_body(original_text)
    sections = split_sections(body)
    reconstructed = "".join(sections)
    if reconstructed != body:
        raise RuntimeError(f"La división de clase {class_number} alteró el cuerpo")

    content_dir = class_dir / "contenido"
    content_dir.mkdir(parents=True, exist_ok=True)
    for context in CONTEXTS:
        (class_dir / "ejemplos" / context).mkdir(parents=True, exist_ok=True)
        (class_dir / context).mkdir(parents=True, exist_ok=True)

    includes: dict[str, list[str]] = {context: [] for context in CONTEXTS}
    contextual_count = 0
    shared_count = 0
    for index, section in enumerate(sections):
        first_line = section.splitlines()[0] if section.splitlines() else ""
        filename = f"_{index:03d}_{slugify(first_line)}.qmd"
        contextual = is_contextual(section)
        if contextual:
            contextual_count += 1
            for context in CONTEXTS:
                relative = f"../ejemplos/{context}/{filename}"
                target = class_dir / "ejemplos" / context / filename
                target.write_text(adapt(section, context), encoding="utf-8")
                includes[context].append(f"{{{{< include {relative} >}}}}")
        else:
            shared_count += 1
            target = content_dir / filename
            target.write_text(clean_separator(adjust_body_paths(section)), encoding="utf-8")
            for context in CONTEXTS:
                includes[context].append(f"{{{{< include ../contenido/{filename} >}}}}")

        manifest.append([
            str(class_number), str(index), first_line.removeprefix("## ").strip(),
            "contextual" if contextual else "comun", filename,
        ])

    for context in CONTEXTS:
        main = yaml_for(class_number, context, original_yaml) + "\n" + "\n\n".join(includes[context]) + "\n"
        output_dir = class_dir / context
        target = output_dir / f"clase_{class_number}_{context}.qmd"
        target.write_text(main, encoding="utf-8")
        resources_dir = output_dir / f"clase_{class_number}_{context}_files"
        resources_dir.mkdir(parents=True, exist_ok=True)
        keep = resources_dir / ".gitkeep"
        if not any(resources_dir.iterdir()):
            keep.write_text("", encoding="utf-8")

    if sha256(original) != before:
        raise RuntimeError(f"El original de clase {class_number} fue modificado")
    print(
        f"clase_{class_number}: {len(sections)} módulos, "
        f"{shared_count} comunes, {contextual_count} contextuales, original {before}"
    )


def main() -> None:
    manifest: list[list[str]] = []
    for class_number in range(4, 21):
        generate_class(class_number, manifest)
    manifest_path = ROOT / "MAPA_MODULOS_CLASES_4_20.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["clase", "indice", "seccion", "tipo", "archivo"])
        writer.writerows(manifest)
    print(f"Mapa escrito en {manifest_path}")


if __name__ == "__main__":
    main()
