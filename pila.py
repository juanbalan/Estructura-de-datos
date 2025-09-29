class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return "La pila está vacía"

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return "La pila está vacía"

    def mostrar(self):
        return self.items
    

pila = Pila()


pila.push(10)
pila.push(20)
pila.push(30)

print("Pila actual:", pila.mostrar())


print("Elemento en la cima:", pila.peek())


print("Elemento eliminado:", pila.pop())
print("Pila después del pop:", pila.mostrar())
