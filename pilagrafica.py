import tkinter as tk
from tkinter import messagebox, simpledialog

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0


# ---------------------------
# Interfaz gráfica principal
# ---------------------------
def main():
    pila = Pila()

    def actualizar_pila():
        # limpiar vista anterior
        for widget in frame_pila.winfo_children():
            widget.destroy()

        if pila.esta_vacia():
            label = tk.Label(frame_pila, text="Pila vacía", font=("Arial", 14), fg="red")
            label.pack()
        else:
            # mostrar de arriba hacia abajo
            for elemento in reversed(pila.items):
                bloque = tk.Label(
                    frame_pila,
                    text=str(elemento),
                    font=("Arial", 14),
                    bg="lightblue",
                    width=20,
                    height=2,
                    relief="raised",
                    bd=2
                )
                bloque.pack(pady=2)

    def apilar_elemento():
        elemento = simpledialog.askstring("Apilar", "Ingresa el elemento a apilar:")
        if elemento:
            pila.apilar(elemento)
            actualizar_pila()

    def desapilar_elemento():
        eliminado = pila.desapilar()
        if eliminado:
            messagebox.showinfo("Desapilar", f"✗ Desapilado: {eliminado}")
        else:
            messagebox.showwarning("Error", "La pila está vacía")
        actualizar_pila()

    def ver_cima():
        cima = pila.cima()
        if cima:
            messagebox.showinfo("Cima", f"Elemento en la cima: {cima}")
        else:
            messagebox.showwarning("Cima", "La pila está vacía")

    def salir():
        root.destroy()

    # Ventana principal
    root = tk.Tk()
    root.title("Pila Animada")

    titulo = tk.Label(root, text="MENÚ PILA", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    boton1 = tk.Button(root, text="1. Apilar", width=20, command=apilar_elemento)
    boton1.pack(pady=5)

    boton2 = tk.Button(root, text="2. Desapilar", width=20, command=desapilar_elemento)
    boton2.pack(pady=5)

    boton3 = tk.Button(root, text="3. Ver cima", width=20, command=ver_cima)
    boton3.pack(pady=5)

    boton4 = tk.Button(root, text="4. Salir", width=20, command=salir, fg="red")
    boton4.pack(pady=5)

    # Frame donde se dibuja la pila
    frame_pila = tk.Frame(root, pady=10)
    frame_pila.pack()

    actualizar_pila()  # mostrar pila inicial vacía

    root.mainloop()

if __name__ == "__main__":
    main()
