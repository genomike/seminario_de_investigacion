"""Renderiza todos los diagramas PlantUML (.puml -> .png) del repositorio."""
import pathlib
import subprocess
import sys

# Layout: <repo>/platform/scripts/build/build_diagrams.py
REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
DIAGRAMS_DIR = REPO_ROOT / "content" / "media" / "diagrams"
FIGURES_DIR = REPO_ROOT / "content" / "media" / "figures"
PLANTUML_JAR = REPO_ROOT / "platform" / "tools" / "plantuml.jar"

# Compatibilidad con código existente
MEDIA = DIAGRAMS_DIR
DIAGRAMS_DIR.mkdir(parents=True, exist_ok=True)
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Raw strings to keep \n as literal backslash-n in .puml files.
# Placeholders {o1},{i1},{e1},{u1},{a1} → accented chars via .replace().

_FT = r"""@startuml diagrama-fundamentacion-teorica
!theme plain
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam defaultFontSize 12
skinparam shadowing false

skinparam rectangle {
    RoundCorner 15
    FontSize 13
    BorderColor #555555
}

skinparam package {
    BackgroundColor #FAFAFA
    BorderColor #888888
    FontSize 14
    FontStyle bold
}

title <b>Enfoques te{o1}ricos que sustentan la investigaci{o1}n</b>

package "Fundamentaci{o1}n Te{o1}rica" as FT {

    rectangle "<b>Teor{i1}a General</b>\n<b>de Sistemas</b>\n(von Bertalanffy, 1968)" as TGS #FFE0B2 {
    }

    rectangle "<b>Enfoque</b>\n<b>Sociot{e1}cnico</b>\n(Emery y Trist, 1960)" as SOC #C8E6C9 {
    }

    rectangle "<b>Teor{i1}a de Difusi{o1}n</b>\n<b>de Innovaciones</b>\n(Rogers, 2003)" as DIF #BBDEFB {
    }

    rectangle "<b>Modelo de Calidad</b>\n<b>de Datos</b>\n(Wang y Strong, 1996)" as CAL #F8BBD0 {
    }
}

note bottom of TGS
  Interoperabilidad como
  propiedad emergente de
  subsistemas articulados
end note

note bottom of SOC
  Optimizaci{o1}n conjunta de
  componentes t{e1}cnicos,
  organizacionales y humanos
end note

note bottom of DIF
  Adopci{o1}n de FHIR seg{u1}n
  ventaja relativa, compatibilidad,
  complejidad, experimentabilidad
end note

note bottom of CAL
  Dimensiones: contextual,
  representacional, accesibilidad,
  integridad referencial
end note

@enduml
"""

_MC = r"""@startuml diagrama-marco-conceptual
!theme plain
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam defaultFontSize 11
skinparam shadowing false
skinparam nodesep 60
skinparam ranksep 40

skinparam rectangle {
    RoundCorner 10
    BorderColor #555555
}

skinparam card {
    BorderColor #777777
    BackgroundColor #FFFDE7
    FontSize 11
}

title <b>Marco Conceptual</b>

together {
    rectangle "<b>Variable</b>\n<b>Independiente</b>" as VI #FFF9C4 {
    }

    rectangle "<i>Modelo de interoperabilidad</i>\n<i>basado en HL7 FHIR</i>" as MOD #FFE082 {
    }
}

together {
    rectangle "<b>Variable</b>\n<b>Dependiente</b>" as VD #E3F2FD {
    }

    rectangle "<i>Calidad del intercambio</i>\n<i>de informaci{o1}n cl{i1}nica</i>" as CAL #90CAF9 {
    }
}

VI -right-> MOD : " Soluci{o1}n\n y/o Propuesta"
VD -right-> CAL : "  Problema"

card "<b>Dimensiones / Categor{i1}as (VI)</b>\n\n1. <b>Diagn{o1}stico (Fase 1):</b> Cumplimiento\n   normativo, adopci{o1}n de est{a1}ndares,\n   codificaci{o1}n, seguridad, infraestructura\n\n2. <b>Implementaci{o1}n piloto (Fase 2):</b> Capa\n   de integraci{o1}n FHIR, mapeo de datos,\n   servicio de intercambio, capacitaci{o1}n\n\n3. <b>Evaluaci{o1}n de impacto (Fase 3):</b>\n   Comparaci{o1}n pre/post de indicadores\n   de calidad" as DIM_VI #FFF8E1

card "<b>Dimensiones / Categor{i1}as (VD)</b>\n\n1. <b>Integridad de datos:</b> Completitud HCE,\n   codificaci{o1}n CIE-10, codificaci{o1}n CPMS\n\n2. <b>Duplicidad:</b> Tasa de duplicidad de\n   pacientes, tasa de duplicidad de ex{a1}menes\n\n3. <b>Eficiencia administrativa:</b> Tiempo\n   promedio de validaci{o1}n de prestaciones SIS\n\n4. <b>Continuidad y trazabilidad:</b> Continuidad\n   de atenci{o1}n, trazabilidad de accesos" as DIM_VD #E3F2FD

MOD -down-> DIM_VI
CAL -down-> DIM_VD

@enduml
"""


