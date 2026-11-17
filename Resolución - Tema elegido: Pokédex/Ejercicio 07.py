# Ejercicio 7
def busqueda_lineal(pokemones, campo, valor):
    resultado = []
    for pokemon in pokemones:
        if campo == "nombre" and pokemon.nombre == valor:
            resultado.append(pokemon)
        elif campo == "tipo" and (pokemon.tipo1 == valor or pokemon.tipo2 == valor):
            resultado.append(pokemon)
        elif campo == "nro" and pokemon.id == valor:
            resultado.append(pokemon)
    return resultado


def busqueda_binaria(pokemones, campo, valor):
    inicio = 0
    fin = len(pokemones) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        pokemon = pokemones[medio]
        if campo == "nombre":
            actual = pokemon.nombre
        else:
            actual = pokemon.id
        if actual == valor:
            return pokemon
        if actual < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None


# TEORIA: No: la búsqueda binaria descarta la mitad de la lista suponiendo que está ordenada
# por ese campo; con otro orden puede descartar justo la mitad donde estaba el valor.