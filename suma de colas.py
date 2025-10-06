from collections import deque

class Cola:
    def __init__(self, nombre):
        self.items = deque()
        self.nombre = nombre

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"{self.nombre}: {list(self.items)}"


def sumar_colas(cola1, cola2):
    cola_resultado = Cola("Cola Resultado")

    while not cola1.esta_vacia() and not cola2.esta_vacia():
        num1 = cola1.desencolar()
        num2 = cola2.desencolar()
        cola_resultado.encolar(num1 + num2)

    return cola_resultado

colaA = Cola("Cola A")
colaB = Cola("Cola B")

for n in [3, 4, 2, 8, 12]:
    colaA.encolar(n)
for n in [6, 2, 9, 11, 3]:
    colaB.encolar(n)

print(colaA)
print(colaB)

resultado = sumar_colas(colaA, colaB)
print(resultado)