_NIV = r"""@startuml diagrama-niveles-interoperabilidad
!theme plain
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam defaultFontSize 12
skinparam shadowing false
skinparam rectangle {
    RoundCorner 12
    BorderColor #555555
    FontSize 13
}

title <b>Niveles de interoperabilidad en salud (HIMSS)</b>

rectangle "<b>Nivel 4: Organizacional</b>\nPol{i1}ticas, gobernanza, acuerdos\ninstitucionales, aspectos legales\ny {e1}ticos del intercambio" as N4 #E1BEE7

rectangle "<b>Nivel 3: Sem{a1}ntico</b>\nDatos interpretados con el mismo\nsignificado cl{i1}nico (CIE-10,\nSNOMED-CT, LOINC, CPMS)" as N3 #BBDEFB

rectangle "<b>Nivel 2: Estructural</b>\nFormato y organizaci{o1}n\ndel intercambio (HL7 FHIR,\nCDA, recursos, perfiles)" as N2 #C8E6C9

rectangle "<b>Nivel 1: Fundacional</b>\nRequisitos de interconexi{o1}n\nb{a1}sica (redes, transporte,\nprotocolos TCP/IP, HTTPS)" as N1 #FFE0B2

N4 -[hidden]down- N3
N3 -[hidden]down- N2
N2 -[hidden]down- N1

note right of N4
  Regulado en Per{u1} por
  RNIEDS (RM 464-2019)
  y PIDESALUD (RM 1193-2019)
end note

note right of N2
  HL7 FHIR opera en
  niveles 2 y 3
end note

@enduml
"""

_EVOL = r"""@startuml diagrama-evolucion-estandares
!theme plain
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam defaultFontSize 11
skinparam shadowing false

title <b>Evoluci{o1}n de est{a1}ndares de interoperabilidad cl{i1}nica</b>

concise "Est{a1}ndares HL7" as HL7
concise "Contexto Per{u1}" as PERU

@0
HL7 is "HL7 v2\n(Mensajer{i1}a)"

@6
HL7 is "HL7 v3 / CDA\n(Documentos)"

@12
HL7 is "HL7 FHIR\n(APIs REST)"

@17
HL7 is "FHIR R4\n(Estable)"

@0
PERU is {hidden}

@8
PERU is "Ley 30024\nRENHICE (2013)"

@13
PERU is "IEDS / RNIEDS\nPIDESALUD\n(2018-2019)"

@17
PERU is "Pilotos\nnacionales\n(2022-2026)"

highlight 12 to 20 #E8F5E9 : Era FHIR

@enduml
"""

