class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = []
        self.tope = 0 
    def esta_vacia(self):
        return self.tope == 0
    def esta_llena(self):
        return self.tope == self.capacidad
    def insertar(self, elemento):
        if self.esta_llena():
            print(f"Error: Desbordamiento. No se puede insertar {elemento}, la pila está llena.")
        else:
            self.items.append(elemento)
            self.tope += 1
            print(f"Insertar({elemento}) -> Pila: {self.items} | Tope = {self.tope}")

    def eliminar(self):
        if self.esta_vacia():
            print("Error: Subdesbordamiento. No se puede eliminar, la pila está vacía.")
        else:
            eliminado = self.items.pop()
            self.tope -= 1
            print(f"Eliminar({eliminado}) -> Pila: {self.items} | Tope = {self.tope}")

pila = Pila(8)

print("=== ESTADO INICIAL ===")
print(f"Pila: {pila.items} | Tope = {pila.tope}\n")


pila.insertar("X")

pila.insertar("Y")

pila.eliminar()

pila.eliminar()

pila.eliminar()

pila.insertar("V")

pila.insertar("W")

pila.eliminar()

pila.insertar("R")

print("\n=== ESTADO FINAL ===")
print(f"Pila final: {pila.items}")
print(f"Elementos en la pila: {pila.tope}/{pila.capacidad}")
