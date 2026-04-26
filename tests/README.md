# `tests/` — Tests del pipeline

Tests unitarios y de arquitectura para el motor en `platform/`.

## Ejecución

```powershell
python -m pytest tests/ -v
```

## Tests incluidos

- `test_paths.py` — valida que constantes de rutas resuelvan a la
  estructura esperada del repo.
- `test_architecture.py` — valida reglas de dependencia entre capas
  (platform no importa content, content no tiene .py, etc.).
- `test_markdown_validation.py` — linter del MD (captions, paths de
  imágenes, citas huérfanas, "siguiente figura/tabla").
- `test_filter_sections.py` — valida `_filtrar_secciones_excluidas`.

Los tests **no** ejecutan pandoc ni postproceso pesado; son rápidos
(< 1 s en total).
