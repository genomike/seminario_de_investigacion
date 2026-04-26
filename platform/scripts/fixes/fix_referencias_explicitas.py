"""
Comentario 1 del asesor: Toda tabla y/o figura debe ser mencionada
de manera explícita en la redacción de párrafos del documento.
Ejemplo: "De acuerdo a la Figura 1 se puede visualizar que..."

Este script:
1. Reemplaza "La siguiente figura" → "la Figura N" (con número correcto)
2. Reemplaza "La siguiente tabla" → "la Tabla N" (con número correcto)
3. Agrega oraciones de referencia explícita donde faltan
4. Corrige la referencia errónea "Tabla 8" → "Tabla 18" en la matriz de consistencia
"""

import re
from pathlib import Path

DOC = Path(r"e:\Maestria\Seminario_De_Investigacion\Investigación\Documento_Tesis.md")

lines = DOC.read_text(encoding="utf-8").split("\n")

# ── 1. Identificar líneas de figuras (![...](...)  excepto logo) ──────────
fig_lines = []  # (line_index, caption)
for i, ln in enumerate(lines):
    m = re.match(r"^!\[(.+?)\]\(", ln)
    if m and "image1.png" not in ln:  # skip logo
        fig_lines.append((i, m.group(1)))

# ── 2. Identificar líneas de tablas (caption `: Título {#tbl:...}` o `: Tabla N.`) ──
tbl_lines = []  # (line_index, caption)
for i, ln in enumerate(lines):
    m = re.match(r"^:\s+(.+?)(?:\s*\{#tbl:[^}]+\})?\s*$", ln)
    if m:
        # Verificar que arriba hay una tabla (|) o que el texto indica tabla
        # Buscar hacia arriba para confirmar que hay una tabla pipe
        has_table = False
        for j in range(i - 1, max(i - 80, 0), -1):
            if lines[j].startswith("|"):
                has_table = True
                break
            if lines[j].startswith("#") or lines[j].startswith("!["):
                break
        if has_table:
            tbl_lines.append((i, m.group(1).strip()))

print(f"Figuras encontradas: {len(fig_lines)}")
for idx, (li, cap) in enumerate(fig_lines, 1):
    print(f"  Figura {idx}: L{li+1} - {cap[:60]}...")

print(f"\nTablas encontradas: {len(tbl_lines)}")
for idx, (li, cap) in enumerate(tbl_lines, 1):
    print(f"  Tabla {idx}: L{li+1} - {cap[:60]}...")

# ── 3. Construir mapas de figura/tabla por línea → número ──────────────
fig_num_by_line = {}
for idx, (li, _) in enumerate(fig_lines, 1):
    fig_num_by_line[li] = idx

tbl_num_by_line = {}
for idx, (li, _) in enumerate(tbl_lines, 1):
    tbl_num_by_line[li] = idx

changes = 0

# ── 4. Reemplazar "La siguiente figura" → "la Figura N" ──────────────
# Para cada ocurrencia, encontrar la siguiente figura (primera ![...] después)
for i, ln in enumerate(lines):
    if "siguiente figura" in ln.lower():
        # Encontrar la siguiente figura después de esta línea
        fig_num = None
        for fi, _ in fig_lines:
            if fi > i:
                fig_num = fig_num_by_line[fi]
                break
        if fig_num is None:
            print(f"  WARN: 'siguiente figura' en L{i+1} sin figura posterior")
            continue

        # Reemplazar: "La siguiente figura" → "la Figura N"
        # Mantener mayúscula si está al inicio de oración
        new_line = ln
        # Patrón: "La siguiente figura" al inicio o después de punto
        new_line = re.sub(
            r"La siguiente figura",
            f"La Figura {fig_num}",
            new_line,
            count=1,
        )
        if new_line != ln:
            lines[i] = new_line
            changes += 1
            print(f"  Reemplazado L{i+1}: 'La siguiente figura' → 'La Figura {fig_num}'")

