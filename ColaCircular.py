class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1

    def esta_vacia(self):
        return self.frente == -1

    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente

    def encolar(self, dato):
        if self.esta_llena():
            print("La cola está llena, no se puede encolar:", dato)
            return
        if self.esta_vacia():
            self.frente = 0
        self.final = (self.final + 1) % self.capacidad
        self.cola[self.final] = dato
        print(f"{dato} agregado a la cola.")

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        dato = self.cola[self.frente]
        if self.frente == self.final:
            self.frente = -1
            self.final = -1
        else:
            self.frente = (self.frente + 1) % self.capacidad
        print(f"{dato} salió de la cola.")
        return dato

    def mostrar(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return
        i = self.frente
        elementos = []
        while True:
            elementos.append(self.cola[i])
            if i == self.final:
                break
            i = (i + 1) % self.capacidad
        print("Cola Circular:", elementos)


# --- Interfaz interactiva ---
def menu():
    capacidad = int(input("Ingrese la capacidad de la cola circular: "))
    cola = ColaCircular(capacidad)

    while True:
        print("\n--- Menú Cola Circular ---")
        print("1. Encolar (Agregar un dato)")
        print("2. Desencolar (Quitar un dato)")
        print("3. Mostrar la cola")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dato = input("Ingrese el valor a encolar: ")
            cola.encolar(dato)
        elif opcion == "2":
            cola.desencolar()
        elif opcion == "3":
            cola.mostrar()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
