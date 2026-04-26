"""
Corrección del script de referencias explícitas.
El script anterior asignó números de tabla incorrectos porque solo detectó 14 de 24 tablas.

Este script:
1. Lee el archivo ya modificado (con figuras correctas, tablas incorrectas)
2. Corrige los números de tabla erróneos
3. Agrega referencias de figuras faltantes (6, 9, 11, 12, 13, 17)
4. Agrega referencias de tablas faltantes (16, 19, 21, 23, 24)
5. Corrige "Tabla 8" → "Tabla 18" en la matriz de consistencia
"""

import re
from pathlib import Path

DOC = Path(r"e:\Maestria\Seminario_De_Investigacion\Investigación\Documento_Tesis.md")

text = DOC.read_text(encoding="utf-8")
lines = text.split("\n")

# ── 1. Corregir números de tabla erróneos ──────────────────────────────
# El script anterior usó numeración basada en 14 tablas en vez de 24.
# Correcciones necesarias (buscar el texto exacto ya insertado):

table_corrections = [
    # (wrong_text, correct_text, context_hint)
    ("La Tabla 4 presenta la correspondencia lógica", "La Tabla 13 presenta la correspondencia lógica", "trazabilidad"),
    ("La Tabla 5 detalla la especificación técnica", "La Tabla 14 detalla la especificación técnica", "indicadores"),
    ("La Tabla 6 sintetiza las métricas de resultados", "La Tabla 15 sintetiza las métricas de resultados", "métricas"),
    ("La Tabla 8 presenta una síntesis comparativa de los diseños metodológicos", "La Tabla 17 presenta una síntesis comparativa de los diseños metodológicos", "diseños"),
    ("La Tabla 9 presenta la trazabilidad entre cada técnica", "La Tabla 18 presenta la trazabilidad entre cada técnica", "técnicas"),
    ("La Tabla 11 detalla las pruebas estadísticas", "La Tabla 20 detalla las pruebas estadísticas", "pruebas"),
    ("La Tabla 13 presenta la distribución del presupuesto", "La Tabla 22 presenta la distribución del presupuesto", "presupuesto"),
]

changes = 0
for wrong, correct, hint in table_corrections:
    if wrong in text:
        text = text.replace(wrong, correct, 1)
        changes += 1
        print(f"  Corregido: '{wrong[:40]}...' → '{correct[:40]}...'")
    else:
        print(f"  WARN: No encontrado '{wrong[:40]}...' ({hint})")

# ── 2. Agregar referencias de figuras faltantes ─────────────────────
# Figuras 6, 9, 11, 12, 13, 17 no tienen referencia en el texto.
# Necesitamos insertar una oración ANTES de cada figura.

fig_inserts = [
    # (text_before_figure_that_identifies_the_location, sentence_to_add)
    (
        # Figura 6: después del párrafo sobre enfoque metodológico
        "que combina diseño técnico de integración con evaluación operacional de resultados alineada a las brechas específicas identificadas en la fase diagnóstica.",
        " La Figura 6 ilustra las tres fases secuenciales del enfoque metodológico adoptado y su correspondencia con los objetivos de la investigación."
    ),
    (
        # Figura 9: después del párrafo sobre desarrollo histórico
        "basándose en su experiencia de implementación de interoperabilidad HL7 FHIR y openEHR en Cataluña.",
        " La Figura 9 presenta la evolución de los principales estándares de interoperabilidad clínica a lo largo de las últimas décadas."
    ),
    (
        # Figura 11: después del párrafo sobre fundamentación teórica
        "el Modelo de Calidad de Datos sustenta las dimensiones e indicadores de la variable dependiente.",
        " La Figura 11 presenta la articulación de estos cuatro enfoques teóricos con las dimensiones de la investigación."
    ),
    (
        # Figura 12: después del párrafo sobre niveles de interoperabilidad HIMSS
        "la interoperabilidad deben resolverse la interoperabilidad técnica (transferencia fiable) y la interoperabilidad semántica (comprensión mutua).",
        " La Figura 12 ilustra los cuatro niveles de interoperabilidad en salud según el modelo HIMSS."
    ),
    (
        # Figura 13: después del párrafo sobre modelos de datos FHIR
        "avanzando en investigación traslacional y fenotipado.",
        " La Figura 13 presenta los recursos FHIR principales y sus relaciones en el modelo de datos."
    ),
    (
        # Figura 17: después del párrafo del marco conceptual
        "cuyas brechas actuales constituyen el problema de investigación.",
        " La Figura 17 sintetiza el marco conceptual que guía la recolección y el análisis de datos."
    ),
]

for anchor, sentence in fig_inserts:
    if anchor in text:
        text = text.replace(anchor, anchor + sentence, 1)
        changes += 1
        print(f"  Insertada ref: {sentence.strip()[:50]}...")
    else:
        print(f"  WARN: Anchor no encontrado: '{anchor[:40]}...'")

