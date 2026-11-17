# Ejercicio 10
import struct

from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex
from ejercicio_09 import ArchivoInvalidoError

FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I20s12s12s4H"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)


def guardar_binario(ruta, pokedex):
    pokemones = pokedex.listar()
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, b"AYED", b"P", len(pokemones)))
        for p in pokemones:
            archivo.write(struct.pack(FORMATO_REGISTRO, p.id, p.nombre.encode("utf-8"),
                                      p.tipo1.encode("utf-8"), p.tipo2.encode("utf-8"),
                                      p.hp, p.ataque, p.defensa, p.velocidad))


def cargar_binario(ruta):
    pokedex = Pokedex()
    with open(ruta, "rb") as archivo:
        datos = archivo.read(TAM_ENCABEZADO)
        if len(datos) < TAM_ENCABEZADO:
            raise ArchivoInvalidoError("El archivo es más corto que el encabezado")
        magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos)
        if magia != b"AYED":
            raise ArchivoInvalidoError("Magia inválida")
        for _ in range(cantidad):
            datos = archivo.read(TAM_REGISTRO)
            if len(datos) < TAM_REGISTRO:
                raise ArchivoInvalidoError("Registro incompleto")
            id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad = struct.unpack(FORMATO_REGISTRO, datos)
            pokedex.agregar(Pokemon(id,
                                    nombre.rstrip(b"\0").decode("utf-8"),
                                    tipo1.rstrip(b"\0").decode("utf-8"),
                                    tipo2.rstrip(b"\0").decode("utf-8"),
                                    hp, ataque, defensa, velocidad, 1))
    return pokedex


def actualizar_registro(ruta, posicion, pokemon):
    with open(ruta, "r+b") as archivo:
        datos = archivo.read(TAM_ENCABEZADO)
        if len(datos) < TAM_ENCABEZADO:
            raise ArchivoInvalidoError("El archivo es más corto que el encabezado")
        magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos)
        if magia != b"AYED":
            raise ArchivoInvalidoError("Magia inválida")
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError("Posición fuera de rango")
        archivo.seek(TAM_ENCABEZADO + posicion * TAM_REGISTRO)
        archivo.write(struct.pack(FORMATO_REGISTRO, pokemon.id, pokemon.nombre.encode("utf-8"),
                                  pokemon.tipo1.encode("utf-8"), pokemon.tipo2.encode("utf-8"),
                                  pokemon.hp, pokemon.ataque, pokemon.defensa, pokemon.velocidad))


# TEORIA: El tamaño fijo de cada registro (56 bytes) junto con el tamaño del encabezado (9 bytes): 
# el registro `posicion` empieza en el byte 9 + posicion * 56.