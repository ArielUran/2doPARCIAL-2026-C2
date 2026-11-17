# Ejercicio 8
def ordenar_seleccion(pokemones, campo, descendente):
    atributo = "id" if campo == "nro" else campo
    n = len(pokemones)
    for i in range(n - 1):
        elegido = i
        for j in range(i + 1, n):
            if descendente:
                if getattr(pokemones[j], atributo) > getattr(pokemones[elegido], atributo):
                    elegido = j
            else:
                if getattr(pokemones[j], atributo) < getattr(pokemones[elegido], atributo):
                    elegido = j
        pokemones[i], pokemones[elegido] = pokemones[elegido], pokemones[i]
    return pokemones


def ordenar_insercion(pokemones, campo, descendente):
    atributo = "id" if campo == "nro" else campo
    for i in range(1, len(pokemones)):
        actual = pokemones[i]
        j = i - 1
        while j >= 0:
            if descendente:
                fuera_de_lugar = getattr(pokemones[j], atributo) < getattr(actual, atributo)
            else:
                fuera_de_lugar = getattr(pokemones[j], atributo) > getattr(actual, atributo)
            if not fuera_de_lugar:
                break
            pokemones[j + 1] = pokemones[j]
            j -= 1
        pokemones[j + 1] = actual
    return pokemones


# TEORIA: El de inserción es estable (el de selección no); estable significa que los elementos 
# con la misma clave conservan el orden relativo que tenían antes de ordenar.