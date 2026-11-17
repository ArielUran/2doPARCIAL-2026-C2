# Ejercicio 1
class Pokemon:
    def __init__(self, id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion):
        self.id = id
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    def __str__(self):
        if self.tipo2 == "":
            return f"#{self.id} {self.nombre} ({self.tipo1})"
        return f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"

    def __eq__(self, otro):
        return isinstance(otro, Pokemon) and self.id == otro.id


# TEORIA: La identidad es el id y el resto (nombre, tipos, estadísticas, generación) es estado; 
# la identidad no debería poder cambiar después de construido el objeto.