# ── 5. Reemplazar "La siguiente tabla" → "la Tabla N" ──────────────
for i, ln in enumerate(lines):
    if "siguiente tabla" in ln.lower():
        # Encontrar la siguiente tabla después de esta línea
        tbl_num = None
        for ti, _ in tbl_lines:
            if ti > i:
                tbl_num = tbl_num_by_line[ti]
                break
        if tbl_num is None:
            print(f"  WARN: 'siguiente tabla' en L{i+1} sin tabla posterior")
            continue

        new_line = re.sub(
            r"La siguiente tabla",
            f"La Tabla {tbl_num}",
            ln,
            count=1,
        )
        if new_line != ln:
            lines[i] = new_line
            changes += 1
            print(f"  Reemplazado L{i+1}: 'La siguiente tabla' → 'La Tabla {tbl_num}'")

# ── 6. Agregar referencias explícitas donde NO hay "La siguiente figura/tabla" ──

# Mapas de figuras y tablas que YA tienen referencia en el texto
# (buscar "la Figura N" o "La Figura N" en todo el texto)
text_full = "\n".join(lines)

figs_referenced = set()
for m in re.finditer(r"[Ll]a Figura (\d+)", text_full):
    figs_referenced.add(int(m.group(1)))

tbls_referenced = set()
for m in re.finditer(r"[Ll]a Tabla (\d+)", text_full):
    tbls_referenced.add(int(m.group(1)))

print(f"\nFiguras ya referenciadas: {sorted(figs_referenced)}")
print(f"Tablas ya referenciadas: {sorted(tbls_referenced)}")

# Figuras sin referencia → agregar oración antes de la línea de la figura
# La oración se inserta como línea ANTES de la imagen, después de la línea en blanco

# Texto personalizado para cada figura sin referencia
fig_missing_text = {
    6: "La Figura 6 ilustra las tres fases secuenciales del enfoque metodológico adoptado y su correspondencia con los objetivos de la investigación.",
    9: "La Figura 9 presenta la evolución de los principales estándares de interoperabilidad clínica a lo largo de las últimas décadas.",
    11: "La Figura 11 presenta la articulación de estos cuatro enfoques teóricos con las dimensiones de la investigación.",
    12: "La Figura 12 ilustra los cuatro niveles de interoperabilidad en salud según el modelo HIMSS.",
    13: "La Figura 13 presenta los recursos FHIR principales y sus relaciones en el modelo de datos.",
    17: "La Figura 17 sintetiza el marco conceptual que guía la recolección y el análisis de datos de la investigación.",
}

# Tablas sin referencia → agregar oración
tbl_missing_text = {
    16: "La Tabla 16 presenta la matriz de operacionalización de variables, detallando las dimensiones, indicadores, escalas, instrumentos y momentos de medición de cada variable.",
    19: None,  # ya tiene texto intro, solo necesita agregar mención explícita
    21: None,  # ya tiene texto intro, solo necesita modificar "A continuación"
    23: None,  # ya tiene texto intro, solo necesita agregar mención
    24: "La Tabla 24 presenta la matriz de consistencia que integra problemas, objetivos, hipótesis, variables, indicadores, metodología y técnicas de la investigación.",
}

# Insertar referencias de figuras faltantes (de atrás hacia adelante para no desplazar índices)
inserts = []  # (line_index, text_to_insert_before)

for fig_num in sorted(fig_missing_text.keys(), reverse=True):
    if fig_num in figs_referenced:
        continue
    fig_line_idx = fig_lines[fig_num - 1][0]  # 0-indexed line of ![...]
    text = fig_missing_text[fig_num]

    # Buscar la línea en blanco justo antes de la figura
    insert_idx = fig_line_idx
    # Insertar texto como párrafo ANTES de la imagen
    # Buscar hacia arriba la última línea no vacía antes de la figura
    for j in range(fig_line_idx - 1, max(fig_line_idx - 5, 0), -1):
        if lines[j].strip() == "":
            insert_idx = j + 1  # insertar después de la línea en blanco
            break

    inserts.append((insert_idx, text))

# Insertar referencia para Tabla 16 (antes de la tabla y su sección)
if 16 not in tbls_referenced:
    # La tabla 16 está justo después de "## Matriz de operacionalización de variables"
    tbl16_line = tbl_lines[15][0]  # caption line
    # Buscar la línea del encabezado ## hacia arriba
    for j in range(tbl16_line - 1, max(tbl16_line - 20, 0), -1):
        if lines[j].startswith("## Matriz de operacionalización"):
            # Insertar después de la línea en blanco que sigue al heading
            insert_after = j + 1
            if insert_after < len(lines) and lines[insert_after].strip() == "":
                insert_after += 1
            # Pero solo si la siguiente línea es la tabla
            if lines[insert_after].startswith("|"):
                inserts.append((insert_after, tbl_missing_text[16]))
                print(f"  Insertando ref Tabla 16 en L{insert_after+1}")
            break

