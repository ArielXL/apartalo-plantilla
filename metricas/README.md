# Métricas (Ejercicio 8)

1. El último día del sprint, exporta la vista de tabla de tu Project: **View → Export view data**. GitHub descarga un archivo `.tsv`.
2. Guárdalo aquí como `tablero.tsv`. Esa es tu **fotografía estática**.
3. Cárgalo y mira sus columnas:
   ```bash
   python metricas/cargar_tablero.py metricas/tablero.tsv
   ```
4. Escribe tus consultas en `consultas.sql` y córrelas:
   ```bash
   python metricas/cargar_tablero.py metricas/tablero.tsv --sql metricas/consultas.sql
   ```

**¿No pudiste exportar?** Llena `tablero_manual.csv` a mano (una fila por historia, fechas como `2026-10-28`) y usa ese archivo en lugar del `.tsv`.

`tablero.db` se genera solo y no se sube al repo (está en `.gitignore`).
