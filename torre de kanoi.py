class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def __str__(self):
        return f"{self.nombre}: {self.items}"


def mover_discos(n, origen, destino, auxiliar):
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover disco {disco} de {origen.nombre} a {destino.nombre}")
    else:
        mover_discos(n - 1, origen, auxiliar, destino)
        mover_discos(1, origen, destino, auxiliar)
        mover_discos(n - 1, auxiliar, destino, origen)


torre1 = Pila("Torre 1")
torre2 = Pila("Torre 2")
torre3 = Pila("Torre 3")


for disco in range(3, 0, -1):
    torre1.apilar(disco)

print("Estado inicial:")
print(torre1, torre2, torre3, "\n")

mover_discos(3, torre1, torre3, torre2)

print("\nEstado final:")
print(torre1, torre2, torre3)
