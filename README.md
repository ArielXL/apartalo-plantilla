# Apártalo — <nombre del negocio de tu variante>

> Repositorio de la **Evidencia 1** de *Proyecto de ingeniería de software* (Tecmilenio, CRN 13241).
> Sustituye todo lo que está entre `< >` y borra las líneas de ayuda que empiezan con `>`.

| Dato | |
|---|---|
| Estudiante | `<tu nombre>` |
| Matrícula | `<tu matrícula>` |
| Variante | `<número y nombre, por ejemplo: 1 — Barbería Filo>` |
| Project (tablero) | `<enlace a tu GitHub Project>` |

## Visión del producto
> 🎩 PO · Ejercicio 1, punto 1. De 3 a 5 líneas: qué es la app, para quién y qué problema resuelve.

<tu visión>

## Mi equipo Scrum (los tres sombreros)

| Sombrero | Lo que hago con él en este proyecto |
|---|---|
| 🎩 PO | `<...>` |
| 🎩 SM | `<...>` |
| 🎩 Desarrollador | `<...>` |

## Cómo está organizado este repositorio

| Carpeta o archivo | Qué contiene | Ejercicio |
|---|---|---|
| `docs/01_vision_y_problema.md` | Paradigmas, manifiesto, requisito vs. solución, incertidumbre | 1 |
| Issues `historia` y `epica` + `docs/02_backlog.md` | Product backlog, plantilla invertida, glosario, iceberg | 2 |
| `docs/03_tablero.md` | Columnas, límites WIP, políticas y prácticas de kanban | 3 |
| `docs/04_refinamiento.md` + `features/` | Grooming, carga máxima, división, escenarios BDD, tabla FIT | 4 |
| `docs/05_sprint1.md` | Planeación, bitácora, revisión y retrospectiva | 5 |
| `src/apartalo/` + `tests/` + `docs/06_tdd.md` | Código, pruebas y ciclos de TDD | 6 |
| Issues `rnf` + `docs/07_rnf.md` | Requisitos no funcionales | 7 |
| `metricas/` + `docs/08_metricas.md` | Fotografía del tablero y consultas SQL | 8 |
| `ENTREGA.md` | Enlaces a cada evidencia | Entrega |

## Cómo correr las pruebas

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest                           # todas las pruebas
pytest -m aceptacion             # solo la suite de aceptación
pytest -m unitaria               # solo las unitarias
pytest -m rnf                    # solo las de requisitos no funcionales
```