# ── 3. Agregar referencia para Tabla 16 (Matriz de operacionalización) ──
# Actualmente: "## Matriz de operacionalización de variables\n\n| Variable |..."
# Necesita un párrafo introductorio con referencia explícita.
tbl16_anchor = "## Matriz de operacionalización de variables\n\n| Variable"
tbl16_replacement = "## Matriz de operacionalización de variables\n\nLa Tabla 16 presenta la matriz de operacionalización de variables, detallando las dimensiones, indicadores, escalas, instrumentos y momentos de medición.\n\n| Variable"
if tbl16_anchor in text:
    text = text.replace(tbl16_anchor, tbl16_replacement, 1)
    changes += 1
    print("  Insertada ref Tabla 16")
else:
    print("  WARN: Anchor Tabla 16 no encontrado")

# ── 4. Tabla 19: agregar referencia explícita en texto existente ──
tbl19_old = "el enfoque mixto del estudio requiere técnicas cualitativas que contribuyen"
tbl19_new = "el enfoque mixto del estudio requiere técnicas cualitativas —detalladas en la Tabla 19— que contribuyen"
if tbl19_old in text:
    text = text.replace(tbl19_old, tbl19_new, 1)
    changes += 1
    print("  Insertada ref Tabla 19")
else:
    print("  WARN: Anchor Tabla 19 no encontrado")

# ── 5. Tabla 21: "A continuación se detalla el presupuesto" → "La Tabla 21 detalla..." ──
tbl21_old = "A continuación se detalla el presupuesto estimado, organizado por categorías de gasto:"
tbl21_new = "La Tabla 21 detalla el presupuesto estimado, organizado por categorías de gasto:"
if tbl21_old in text:
    text = text.replace(tbl21_old, tbl21_new, 1)
    changes += 1
    print("  Insertada ref Tabla 21")
else:
    print("  WARN: Anchor Tabla 21 no encontrado")

# ── 6. Tabla 23: "El siguiente cronograma distribuye" → "La Tabla 23 distribuye..." ──
tbl23_old = "El siguiente cronograma distribuye las actividades"
tbl23_new = "La Tabla 23 distribuye las actividades"
if tbl23_old in text:
    text = text.replace(tbl23_old, tbl23_new, 1)
    changes += 1
    print("  Insertada ref Tabla 23")
else:
    print("  WARN: Anchor Tabla 23 no encontrado")

# ── 7. Tabla 24 (Matriz consistencia en Anexo): agregar párrafo introductorio ──
tbl24_anchor = "## Anexo 1: Matriz de consistencia\n\n: Matriz de consistencia"
tbl24_replacement = "## Anexo 1: Matriz de consistencia\n\nLa Tabla 24 presenta la matriz de consistencia que integra problemas, objetivos, hipótesis, variables, indicadores, metodología y técnicas de la investigación.\n\n: Matriz de consistencia"
if tbl24_anchor in text:
    text = text.replace(tbl24_anchor, tbl24_replacement, 1)
    changes += 1
    print("  Insertada ref Tabla 24")
else:
    print("  WARN: Anchor Tabla 24 no encontrado")

# ── 8. Corregir "conforme a la Tabla 8" → "conforme a la Tabla 18" ──
# (en la nota de la Matriz de consistencia, cerca del final del documento)
tbl8_old = "conforme a la Tabla 8."
tbl8_new = "conforme a la Tabla 18."
if tbl8_old in text:
    text = text.replace(tbl8_old, tbl8_new, 1)
    changes += 1
    print("  Corregida ref 'Tabla 8' → 'Tabla 18'")
else:
    print("  WARN: 'conforme a la Tabla 8' no encontrado")

# ── 9. Verificación final ──────────────────────────────────────────────
# Buscar "La siguiente figura" o "La siguiente tabla" residuales
residual_fig = len(re.findall(r"[Ll]a siguiente figura", text))
residual_tbl = len(re.findall(r"[Ll]a siguiente tabla", text))
print(f"\n  Residuales 'siguiente figura': {residual_fig}")
print(f"  Residuales 'siguiente tabla': {residual_tbl}")

# Verificar que ahora las figuras 1-20 están referenciadas
for n in range(1, 21):
    if f"Figura {n}" not in text:
        print(f"  WARN: Figura {n} no referenciada en el texto")

# Verificar tablas clave
for n in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]:
    if f"Tabla {n} " not in text and f"Tabla {n})" not in text and f"Tabla {n}." not in text and f"Tabla {n}\n" not in text and f"Tabla {n}—" not in text and f"Tabla {n}," not in text:
        # More flexible check
        if not re.search(rf"Tabla {n}\b", text):
            print(f"  WARN: Tabla {n} no referenciada en el texto")

# ── 10. Escribir resultado ──────────────────────────────────────────────
DOC.write_text(text, encoding="utf-8")
print(f"\nTotal de cambios adicionales: {changes}")
print("Archivo actualizado correctamente.")
