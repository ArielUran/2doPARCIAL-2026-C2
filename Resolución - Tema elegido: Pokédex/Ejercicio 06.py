# Ejercicio 6
from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:
    def __init__(self):
        self._lista = ListaEnlazada()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self._lista.quitar_primero()

    def ver_frente(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self._lista.primero.dato

    def esta_vacia(self):
        return self._lista.esta_vacia()


class ColaTurnos:
    def __init__(self):
        self._cola = Cola()

    def encolar(self, pokemon):
        self._cola.encolar(pokemon)

    def siguiente(self):
        return self._cola.desencolar()

    def proximo(self):
        return self._cola.ver_frente()


# TEORIA: Porque la cola es FIFO (first in, first out): sale primero el que entró primero.
# C entró último, así que sale último.