_FHIR_RES = r"""@startuml diagrama-recursos-fhir
!theme plain
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam defaultFontSize 11
skinparam shadowing false
skinparam rectangle {
    RoundCorner 10
    BorderColor #555555
}
skinparam card {
    BorderColor #777777
    FontSize 11
}

title <b>Recursos FHIR principales y sus relaciones</b>

rectangle "<b>Patient</b>\nDatos demogr{a1}ficos\ndel paciente" as PAT #BBDEFB

rectangle "<b>Encounter</b>\nContacto asistencial\n(consulta, internamiento)" as ENC #C8E6C9

rectangle "<b>Condition</b>\nDiagn{o1}sticos\n(codificaci{o1}n CIE-10)" as COND #FFE0B2

rectangle "<b>Observation</b>\nResultados cl{i1}nicos\n(lab, signos vitales)" as OBS #FFF9C4

rectangle "<b>Procedure</b>\nProcedimientos\n(codificaci{o1}n CPMS)" as PROC #F8BBD0

rectangle "<b>Practitioner</b>\nProfesional\nde salud" as PRAC #E1BEE7

rectangle "<b>Organization</b>\nEstablecimiento\nde salud (IPRESS)" as ORG #D7CCC8

rectangle "<b>Bundle</b>\nContenedor de\nm{u1}ltiples recursos" as BUND #E0E0E0

PAT -down-> ENC : "subject"
ENC -down-> COND : "encounter"
ENC -down-> OBS : "encounter"
ENC -down-> PROC : "encounter"
ENC -right-> PRAC : "participant"
ENC -left-> ORG : "serviceProvider"
BUND .down.> PAT : "entry"
BUND .down.> ENC : "entry"

@enduml
"""

PLACEHOLDER_MAP = {
    "{a1}": "á",
    "{e1}": "é",
    "{i1}": "í",
    "{o1}": "ó",
    "{u1}": "ú",
    "{n1}": "ñ",
    "{N1}": "Ñ",
}


def _accent(s: str) -> str:
    out = s
    for token, val in PLACEHOLDER_MAP.items():
        out = out.replace(token, val)
    return out


def _decode_output(raw: bytes) -> str:
    if not raw:
        return ""
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def _render_puml_file(puml_file: pathlib.Path, jar: pathlib.Path) -> bool:
    """Renderiza un .puml individual a PNG sin sobrescribir el fuente."""
    output_png = FIGURES_DIR / f"{puml_file.stem}.png"
    temp_puml = None
    temp_png = None

    try:
        source_for_render = puml_file
        source_text = puml_file.read_text(encoding="utf-8")

        # Soporta placeholders de acentos sin tocar el .puml original.
        if any(token in source_text for token in PLACEHOLDER_MAP):
            temp_puml = puml_file.with_name(f"{puml_file.stem}.__render__.puml")
            temp_puml.write_text(_accent(source_text), encoding="utf-8")
            source_for_render = temp_puml
            temp_png = FIGURES_DIR / f"{temp_puml.stem}.png"

        cmd = [
            "java",
            "-Dfile.encoding=UTF-8",
            "-jar",
            str(jar),
            "-charset",
            "UTF-8",
            "-tpng",
            str(source_for_render),
            "-o",
            str(FIGURES_DIR),
        ]
        print(f"Generando: {output_png.name} ...")
        result = subprocess.run(cmd, capture_output=True, check=False)
        if result.returncode != 0:
            stderr = _decode_output(result.stderr)
            print(f"  ERROR: {stderr.strip() or 'falló PlantUML sin stderr'}")
            return False

        # Si se renderizó desde archivo temporal, renombrar al nombre final.
        if temp_png and temp_png.exists():
            if output_png.exists():
                output_png.unlink()
            temp_png.replace(output_png)

        if not output_png.exists():
            print(f"  ERROR: no se encontró el PNG de salida esperado: {output_png.name}")
            return False

        print(f"  OK: {output_png.name}")
        return True
    finally:
        if temp_puml and temp_puml.exists():
            temp_puml.unlink()
        if temp_png and temp_png.exists():
            temp_png.unlink()


def main():
    jar = PLANTUML_JAR
    if not jar.exists():
        print(f"ERROR: plantuml.jar no encontrado en {jar}")
        sys.exit(1)

    puml_files = sorted(DIAGRAMS_DIR.glob("*.puml"))
    if not puml_files:
        print(f"No se encontraron .puml en {DIAGRAMS_DIR}")
        return

    print(f"Renderizando {len(puml_files)} diagrama(s) desde {DIAGRAMS_DIR}...")
    ok = 0
    failed = 0
    for puml_file in puml_files:
        if _render_puml_file(puml_file, jar):
            ok += 1
        else:
            failed += 1

    print(f"Resumen PlantUML: OK={ok}, ERROR={failed}")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
