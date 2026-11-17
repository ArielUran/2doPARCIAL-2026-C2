# Ejercicio 5
from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:
    def __init__(self):
        self._lista = ListaEnlazada()

    def apilar(self, dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        return self._lista.quitar_primero()

    def ver_tope(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        return self._lista.primero.dato

    def esta_vacia(self):
        return self._lista.esta_vacia()


class HistorialAcciones:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, accion):
        self._pila.apilar(accion)

    def deshacer(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()


# TEORIA: En el tope queda "B". La disciplina se llama LIFO (last in, first out): lo último
# que entra es lo primero que sale.