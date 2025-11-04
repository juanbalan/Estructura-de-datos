import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque
import math


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz is None

    
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
            return True
        else:
            return self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if dato == nodo.dato:
            return False  # no duplicados
        elif dato < nodo.dato:
            if nodo.izq is None:
                nodo.izq = Nodo(dato)
                return True
            else:
                return self._insertar(nodo.izq, dato)
        else:
            if nodo.der is None:
                nodo.der = Nodo(dato)
                return True
            else:
                return self._insertar(nodo.der, dato)

    
    def buscar_nodo(self, dato):
        nodo = self.raiz
        while nodo:
            if dato == nodo.dato:
                return nodo
            elif dato < nodo.dato:
                nodo = nodo.izq
            else:
                nodo = nodo.der
        return None

    def buscar(self, dato):
        return self.buscar_nodo(dato) is not None

    
    def preOrden(self):
        res = []
        self._preOrden(self.raiz, res)
        return res

    def _preOrden(self, nodo, res):
        if nodo:
            res.append(nodo.dato)
            self._preOrden(nodo.izq, res)
            self._preOrden(nodo.der, res)

    def inOrden(self):
        res = []
        self._inOrden(self.raiz, res)
        return res

    def _inOrden(self, nodo, res):
        if nodo:
            self._inOrden(nodo.izq, res)
            res.append(nodo.dato)
            self._inOrden(nodo.der, res)

    def postOrden(self):
        res = []
        self._postOrden(self.raiz, res)
        return res

    def _postOrden(self, nodo, res):
        if nodo:
            self._postOrden(nodo.izq, res)
            self._postOrden(nodo.der, res)
            res.append(nodo.dato)

    def recorrido_por_niveles(self):
        res = []
        if not self.raiz:
            return res
        cola = deque([self.raiz])
        while cola:
            n = cola.popleft()
            res.append(n.dato)
            if n.izq: cola.append(n.izq)
            if n.der: cola.append(n.der)
        return res

    
    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.izq), self._altura(nodo.der))

    
    def contar_hojas(self):
        return self._contar_hojas(self.raiz)

    def _contar_hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.izq is None and nodo.der is None:
            return 1
        return self._contar_hojas(nodo.izq) + self._contar_hojas(nodo.der)

    def contar_nodos(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izq) + self._contar_nodos(nodo.der)

    
    def _minimo_nodo(self, nodo):
        if nodo is None:
            return None
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def _maximo_nodo(self, nodo):
        if nodo is None:
            return None
        while nodo.der:
            nodo = nodo.der
        return nodo

    
    def eliminar_predecesor(self, dato):
        self.raiz, eliminado = self._eliminar_predecesor(self.raiz, dato)
        return eliminado

    def _eliminar_predecesor(self, nodo, dato):
        if nodo is None:
            return nodo, False
        if dato < nodo.dato:
            nodo.izq, eliminado = self._eliminar_predecesor(nodo.izq, dato)
        elif dato > nodo.dato:
            nodo.der, eliminado = self._eliminar_predecesor(nodo.der, dato)
        else:
            
            eliminado = True
            if nodo.izq is None:
                return nodo.der, True
            elif nodo.der is None:
                return nodo.izq, True
            
            pre = self._maximo_nodo(nodo.izq)
            nodo.dato = pre.dato
            nodo.izq, _ = self._eliminar_predecesor(nodo.izq, pre.dato)
        return nodo, eliminado

    
    def eliminar_sucesor(self, dato):
        self.raiz, eliminado = self._eliminar_sucesor(self.raiz, dato)
        return eliminado

    def _eliminar_sucesor(self, nodo, dato):
        if nodo is None:
            return nodo, False
        if dato < nodo.dato:
            nodo.izq, eliminado = self._eliminar_sucesor(nodo.izq, dato)
        elif dato > nodo.dato:
            nodo.der, eliminado = self._eliminar_sucesor(nodo.der, dato)
        else:
            eliminado = True
            if nodo.izq is None:
                return nodo.der, True
            elif nodo.der is None:
                return nodo.izq, True
            suc = self._minimo_nodo(nodo.der)
            nodo.dato = suc.dato
            nodo.der, _ = self._eliminar_sucesor(nodo.der, suc.dato)
        return nodo, eliminado

    
    def es_completo(self):
        n = self.contar_nodos()
        return self._es_completo(self.raiz, 0, n)

    def _es_completo(self, nodo, indice, num_nodos):
        if nodo is None:
            return True
        if indice >= num_nodos:
            return False
        return (self._es_completo(nodo.izq, 2 * indice + 1, num_nodos) and
                self._es_completo(nodo.der, 2 * indice + 2, num_nodos))

    
    def es_lleno(self):
        return self._es_lleno(self.raiz)

    def _es_lleno(self, nodo):
        if nodo is None:
            return True
        if (nodo.izq is None) and (nodo.der is None):
            return True
        if (nodo.izq is not None) and (nodo.der is not None):
            return self._es_lleno(nodo.izq) and self._es_lleno(nodo.der)
        return False

    
    def eliminar_arbol(self):
        self.raiz = None


