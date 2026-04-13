from pathlib import Path
import re

path = Path(r"e:\Maestria\Seminario_De_Investigacion\Investigación\Documento_Tesis.md")
text = path.read_text(encoding="utf-8")
lines = text.splitlines()

label_re = re.compile(
    r"^\*\*(Aporte|Problema|Objetivo|Metodología|Instrumentos de evaluación|Métricas o indicadores de desempeño|Resultados|Limitaciones|Crítica o aporte a la tesis):\*\*\s*(.*)$"
)
author_only_re = re.compile(r"^\*\*[^*].+\*\*$")

required = [
    "Aporte",
    "Problema",
    "Objetivo",
    "Metodología",
    "Instrumentos de evaluación",
    "Métricas o indicadores de desempeño",
    "Resultados",
    "Limitaciones",
    "Crítica o aporte a la tesis",
]


def ensure_period(s: str) -> str:
    s = s.strip()
    if not s:
        return s
    if s[-1] in ".!?":
        return s
    return s + "."


out = []
i = 0
converted = 0

while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    if author_only_re.match(stripped) and ":" not in stripped:
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1

        if j < len(lines):
            first_label = label_re.match(lines[j].strip())
            if first_label and first_label.group(1) == "Aporte":
                fields = {}
                k = j
                while k < len(lines):
                    m = label_re.match(lines[k].strip())
                    if not m:
                        break
                    fields[m.group(1)] = m.group(2).strip()
                    k += 1

                if all(key in fields for key in required):
                    p1_parts = [
                        f"{stripped} {fields['Aporte']}",
                        f"En ese marco, el problema se centró en {fields['Problema']}",
                        f"A partir de ello, el objetivo se orientó a {fields['Objetivo']}",
                        f"Para abordarlo, se empleó la siguiente metodología: {fields['Metodología']}",
                    ]
                    p1 = " ".join(ensure_period(p) for p in p1_parts)

                    p2_parts = [
                        f"Para la evaluación, se utilizaron {fields['Instrumentos de evaluación']}",
                        f"Como métricas o indicadores de desempeño, se consideraron {fields['Métricas o indicadores de desempeño']}",
                        f"En términos de resultados, {fields['Resultados']}",
                        f"No obstante, {fields['Limitaciones']}",
                        f"En relación con esta tesis, {fields['Crítica o aporte a la tesis']}",
                    ]
                    p2 = " ".join(ensure_period(p) for p in p2_parts)

                    out.append(p1)
                    out.append("")
                    out.append(p2)
                    out.append("")

                    while k < len(lines) and not lines[k].strip():
                        k += 1
                    i = k
                    converted += 1
                    continue

    out.append(line)
    i += 1

new_text = "\n".join(out)
if text.endswith("\n"):
    new_text += "\n"

path.write_text(new_text, encoding="utf-8")
print(f"Antecedentes convertidos: {converted}")
