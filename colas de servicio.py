from collections import deque

class Cola:
    def __init__(self, nombre):
        self.items = deque()
        self.nombre = nombre
        self.contador = 1

    def encolar(self):
        numero = f"{self.nombre}-{self.contador}"
        self.items.append(numero)
        print(f"Cliente agregado: {numero}")
        self.contador += 1

    def atender(self):
        if not self.items:
            print(f"No hay clientes en {self.nombre}")
        else:
            cliente = self.items.popleft()
            print(f"Atendiendo a: {cliente}")

    def mostrar(self):
        print(f"{self.nombre}: {list(self.items)}")


servicios = {
    "1": Cola("Servicio 1"),
    "2": Cola("Servicio 2"),
    "3": Cola("Servicio 3")
}

print("=== SISTEMA DE COLAS DE ATENCIÓN ===")
print("Comandos:")
print("  C# -> Nuevo cliente en el servicio # (Ej: C1, C2, C3)")
print("  A# -> Atender cliente del servicio # (Ej: A1, A2, A3)")
print("  M  -> Mostrar estado de las colas")
print("  S  -> Salir del sistema\n")

while True:
    comando = input("Ingrese comando: ").upper()

    if comando == "S":
        print("Saliendo del sistema...")
        break

    elif comando == "M":
        for cola in servicios.values():
            cola.mostrar()

    elif comando.startswith("C") and comando[1:] in servicios:
        servicios[comando[1:]].encolar()

    elif comando.startswith("A") and comando[1:] in servicios:
        servicios[comando[1:]].atender()

    else:
        print( "Comando no válido. Intente nuevamente.")
