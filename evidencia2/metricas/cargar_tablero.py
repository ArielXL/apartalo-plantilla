"""Carga una o varias fotografías de tu tablero en una base SQLite (versión 2, Evidencia 2).

Uso:
    python metricas/cargar_tablero.py metricas/tablero.tsv
    python metricas/cargar_tablero.py metricas/tablero.tsv metricas/tablero_s2.tsv --sql metricas/consultas_s2.sql

- Acepta el .tsv que exporta GitHub Projects (Export view data) o un .csv que llenes a mano.
- Cada archivo se vuelve una tabla con el nombre del archivo sin extensión:
  tablero.tsv → tabla `tablero` (Sprint 1) · tablero_s2.tsv → tabla `tablero_s2` (Sprint 2).
  Si el nombre termina en "_manual" se quita: tablero_manual.csv → `tablero`, tablero_s2_manual.csv → `tablero_s2`.
- La base se guarda junto al primer archivo como tablero.db (se reemplaza cada vez).
- Los nombres de columna se pasan a minúsculas, sin acentos y con guion bajo:
  "Title" → titulo, "Status" → estado, "Labels" → etiquetas, "Puntos" → puntos,
  "Prioridad" → prioridad, "Sprint" → sprint, "Inicio" → inicio, "Terminado" → terminado.
- Las fechas se guardan como texto AAAA-MM-DD, para que funcione julianday() en SQLite.
- Solo usa la biblioteca estándar de Python: no hay que instalar nada.
"""
import argparse
import csv
import re
import sqlite3
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

ALIAS = {"title": "titulo", "status": "estado", "labels": "etiquetas", "assignees": "responsables"}
FORMATOS_FECHA = ("%Y-%m-%d", "%b %d, %Y", "%B %d, %Y", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y")


def normalizar_columna(nombre):
    texto = unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode()
    texto = re.sub(r"[^a-z0-9]+", "_", texto.strip().lower()).strip("_")
    return ALIAS.get(texto, texto) or "columna"


def convertir(valor):
    valor = valor.strip()
    if valor == "":
        return None
    for formato in FORMATOS_FECHA:
        try:
            return datetime.strptime(valor, formato).strftime("%Y-%m-%d")
        except ValueError:
            pass
    try:
        numero = float(valor)
        return int(numero) if numero.is_integer() else numero
    except ValueError:
        return valor


def leer_archivo(ruta):
    delimitador = "\t" if ruta.suffix.lower() in (".tsv", ".txt") else ","
    with open(ruta, newline="", encoding="utf-8-sig") as archivo:
        lector = csv.reader(archivo, delimiter=delimitador)
        encabezado = next(lector)
        filas = [fila for fila in lector if any(celda.strip() for celda in fila)]
    columnas = []
    for nombre in encabezado:
        columna = normalizar_columna(nombre)
        while columna in columnas:
            columna += "_2"
        columnas.append(columna)
    datos = [[convertir(celda) for celda in fila + [""] * (len(columnas) - len(fila))] for fila in filas]
    return columnas, datos


def nombre_tabla(ruta):
    nombre = normalizar_columna(ruta.stem)
    if nombre.endswith("_manual"):
        nombre = nombre[: -len("_manual")]
    return nombre or "tablero"


def cargar(conexion, tabla, columnas, datos):
    conexion.execute(f"DROP TABLE IF EXISTS {tabla}")
    conexion.execute(f"CREATE TABLE {tabla} ({', '.join(columnas)})")
    marcas = ", ".join("?" for _ in columnas)
    conexion.executemany(f"INSERT INTO {tabla} VALUES ({marcas})", [fila[: len(columnas)] for fila in datos])
    conexion.commit()


def imprimir_tabla(cursor):
    nombres = [descripcion[0] for descripcion in cursor.description]
    filas = cursor.fetchall()
    anchos = [max(len(str(x)) for x in [n] + [f[i] for f in filas]) for i, n in enumerate(nombres)]
    print(" | ".join(n.ljust(a) for n, a in zip(nombres, anchos)))
    print("-+-".join("-" * a for a in anchos))
    for fila in filas:
        print(" | ".join(str(v).ljust(a) for v, a in zip(fila, anchos)))
    print()


def correr_consultas(conexion, ruta_sql):
    texto = Path(ruta_sql).read_text(encoding="utf-8")
    sin_comentarios = "\n".join(linea for linea in texto.splitlines() if not linea.strip().startswith("--"))
    consultas = [c.strip() for c in sin_comentarios.split(";") if c.strip()]
    if not consultas:
        print("No encontré consultas en", ruta_sql)
    for numero, consulta in enumerate(consultas, start=1):
        print(f"── Consulta {numero} ──")
        print(consulta)
        print()
        try:
            imprimir_tabla(conexion.execute(consulta))
        except sqlite3.Error as error:
            print("ERROR:", error, "\n")


def main():
    parser = argparse.ArgumentParser(description="Carga uno o varios tableros exportados en SQLite.")
    parser.add_argument("archivos", nargs="+", help="tablero.tsv, tablero_s2.tsv, o sus versiones _manual.csv")
    parser.add_argument("--sql", help="archivo .sql con tus consultas")
    parser.add_argument("--db", default=None, help="ruta de la base (por omisión, junto al primer archivo)")
    args = parser.parse_args()

    rutas = [Path(a) for a in args.archivos]
    for ruta in rutas:
        if not ruta.exists():
            sys.exit(f"No existe el archivo {ruta}")
    ruta_db = Path(args.db) if args.db else rutas[0].with_name("tablero.db")
    if ruta_db.exists():
        ruta_db.unlink()
    conexion = sqlite3.connect(ruta_db)
    for ruta in rutas:
        columnas, datos = leer_archivo(ruta)
        tabla = nombre_tabla(ruta)
        cargar(conexion, tabla, columnas, datos)
        print(f"Cargué {len(datos)} filas de {ruta.name} en la tabla `{tabla}`")
        print("  Columnas:", ", ".join(columnas))
    print(f"Base: {ruta_db}")
    print()
    if args.sql:
        correr_consultas(conexion, args.sql)
    conexion.close()


if __name__ == "__main__":
    main()
