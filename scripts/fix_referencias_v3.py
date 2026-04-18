"""
Comentario 1: Referencias explícitas a todas las figuras y tablas.
Mapeo correcto: 20 figuras, 24 tablas por orden de aparición.
"""
import re
from pathlib import Path

DOC = Path(r"e:\Maestria\Seminario_De_Investigacion\Investigación\Documento_Tesis.md")
text = DOC.read_text(encoding="utf-8")
changes = 0

# ══════════════════════════════════════════════════════════════════════
# FIGURAS: 14 ocurrencias de "La siguiente figura" → "La Figura N"
# ══════════════════════════════════════════════════════════════════════
fig_replacements = [
    ("La siguiente figura ilustra la fragmentación del sistema de salud", 1),
    ("La siguiente figura presenta la estructura del marco normativo", 2),
    ("La siguiente figura sintetiza las cuatro brechas identificadas", 3),
    ("La siguiente figura resume los indicadores clave que dimensionan", 4),
    ("La siguiente figura presenta la correspondencia entre los problemas específicos", 5),
    ("La siguiente figura presenta una visión integrada de las seis limitaciones", 7),
    ("La siguiente figura presenta la distribución de las 107 incidencias", 8),
    ("La siguiente figura presenta una taxonomía visual de los estándares", 10),
    ("La siguiente figura visualiza la distribución de estos seis enfoques", 14),
    ("La siguiente figura presenta cuatro modelos arquitectónicos", 15),
    ("La siguiente figura ilustra una arquitectura por capas para la interoperabilidad", 16),
    ("La siguiente figura ilustra la relación conceptual entre la variable independiente", 18),
    ("La siguiente figura ilustra esquemáticamente el diseño pre-experimental", 19),
    ("La siguiente figura presenta la representación visual del cronograma", 20),
]

for ctx, num in fig_replacements:
    if ctx in text:
        new = ctx.replace("La siguiente figura", f"La Figura {num}")
        text = text.replace(ctx, new, 1)
        changes += 1
        print(f"  Fig {num}: reemplazada")
    else:
        print(f"  WARN Fig {num}: no encontrado")

# ══════════════════════════════════════════════════════════════════════
# FIGURAS SIN REFERENCIA: 6, 9, 11, 12, 13, 17
# ══════════════════════════════════════════════════════════════════════
fig_inserts = [
    ("alineada a las brechas específicas identificadas en la fase diagnóstica.",
     " La Figura 6 ilustra las fases secuenciales del enfoque metodológico adoptado."),
    ("basándose en su experiencia de implementación de interoperabilidad HL7 FHIR y openEHR en Cataluña.",
     " La Figura 9 presenta la evolución de los principales estándares de interoperabilidad clínica."),
    ("el Modelo de Calidad de Datos sustenta las dimensiones e indicadores de la variable dependiente.",
     " La Figura 11 presenta la articulación de estos cuatro enfoques teóricos con las dimensiones de la investigación."),
    ("la interoperabilidad deben resolverse la interoperabilidad técnica (transferencia fiable) y la interoperabilidad semántica (comprensión mutua).",
     " La Figura 12 ilustra los cuatro niveles de interoperabilidad en salud según el modelo HIMSS."),
    ("avanzando en investigación traslacional y fenotipado.",
     " La Figura 13 presenta los recursos FHIR principales y sus relaciones en el modelo de datos."),
    ("cuyas brechas actuales constituyen el problema de investigación.",
     " La Figura 17 sintetiza el marco conceptual que guía la recolección y el análisis de datos de la investigación."),
]

for anchor, sentence in fig_inserts:
    if anchor in text:
        text = text.replace(anchor, anchor + sentence, 1)
        changes += 1
        fig_n = re.search(r"Figura (\d+)", sentence).group(1)
        print(f"  Fig {fig_n}: insertada referencia")
    else:
        print(f"  WARN: anchor no encontrado: {anchor[:50]}...")

