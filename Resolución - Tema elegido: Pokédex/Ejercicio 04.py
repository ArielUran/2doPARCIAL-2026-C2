# Ejercicio 4
from ejercicio_02 import PokemonNoEncontrado


class EquipoLlenoError(Exception):
    pass


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.primero
        self.primero = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.primero is None:
            raise IndexError("La lista está vacía")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self._tamanio -= 1
        return dato

    def eliminar(self, id):
        anterior = None
        actual = self.primero
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, id):
        actual = self.primero
        while actual is not None:
            if actual.dato.id == id:
                return actual.dato
            actual = actual.siguiente
        return None

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Equipo:
    MAXIMO = 6

    def __init__(self):
        self._pokemones = ListaEnlazada()

    def agregar(self, pokemon):
        if self._pokemones.tamanio() >= Equipo.MAXIMO:
            raise EquipoLlenoError("El equipo ya tiene 6 Pokémon")
        self._pokemones.insertar_al_final(pokemon)

    def quitar(self, id):
        if not self._pokemones.eliminar(id):
            raise PokemonNoEncontrado(f"El Pokémon con id {id} no está en el equipo")

    def cantidad(self):
        return self._pokemones.tamanio()

    def __iter__(self):
        for pokemon in self._pokemones:
            yield pokemon


# TEORIA: No está guardada en ningún lado: cada nodo solo apunta al siguiente, así que hay
# que recorrer la lista desde `primero` hasta encontrar el nodo cuyo `siguiente` es el último.