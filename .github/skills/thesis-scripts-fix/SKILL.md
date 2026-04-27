---
name: thesis-scripts-fix
description: Diseñar y escribir scripts Python idempotentes para correcciones masivas en `content/manuscript/Documento_Tesis.md`. Usar cuando hay que aplicar el mismo patrón de cambio en >3 lugares, cuando una corrección se repite cada build, o cuando el usuario pide "aplica esto a todos los antecedentes / tablas / figuras".
---

# Scripts de corrección idempotente

## Cuándo escribir un script (en vez de editar a mano)

| Cambio | A mano | Script |
|---|---|---|
| 1-3 reemplazos puntuales | sí | no |
| > 3 reemplazos del mismo patrón | no | **sí** |
| Renumerar tablas o figuras | no | **sí** |
| Insertar conector en cada antecedente | no | **sí** |
| Validar enlaces / DOIs / citas huérfanas | no | **sí** (lectura, no escritura) |
| Cambio estructural (mover sección) | sí, con confirmación | no (es one-shot) |

## Plantilla canónica (Python)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script: fix_<nombre>.py
Objetivo: <una frase>.
Idempotente: sí — verifica antes de tocar.
"""
import sys
from pathlib import Path

DOC = Path("content/manuscript/Documento_Tesis.md")
text = DOC.read_text(encoding="utf-8")
changes = 0
errors = 0

def replace_once(old: str, new: str, label: str = "") -> None:
    global text, changes, errors
    if old not in text:
        # Si el "new" YA está, lo damos por aplicado (idempotencia).
        if new in text:
            print(f"  ·  ya aplicado: {label or old[:60]}")
        else:
            print(f"  ✗  NO ENCONTRADO: {label or old[:60]}", file=sys.stderr)
            errors += 1
        return
    if text.count(old) > 1:
        print(f"  ⚠  AMBIGUO ({text.count(old)} matches): {label}", file=sys.stderr)
        errors += 1
        return
    text = text.replace(old, new, 1)
    changes += 1
    print(f"  ✓  {label or old[:60]}")

# ── reemplazos ────────────────────────────────────────────────────────
replace_once(
    "La siguiente figura ilustra X",
    "La Figura 5 ilustra X",
    "Fig 5 — referencia explícita",
)

# ── escritura ─────────────────────────────────────────────────────────
if errors == 0 and changes > 0:
    DOC.write_text(text, encoding="utf-8")
    print(f"\n✔ {changes} cambios aplicados.")
elif errors > 0:
    print(f"\n✘ {errors} errores; NO se escribió el archivo.", file=sys.stderr)
    sys.exit(1)
else:
    print("\n· nada que cambiar.")
```

## Reglas de oro

1. **Idempotencia**: correr el script dos veces seguidas debe dejar el
   archivo igual la segunda vez. Hacerlo verificando que el `new` ya
   esté presente y, en ese caso, no tocar.
2. **Match único**: si el ancla aparece > 1 vez, **abortar** el reemplazo
   y reportar (es síntoma de ancla mal elegida). Nunca hacer
   reemplazos múltiples ciegos del mismo string.
3. **Anclas largas y específicas** (≥ 60 caracteres del texto real). No
   anclas como `"En ese marco,"` — ese token aparece en cada antecedente.
4. **No regex agresivos**. Si se usa regex, anclar con lookbehind /
   lookahead acotados y probar primero con `Select-String` (read-only).
5. **No escribir si hay errores**. Si alguna ancla no encuentra match,
   abortar y dejar el archivo intacto. Mejor reportar todas las fallas
   antes de pedir intervención humana.
6. **Salida verbose**: una línea por reemplazo (✓), por idempotente (·),
   por error (✗). Un humano debe poder revisar el log.
7. **Ubicación**: `platform/scripts/fixes/fix_<patron>_v<N>.py`. Versionar `vN` cuando se
   itera sobre el mismo tema (no sobrescribir scripts viejos: pueden
   re-correrse en otro fork).

## Catálogo del repo

- [platform/scripts/fixes/template_fix_markdown.py](../../../platform/scripts/fixes/template_fix_markdown.py) —
  plantilla agnóstica para correcciones masivas idempotentes.

Copiar la plantilla y renombrarla según el patrón a corregir. Los scripts
one-off que contengan texto de un tema concreto no deben vivir en `platform/`
después de que el cambio quede consolidado.

## Validaciones útiles (read-only, PowerShell)

```powershell
# Antecedentes que faltan el cierre obligatorio:
Select-String content/manuscript/Documento_Tesis.md -Pattern '^\*\*[A-ZÁÉÍÓÚÑ]+ ET AL\.' -Context 0,40 |
  Where-Object { $_.Context.PostContext -notmatch 'En relación con esta tesis' }

# Captions de tabla mal formados:
Select-String content/manuscript/Documento_Tesis.md -Pattern '^: Tabla \d+\.' -NotMatch |
  Select-String -Pattern '^: '
```

## Anti-patrones

- Reemplazos con `str.replace(old, new)` sin contar ocurrencias previas
  → cambia más de lo esperado.
- Regex con `.*?` ávidos que cruzan líneas y comen otros antecedentes.
- Escribir el archivo aunque hubo errores ("ya lo arreglo después" =
  arrastra el bug).
- Borrar el script tras correrlo: pierde la trazabilidad del cambio.
- Editar `content/manuscript/Documento_Tesis.md` directamente con un one-liner shell sin
  backup: Markdown roto = pandoc roto = tesis no compila.