# ══════════════════════════════════════════════════════════════════════
# TABLAS: 7 ocurrencias de "La siguiente tabla" → "La Tabla N"
# ══════════════════════════════════════════════════════════════════════
tbl_replacements = [
    ("La siguiente tabla presenta la correspondencia lógica entre cada hipótesis", 13),
    ("La siguiente tabla detalla la especificación técnica de cada indicador", 14),
    ("La siguiente tabla sintetiza las métricas de resultados reportadas", 15),
    ("La siguiente tabla presenta una síntesis comparativa de los diseños metodológicos", 17),
    ("La siguiente tabla presenta la trazabilidad entre cada técnica de medición", 18),
    ("La siguiente tabla detalla las pruebas estadísticas que se aplicarán", 20),
    ("La siguiente tabla presenta la distribución del presupuesto agrupada", 22),
]

for ctx, num in tbl_replacements:
    if ctx in text:
        new = ctx.replace("La siguiente tabla", f"La Tabla {num}")
        text = text.replace(ctx, new, 1)
        changes += 1
        print(f"  Tbl {num}: reemplazada")
    else:
        print(f"  WARN Tbl {num}: no encontrado")

# ══════════════════════════════════════════════════════════════════════
# TABLAS SIN REFERENCIA: 16, 19, 21, 23, 24
# ══════════════════════════════════════════════════════════════════════
t16_old = "## Matriz de operacionalización de variables\n"
if t16_old in text:
    t16_new = "## Matriz de operacionalización de variables\n\nLa Tabla 16 presenta la matriz de operacionalización de variables, detallando dimensiones, indicadores, escalas, instrumentos y momentos de medición.\n"
    text = text.replace(t16_old, t16_new, 1)
    changes += 1
    print("  Tbl 16: insertada")

t19_old = "el enfoque mixto del estudio requiere técnicas cualitativas que contribuyen"
t19_new = "el enfoque mixto del estudio requiere técnicas cualitativas —detalladas en la Tabla 19— que contribuyen"
if t19_old in text:
    text = text.replace(t19_old, t19_new, 1)
    changes += 1
    print("  Tbl 19: insertada")

t21_old = "A continuación se detalla el presupuesto estimado, organizado por categorías de gasto:"
t21_new = "La Tabla 21 detalla el presupuesto estimado, organizado por categorías de gasto:"
if t21_old in text:
    text = text.replace(t21_old, t21_new, 1)
    changes += 1
    print("  Tbl 21: reemplazada")

t23_old = "El siguiente cronograma distribuye las actividades"
t23_new = "La Tabla 23 distribuye las actividades"
if t23_old in text:
    text = text.replace(t23_old, t23_new, 1)
    changes += 1
    print("  Tbl 23: reemplazada")

t24_old = "## Anexo 1: Matriz de consistencia\n\n: Matriz de consistencia"
t24_new = "## Anexo 1: Matriz de consistencia\n\nLa Tabla 24 presenta la matriz de consistencia que integra problemas, objetivos, hipótesis, variables, indicadores, metodología y técnicas.\n\n: Matriz de consistencia"
if t24_old in text:
    text = text.replace(t24_old, t24_new, 1)
    changes += 1
    print("  Tbl 24: insertada")

# ══════════════════════════════════════════════════════════════════════
# CORRECCIÓN: "conforme a la Tabla 8" → "conforme a la Tabla 18"
# ══════════════════════════════════════════════════════════════════════
if "conforme a la Tabla 8." in text:
    text = text.replace("conforme a la Tabla 8.", "conforme a la Tabla 18.", 1)
    changes += 1
    print("  Corregida 'Tabla 8' → 'Tabla 18'")

# ══════════════════════════════════════════════════════════════════════
# VERIFICACIÓN
# ══════════════════════════════════════════════════════════════════════
res_f = len(re.findall(r"[Ll]a siguiente figura", text))
res_t = len(re.findall(r"[Ll]a siguiente tabla", text))
print(f"\nResiduales: {res_f} 'siguiente figura', {res_t} 'siguiente tabla'")

for n in range(1, 21):
    if not re.search(rf"Figura {n}\b", text):
        print(f"  WARN: Figura {n} sin referencia")
for n in range(1, 25):
    if not re.search(rf"Tabla {n}\b", text):
        print(f"  WARN: Tabla {n} sin referencia")

DOC.write_text(text, encoding="utf-8")
print(f"\nTotal cambios: {changes}")
print("Archivo actualizado.")
