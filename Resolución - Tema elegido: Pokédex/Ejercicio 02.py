# Ejercicio 2
class PokemonNoEncontrado(Exception):
    pass


class Pokedex:
    def __init__(self):
        self._pokemones = []

    def agregar(self, pokemon):
        for i in range(len(self._pokemones)):
            if self._pokemones[i].id == pokemon.id:
                self._pokemones[i] = pokemon
                return
        self._pokemones.append(pokemon)

    def obtener(self, id):
        for pokemon in self._pokemones:
            if pokemon.id == id:
                return pokemon
        raise PokemonNoEncontrado(f"No existe el Pokémon con id {id}")

    def listar(self):
        return list(self._pokemones)

    def cantidad(self):
        return len(self._pokemones)


# TEORIA: Quien llama sabe que si el método devolvió algo ese valor es válido y el error no
# pasa desapercibido, en lugar de arrastrar un None que explota más adelante.