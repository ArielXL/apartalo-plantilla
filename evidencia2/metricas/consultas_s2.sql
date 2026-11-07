-- Evidencia 2 · Ejercicio 6 · Sprint 1 contra Sprint 2.
-- Tablas: `tablero` (fotografía del Sprint 1) y `tablero_s2` (fotografía del Sprint 2).
-- Para ver sus columnas corre primero:
--     python metricas/cargar_tablero.py metricas/tablero.tsv metricas/tablero_s2.tsv
-- Termina cada consulta con punto y coma (;). Las líneas que empiezan con -- son comentarios.

-- a) Puntos comprometidos y entregados de cada sprint, en una sola consulta
--    Pista: SELECT 'Sprint 1' AS sprint, ... FROM tablero WHERE ...  UNION ALL  SELECT 'Sprint 2', ... FROM tablero_s2 WHERE ...


-- b) Velocidad del periodo de cada sprint y del periodo completo (entregados ÷ comprometidos)
--    Cuidado con la división entera: multiplica por 1.0


-- c) Tiempo de ciclo promedio (días de inicio a terminado) de cada sprint
--    Pista: julianday(terminado) - julianday(inicio)


-- d) Historias que pasaron del Sprint 1 al Sprint 2
--    Pista: JOIN de tablero y tablero_s2 por titulo


-- e) Puntos que quedan sin liberar en el backlog y sprints que faltan con tu velocidad del Sprint 2

