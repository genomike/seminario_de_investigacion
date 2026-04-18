"""
Script para:
1. Poner en negrita los conectores lógicos en los antecedentes (internacionales y nacionales)
2. Corregir mayúsculas incorrectas después de conectores y nombres de autores
"""
import re

filepath = r"e:\Maestria\Seminario_De_Investigacion\Investigación\Documento_Tesis.md"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Delimitar la sección de antecedentes
start_marker = "### Internacionales\n"
end_marker = "### Síntesis crítica de antecedentes"

start_idx = content.index(start_marker)
end_idx = content.index(end_marker)

before = content[:start_idx]
section = content[start_idx:end_idx]
after = content[end_idx:]

print("=== PASO 1: Negrita en conectores lógicos estructurales ===")

# Conectores que separan las partes de cada antecedente (estructurado)
connectors = [
    "En ese marco,",
    "A partir de ello,",
    "Para abordarlo,",
    "Para la evaluación,",
    "Como métricas o indicadores de desempeño,",
    "En términos de resultados,",
    "No obstante,",
    "En relación con esta tesis,",
]

for c in connectors:
    count = section.count(c)
    if count > 0:
        bold_c = f"**{c}**"
        section = section.replace(c, bold_c)
        print(f"  '{c}' → negrita: {count} ocurrencias")

print("\n=== PASO 2: Negrita en conectores de ADELUSI (estilo narrativo) ===")

adelusi_pairs = [
    ("Parten de la fragmentación", "**Parten de** la fragmentación"),
    ("por ello, buscan", "**por ello,** buscan"),
    ("Para ello, desarrollan", "**Para ello,** desarrollan"),
    ("Asimismo, aplican", "**Asimismo,** aplican"),
    ("Sin embargo, el estudio se limita", "**Sin embargo,** el estudio se limita"),
    ("En conjunto, la evidencia", "**En conjunto,** la evidencia"),
]

for old, new in adelusi_pairs:
    if old in section:
        section = section.replace(old, new)
        print(f"  Negrita: '{old[:50]}...'")

print("\n=== PASO 3: Caso especial MAURICIO ('en En Perú') ===")

old_m = "el problema se centró en En Perú no existe"
new_m = "el problema se centró en que en Perú no existe"
if old_m in section:
    section = section.replace(old_m, new_m)
    print("  Corregido: 'en En Perú' → 'en que en Perú'")
else:
    print("  No encontrado (puede ya estar corregido)")

print("\n=== PASO 4: Corregir mayúsculas después de nombres de autores ===")
# **AUTOR (AÑO)** Verbo → **AUTOR (AÑO)** verbo

def fix_author_verb(m):
    return m.group(1) + m.group(2) + m.group(3).lower()

section, n = re.subn(
    r'(\*\*[A-ZÁÉÍÓÚÑ][^*]+\(\d{4}\)\*\*)(\s+)([A-ZÁÉÍÓÚÑ])',
    fix_author_verb,
    section
)
print(f"  Verbos después de autor corregidos: {n}")

print("\n=== PASO 5: Corregir mayúsculas después de frases descriptivas ===")

fixes = [
    ("el problema se centró en", r'(el problema se centró en )([A-ZÁÉÍÓÚÑ])'),
    ("el objetivo se orientó a", r'(el objetivo se orientó a )([A-ZÁÉÍÓÚÑ])'),
    ("se empleó la siguiente metodología:", r'(se empleó la siguiente metodología: )([A-ZÁÉÍÓÚÑ])'),
    ("se utilizaron", r'(\bse utilizaron )([A-ZÁÉÍÓÚÑ])'),
    ("se consideraron", r'(\bse consideraron )([A-ZÁÉÍÓÚÑ])'),
    ("**En términos de resultados,**", r'(\*\*En términos de resultados,\*\* )([A-ZÁÉÍÓÚÑ])'),
    ("**No obstante,**", r'(\*\*No obstante,\*\* )([A-ZÁÉÍÓÚÑ])'),
    ("**En relación con esta tesis,**", r'(\*\*En relación con esta tesis,\*\* )([A-ZÁÉÍÓÚÑ])'),
]

for name, regex in fixes:
    section, n = re.subn(regex, lambda m: m.group(1) + m.group(2).lower(), section)
    if n > 0:
        print(f"  Después de '{name}': {n} corregidas")

print("\n=== PASO 6: Restaurar nombres propios de metodologías ===")

# "Design Science Research" es un nombre propio de metodología
if "design Science Research" in section:
    section = section.replace("design Science Research", "Design Science Research")
    print("  Restaurado: 'Design Science Research'")

# Reconstruir el contenido completo
content = before + section + after

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ Archivo actualizado exitosamente.")
print("  - Conectores lógicos en negrita")
print("  - Mayúsculas corregidas en antecedentes")
