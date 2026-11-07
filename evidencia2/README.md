# Archivos de la Evidencia 2

Copia **todo el contenido de esta carpeta** a la raíz de tu repositorio de la Evidencia 1, respetando las carpetas:

| Archivo de esta carpeta | Va en tu repo como… |
|---|---|
| `docs/09_cambio_del_cliente.md` … `docs/14_cierre_v1.md` | `docs/` (se suman a los que ya tienes) |
| `metricas/cargar_tablero.py` | **reemplaza** `metricas/cargar_tablero.py` (la versión nueva carga dos sprints) |
| `metricas/consultas_s2.sql` | `metricas/consultas_s2.sql` |
| `ENTREGA2.md` | raíz |
| `CHANGELOG.md` | raíz |
| `burndown_sprint2.xlsx` | raíz |

**No copies este `README.md`**: tu repo ya tiene el suyo.

Guarda las imágenes nuevas (la gráfica del burndown y la estructura del Ejercicio 5) en tu carpeta `docs/img/`, que ya existe.

Después:

```bash
git add .
git commit -m "Archivos de la Evidencia 2"
git push
```

Comprueba que el script nuevo sigue leyendo tu Sprint 1:

```bash
python metricas/cargar_tablero.py metricas/tablero.tsv
```
