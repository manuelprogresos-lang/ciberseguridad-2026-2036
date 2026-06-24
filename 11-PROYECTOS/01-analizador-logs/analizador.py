#!/usr/bin/env python3
"""Analizador sencillo de logs completamente sintéticos."""

from __future__ import annotations
from collections import Counter
from pathlib import Path
import sys


def analizar(ruta: Path) -> tuple[Counter, Counter, Counter]:
    severidades: Counter[str] = Counter()
    ips: Counter[str] = Counter()
    eventos: Counter[str] = Counter()

    with ruta.open("r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, start=1):
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split()
            if len(partes) != 4:
                print(f"Advertencia: línea {numero} ignorada por formato inválido.")
                continue

            _, severidad, ip, evento = partes
            severidades[severidad] += 1
            ips[ip] += 1
            eventos[evento] += 1

    return severidades, ips, eventos


def mostrar(titulo: str, datos: Counter) -> None:
    print(f"\n{titulo}")
    print("-" * len(titulo))
    for elemento, cantidad in datos.most_common():
        print(f"{elemento:<25} {cantidad}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python3 analizador.py datos.log")
        return 1

    ruta = Path(sys.argv[1])
    if not ruta.is_file():
        print(f"Error: no existe el archivo {ruta}")
        return 1

    severidades, ips, eventos = analizar(ruta)
    mostrar("Severidades", severidades)
    mostrar("Direcciones ficticias", ips)
    mostrar("Eventos", eventos)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