class TreeDrawer:
    def __init__(self, canvas, tree: ArbolBinarioBusqueda):
        self.canvas = canvas
        self.tree = tree
        self.node_radius = 20
        self.x_spacing = 40
        self.y_spacing = 80

    def dibujar(self):
        self.canvas.delete("all")
        if self.tree.raiz is None:
            return
        
        positions = {}
        x_counter = {'x': 0}

        def assign_x(nodo, depth=0):
            if nodo is None:
                return
            assign_x(nodo.izq, depth + 1)
            
            positions[nodo] = (x_counter['x'], depth)
            x_counter['x'] += 1
            assign_x(nodo.der, depth + 1)

        assign_x(self.tree.raiz)
        
        total_width_units = max(1, x_counter['x'])
        width = int(self.canvas.winfo_width() or self.canvas['width'])
        height = int(self.canvas.winfo_height() or self.canvas['height'])
        unit_x = max(self.x_spacing, width / (total_width_units + 1))
        center_x_offset = unit_x

        coords = {}
        for nodo, (x_unit, depth) in positions.items():
            x = center_x_offset + x_unit * unit_x
            y = self.y_spacing/2 + depth * self.y_spacing + 20
            coords[nodo] = (x, y)

        
        for nodo, (x, y) in coords.items():
            if nodo.izq:
                x2, y2 = coords[nodo.izq]
                self.canvas.create_line(x, y, x2, y2, width=2)
            if nodo.der:
                x2, y2 = coords[nodo.der]
                self.canvas.create_line(x, y, x2, y2, width=2)

        
        for nodo, (x, y) in coords.items():
            r = self.node_radius
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="white", outline="black", width=2)
            self.canvas.create_text(x, y, text=str(nodo.dato), font=("Helvetica", 10, "bold"))


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Árbol Binario de Búsqueda - Interactivo (Tkinter)")
        self.tree = ArbolBinarioBusqueda()
        self._build_ui()
        self.drawer = TreeDrawer(self.canvas, self.tree)
        
        self.canvas.bind("<Configure>", lambda e: self.drawer.dibujar())

    def _build_ui(self):
        
        frame_left = ttk.Frame(self.root)
        frame_left.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(frame_left, width=800, height=600, bg="white")
        self.canvas.pack(fill="both", expand=True)

        
        frame_right = ttk.Frame(self.root, width=300)
        frame_right.grid(row=0, column=1, padx=8, pady=8, sticky="ns")
        frame_right.grid_propagate(False)

        
        ttk.Label(frame_right, text="Dato (entero):").pack(pady=(6,0))
        self.entry_dato = ttk.Entry(frame_right)
        self.entry_dato.pack(fill="x", padx=6, pady=4)

        btns = [
            ("Insertar", self._btn_insertar),
            ("Buscar", self._btn_buscar),
            ("Eliminar (Predecesor)", self._btn_eliminar_predecesor),
            ("Eliminar (Sucesor)", self._btn_eliminar_sucesor),
            ("Recorridos", self._btn_mostrar_recorridos),
            ("Recorrido por niveles", self._btn_recorrido_niveles),
            ("Altura", self._btn_altura),
            ("Contar hojas", self._btn_contar_hojas),
            ("Contar nodos", self._btn_contar_nodos),
            ("¿Es completo?", self._btn_es_completo),
            ("¿Es lleno?", self._btn_es_lleno),
            ("Eliminar árbol", self._btn_eliminar_arbol),
            ("Limpiar salida", self._btn_limpiar_salida)
        ]

        for (text, cmd) in btns:
            ttk.Button(frame_right, text=text, command=cmd).pack(fill="x", padx=6, pady=3)

        
        ttk.Label(frame_right, text="Salida:").pack(pady=(8,0))
        self.txt_salida = tk.Text(frame_right, height=12, wrap="word")
        self.txt_salida.pack(fill="both", padx=6, pady=(0,6), expand=True)

    
    def _leer_dato(self):
        s = self.entry_dato.get().strip()
        if s == "":
            messagebox.showwarning("Entrada", "Ingresa un número entero.")
            return None
        try:
            return int(s)
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero válido.")
            return None

    def _actualizar_dibujo(self):
        self.drawer.dibujar()

    def _escribir_salida(self, texto, newline=True):
        if newline:
            self.txt_salida.insert("end", str(texto) + "\n")
        else:
            self.txt_salida.insert("end", str(texto))
        self.txt_salida.see("end")

    def _btn_insertar(self):
        dato = self._leer_dato()
        if dato is None:
            return
        ok = self.tree.insertar(dato)
        if ok:
            self._escribir_salida(f"Insertado: {dato}")
        else:
            self._escribir_salida(f"Valor {dato} ya existe (no se insertó).")
        self._actualizar_dibujo()

    def _btn_buscar(self):
        dato = self._leer_dato()
        if dato is None:
            return
        found = self.tree.buscar(dato)
        self._escribir_salida(f"Buscar {dato}: {'Encontrado' if found else 'No encontrado'}")

    def _btn_eliminar_predecesor(self):
        dato = self._leer_dato()
        if dato is None:
            return
        eliminado = self.tree.eliminar_predecesor(dato)
        self._escribir_salida(f"Eliminar (predecesor) {dato}: {'Eliminado' if eliminado else 'No encontrado'}")
        self._actualizar_dibujo()

    def _btn_eliminar_sucesor(self):
        dato = self._leer_dato()
        if dato is None:
            return
        eliminado = self.tree.eliminar_sucesor(dato)
        self._escribir_salida(f"Eliminar (sucesor) {dato}: {'Eliminado' if eliminado else 'No encontrado'}")
        self._actualizar_dibujo()

    def _btn_mostrar_recorridos(self):
        pre = self.tree.preOrden()
        ino = self.tree.inOrden()
        post = self.tree.postOrden()
        self._escribir_salida(f"PreOrden: {pre}")
        self._escribir_salida(f"InOrden : {ino}")
        self._escribir_salida(f"PostOrden: {post}")

    def _btn_recorrido_niveles(self):
        r = self.tree.recorrido_por_niveles()
        self._escribir_salida(f"Por niveles: {r}")

    def _btn_altura(self):
        h = self.tree.altura()
        self._escribir_salida(f"Altura (nodos): {h}")

    def _btn_contar_hojas(self):
        c = self.tree.contar_hojas()
        self._escribir_salida(f"Hojas: {c}")

    def _btn_contar_nodos(self):
        c = self.tree.contar_nodos()
        self._escribir_salida(f"Nodos: {c}")

    def _btn_es_completo(self):
        r = self.tree.es_completo()
        self._escribir_salida(f"Es completo: {'Sí' if r else 'No'}")

    def _btn_es_lleno(self):
        r = self.tree.es_lleno()
        self._escribir_salida(f"Es lleno: {'Sí' if r else 'No'}")

    def _btn_eliminar_arbol(self):
        if messagebox.askyesno("Confirmar", "¿Eliminar todo el árbol?"):
            self.tree.eliminar_arbol()
            self._escribir_salida("Árbol eliminado.")
            self._actualizar_dibujo()

    def _btn_limpiar_salida(self):
        self.txt_salida.delete("1.0", "end")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
