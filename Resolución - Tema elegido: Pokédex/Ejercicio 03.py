# Ejercicio 3
def descendientes(origen_id, pokedex, aristas):
    pokedex.obtener(origen_id)
    resultado = []
    for origen, destino in aristas:
        if origen == origen_id:
            pokedex.obtener(destino)
            resultado.append(destino)
            resultado.extend(descendientes(destino, pokedex, aristas))
    return resultado


# TEORIA: Con las aristas (4, 5) y (5, 6):
# descendientes(4) -> agrega 5 y llama descendientes(5)
# descendientes(5) -> agrega 6 y llama descendientes(6)
# descendientes(6) -> caso base, no tiene destinos: []
# Orden en que entran los llamados: 4, 5, 6. Al volver: [6] y luego [5, 6].