# Insertar referencia para Tabla 24 (Matriz consistencia en Anexos)
if 24 not in tbls_referenced and len(tbl_lines) >= 24:
    tbl24_line = tbl_lines[23][0]
    # Buscar línea "## Anexo 1:" hacia arriba
    for j in range(tbl24_line - 1, max(tbl24_line - 10, 0), -1):
        if "Anexo 1" in lines[j]:
            insert_after = j + 1
            if insert_after < len(lines) and lines[insert_after].strip() == "":
                insert_after += 1
            # Verificar que sigue el caption de la tabla
            if lines[insert_after].startswith(":"):
                inserts.append((insert_after, tbl_missing_text[24]))
                print(f"  Insertando ref Tabla 24 en L{insert_after+1}")
            break

# Ordenar inserts de mayor a menor índice para no desplazar
inserts.sort(key=lambda x: x[0], reverse=True)

for insert_idx, text in inserts:
    lines.insert(insert_idx, "")
    lines.insert(insert_idx, text)
    changes += 1
    print(f"  Insertada referencia en L{insert_idx+1}: {text[:50]}...")

# ── 7. Modificar textos para tablas 19, 21, 23 que tienen intro sin número explícito ──

# Tabla 19: Modificar "técnicas cualitativas que contribuyen" → agregar "La Tabla 19 presenta las"
# Buscar la línea que introduce tabla 19
if 19 not in tbls_referenced:
    for i, ln in enumerate(lines):
        if "el enfoque mixto del estudio requiere técnicas cualitativas" in ln:
            lines[i] = ln.replace(
                "el enfoque mixto del estudio requiere técnicas cualitativas que contribuyen",
                "el enfoque mixto del estudio requiere técnicas cualitativas que contribuyen"
            )
            # Mejor: agregar referencia al inicio del párrafo
            lines[i] = re.sub(
                r"Además de las técnicas de medición de variables, el enfoque mixto del estudio requiere técnicas cualitativas que contribuyen",
                f"Además de las técnicas de medición de variables, el enfoque mixto del estudio requiere técnicas cualitativas —detalladas en la Tabla 19— que contribuyen",
                lines[i],
            )
            changes += 1
            print(f"  Tabla 19: agregada referencia explícita en L{i+1}")
            break

# Tabla 21: Modificar "A continuación se detalla el presupuesto"
if 21 not in tbls_referenced:
    for i, ln in enumerate(lines):
        if "A continuación se detalla el presupuesto estimado" in ln:
            lines[i] = ln.replace(
                "A continuación se detalla el presupuesto estimado, organizado por categorías de gasto:",
                f"La Tabla 21 detalla el presupuesto estimado, organizado por categorías de gasto:",
            )
            changes += 1
            print(f"  Tabla 21: agregada referencia explícita en L{i+1}")
            break

# Tabla 23: Modificar "El siguiente cronograma distribuye..."
if 23 not in tbls_referenced:
    for i, ln in enumerate(lines):
        if "El siguiente cronograma distribuye las actividades" in ln:
            lines[i] = ln.replace(
                "El siguiente cronograma distribuye las actividades",
                f"La Tabla 23 distribuye las actividades",
            )
            changes += 1
            print(f"  Tabla 23: agregada referencia explícita en L{i+1}")
            break

# ── 8. Corregir "conforme a la Tabla 8" → "conforme a la Tabla 18" ──────────
# (en la nota de la Matriz de consistencia)
for i, ln in enumerate(lines):
    if "conforme a la Tabla 8" in ln and "Matriz" not in ln:
        # Solo corregir en la nota de la matriz de consistencia (cerca del final)
        if i > 1300:
            lines[i] = ln.replace("conforme a la Tabla 8", "conforme a la Tabla 18")
            changes += 1
            print(f"  Corregida referencia 'Tabla 8' → 'Tabla 18' en L{i+1}")

# ── 9. Escribir resultado ─────────────────────────────────────────────
DOC.write_text("\n".join(lines), encoding="utf-8")
print(f"\nTotal de cambios: {changes}")
print("Archivo actualizado correctamente.")
