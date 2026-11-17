# Ejercicio 9
import csv

from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex

COLUMNAS = ["id", "nombre", "tipo1", "tipo2", "hp", "ataque", "defensa", "velocidad", "generacion"]


class ArchivoInvalidoError(Exception):
    pass


def guardar_csv(ruta, pokedex):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(COLUMNAS)
        for p in pokedex.listar():
            escritor.writerow([p.id, p.nombre, p.tipo1, p.tipo2, p.hp, p.ataque,
                               p.defensa, p.velocidad, p.generacion])


def cargar_csv(ruta):
    pokedex = Pokedex()
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        encabezado = next(lector, None)
        if encabezado != COLUMNAS:
            raise ArchivoInvalidoError("El archivo no tiene el encabezado esperado")
        for fila in lector:
            if len(fila) != 9:
                raise ArchivoInvalidoError("Fila con cantidad de columnas incorrecta")
            try:
                pokemon = Pokemon(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]),
                                  int(fila[5]), int(fila[6]), int(fila[7]), int(fila[8]))
            except ValueError:
                raise ArchivoInvalidoError("Número inválido en una fila")
            pokedex.agregar(pokemon)
    return pokedex


# TEORIA: Sí, hay que leer los anteriores: las filas del CSV tienen largo variable, así que
# no se puede saltar directo a la décima. El acceso es secuencial.