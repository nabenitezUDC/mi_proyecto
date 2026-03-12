import random

"""
Clases y Subclases en Python
"""

class Personaje():

    def __init__(self, nombre, vida): 
        self.nombre = nombre
        self._vida = vida

    def esta_vivo(self):
        return self._vida > 0
    
    def atacar(self):
        pass

    def recibir_daño(self, daño):
        self._vida -= daño
        
        print(f"{self.nombre} ha recibido {daño} de danio y tiene {self._vida} de vida restante.")

class Guerrero(Personaje):
    def __init__(self, nombre, vida, ataque, armadura):
        super().__init__(nombre, vida)
        self.ataque = ataque
        self.armadura = armadura

    def atacar(self, enemigo):
        if self.esta_vivo():
            danio = self.ataque - enemigo.armadura
            print(f"{self.nombre} realiza un ataque a {enemigo.nombre} con un danio de {danio}")
            enemigo.recibir_daño(danio)
            
        else:
            print(f"{self.nombre} no puede atacar porque está muerto.")

class Mago(Personaje):
    def __init__(self, nombre, vida, poder_magico, armadura):
        super().__init__(nombre, vida) 
        self.poder_magico = poder_magico
        self.armadura = armadura

    def atacar(self, enemigo):
        if self.esta_vivo():
            danio = self.poder_magico - enemigo.armadura
            print (f"{self.nombre} lanza un hechizo a {enemigo.nombre} causando {danio} de danio.")
            enemigo.recibir_daño(danio)
            
        else:
            print(f"{self.nombre} no puede lanzar hechizos porque está muerto.")

"""
Lista de Personajes
"""
Targaryen = Guerrero("Targaryen", 100, 20, 5)
Arturo = Guerrero("Arturo", 120, 25, 10)
Barfort = Guerrero("Barfort", 90, 15, 8)

Merlin = Mago("Merlin", 80, 25, 3)
Dumbledore = Mago("Dumbledore", 70, 30, 4)
Gandalf = Mago("Gandalf", 90, 35, 5)

lista_personajes = [Targaryen, Merlin, Barfort, Dumbledore, Arturo, Gandalf]

""""
Mostrar resultado de atacar
"""

def mostrar_ataque(personaje):
    print(personaje.atacar())

while True:
    personaje1 = random.choice(lista_personajes)
    personaje2 = random.choice(lista_personajes)

    if personaje1 != personaje2 and personaje1.esta_vivo() and personaje2.esta_vivo():
        print(f"\n{personaje1.nombre} VS {personaje2.nombre}:")
    else:
        print("\nNo se pueden seleccionar personajes iguales o personajes muertos. Seleccionando nuevamente...")
        continue

    while True:
        if personaje1 != personaje2 and personaje1.esta_vivo() and personaje2.esta_vivo():
            print(f"\n{personaje1.nombre} ataca a {personaje2.nombre}:")
            personaje1.atacar(personaje2)
            print(f"\n{personaje2.nombre} ataca a {personaje1.nombre}:")
            personaje2.atacar(personaje1)
            print(" -----------------------------------")

        if not personaje1.esta_vivo() or not personaje2.esta_vivo():
            print("\n¡Un personaje ha muerto! Fin del combate.")
            break

    if not personaje1.esta_vivo() or not personaje2.esta_vivo():
        print("\nFin de la partida.")
        break
