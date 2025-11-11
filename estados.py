# ============================================================
# Programa: Red Interactiva de Estados de México (versión Tkinter)
# ============================================================


import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import folium
import os
import webbrowser


class RedMexico:
    def __init__(self, root):
        self.root = root
        self.root.title("Red de Estados de México")
        self.root.geometry("750x600")
        self.root.config(bg="#f2f2f2")

        # === Grafo ===
        self.grafo = nx.Graph()

        # === Coordenadas de estados ===
        self.ubicaciones = {
            "Baja California": (32.5, -115.0), "Sonora": (29.0, -110.0),
            "Chihuahua": (28.6, -106.0), "Coahuila": (27.0, -101.0),
            "Nuevo León": (25.7, -100.3), "Tamaulipas": (24.2, -98.7),
            "Sinaloa": (25.0, -107.5), "Durango": (24.0, -104.7),
            "Zacatecas": (23.6, -102.5), "San Luis Potosí": (22.2, -100.9),
            "Nayarit": (21.8, -104.9), "Jalisco": (20.7, -103.3),
            "Guanajuato": (20.9, -101.2), "Querétaro": (20.6, -100.4),
            "Hidalgo": (20.5, -98.9), "Veracruz": (19.2, -96.1),
            "Puebla": (19.0, -98.2), "Michoacán": (19.7, -101.2),
            "Guerrero": (17.5, -99.5), "Oaxaca": (17.0, -96.7),
            "Chiapas": (16.7, -93.1), "Tabasco": (17.8, -92.6),
            "Campeche": (19.8, -90.5), "Yucatán": (20.9, -89.6),
            "Quintana Roo": (19.6, -88.0), "CDMX": (19.4, -99.1),
            "Estado de México": (19.3, -99.6), "Morelos": (18.8, -99.2),
            "Tlaxcala": (19.3, -98.2)
        }

        # === INTERFAZ ===
        self.crear_interfaz()

    # ---------------------------------------------------------
    # Sección de interfaz
    # ---------------------------------------------------------
    def crear_interfaz(self):
        marco = tk.Frame(self.root, bg="#ffffff", bd=2, relief="groove")
        marco.pack(padx=10, pady=10, fill="both", expand=True)

        ttk.Label(marco, text="Red de Estados de México", font=("Arial", 16, "bold")).pack(pady=10)

        # --- Sección de agregar estado ---
        frame_estado = tk.LabelFrame(marco, text="Agregar Estado", bg="#ffffff")
        frame_estado.pack(padx=10, pady=10, fill="x")

        self.estado_combo = ttk.Combobox(frame_estado, values=list(self.ubicaciones.keys()), width=35)
        self.estado_combo.pack(side="left", padx=10, pady=5)
        ttk.Button(frame_estado, text="Añadir", command=self.añadir_estado).pack(side="left", padx=10)

        # --- Sección de conexiones ---
        frame_conexion = tk.LabelFrame(marco, text="Crear Conexión", bg="#ffffff")
        frame_conexion.pack(padx=10, pady=10, fill="x")

        self.origen_combo = ttk.Combobox(frame_conexion, values=list(self.ubicaciones.keys()), width=20)
        self.origen_combo.pack(side="left", padx=5, pady=5)
        ttk.Label(frame_conexion, text="↔").pack(side="left")
        self.destino_combo = ttk.Combobox(frame_conexion, values=list(self.ubicaciones.keys()), width=20)
        self.destino_combo.pack(side="left", padx=5, pady=5)
        ttk.Label(frame_conexion, text="Costo:").pack(side="left", padx=5)
        self.costo_entry = ttk.Entry(frame_conexion, width=8)
        self.costo_entry.pack(side="left", padx=5)
        ttk.Button(frame_conexion, text="Conectar", command=self.enlazar_estados).pack(side="left", padx=5)

        # --- Sección de acciones ---
        frame_acciones = tk.Frame(marco, bg="#ffffff")
        frame_acciones.pack(padx=10, pady=5)

        ttk.Button(frame_acciones, text="Mostrar Red", command=self.mostrar_red).grid(row=0, column=0, padx=8, pady=5)
        ttk.Button(frame_acciones, text="Recorrido sin repetir", command=self.recorrido_unico).grid(row=0, column=1, padx=8, pady=5)
        ttk.Button(frame_acciones, text="Recorrido con repetición", command=self.recorrido_con_repeticion).grid(row=0, column=2, padx=8, pady=5)
        ttk.Button(frame_acciones, text="Generar Mapa", command=self.generar_mapa).grid(row=0, column=3, padx=8, pady=5)

        # --- Sección de salida ---
        frame_salida = tk.LabelFrame(marco, text="Salida", bg="#ffffff")
        frame_salida.pack(padx=10, pady=10, fill="both", expand=True)

        self.texto_salida = tk.Text(frame_salida, wrap="word", height=15)
        self.texto_salida.pack(padx=10, pady=10, fill="both", expand=True)

    # ---------------------------------------------------------
    # Lógica del programa
    # ---------------------------------------------------------
    def añadir_estado(self):
        estado = self.estado_combo.get()
        if not estado:
            messagebox.showwarning("Atención", "Selecciona un estado válido.")
            return
        if estado in self.grafo.nodes:
            messagebox.showinfo("Duplicado", f"El estado {estado} ya fue agregado.")
            return
        self.grafo.add_node(estado)
        self.mostrar_mensaje(f"✅ Estado agregado: {estado}")

    def enlazar_estados(self):
        origen = self.origen_combo.get()
        destino = self.destino_combo.get()
        costo = self.costo_entry.get()

        if not (origen and destino and costo):
            messagebox.showwarning("Atención", "Completa todos los campos para crear una conexión.")
            return
        try:
            costo = float(costo)
        except ValueError:
            messagebox.showerror("Error", "El costo debe ser un número.")
            return

        if origen not in self.grafo.nodes or destino not in self.grafo.nodes:
            messagebox.showerror("Error", "Ambos estados deben estar añadidos antes de conectarlos.")
            return

        self.grafo.add_edge(origen, destino, weight=costo)
        self.mostrar_mensaje(f"🔗 Conexión creada: {origen} ↔ {destino} | Costo: {costo}")

    def mostrar_red(self):
        if not self.grafo.nodes:
            self.mostrar_mensaje("⚠️ No hay estados registrados.")
            return

        texto = "\n📍 Estados actuales:\n"
        for estado in self.grafo.nodes:
            texto += f" - {estado}\n"

        texto += "\n🔗 Conexiones:\n"
        for a, b, info in self.grafo.edges(data=True):
            texto += f" - {a} ↔ {b} | Costo: {info['weight']}\n"

        self.mostrar_mensaje(texto)

    def recorrido_unico(self):
        if not self.grafo.nodes:
            self.mostrar_mensaje("⚠️ No hay estados registrados.")
            return
        recorrido = list(nx.dfs_preorder_nodes(self.grafo))
        total = 0
        for i in range(len(recorrido) - 1):
            try:
                total += self.grafo[recorrido[i]][recorrido[i + 1]]['weight']
            except KeyError:
                
                continue
        texto = f"\n🚗 Recorrido sin repetir:\n{' → '.join(recorrido)}\nCosto total: {total}"
        self.mostrar_mensaje(texto)

    def recorrido_con_repeticion(self):
        """
        Recorrido tipo BFS que puede repetir nodos.
        Corregido para:
          - Elegir un nodo inicial si hay nodos pero no se indicó fuente.
          - Manejar grafos sin aristas.
          - Evitar IndexError cuando no hay aristas.
        """
        if not self.grafo.nodes:
            self.mostrar_mensaje("⚠️ No hay estados registrados.")
            return

        
        inicio = list(self.grafo.nodes)[0]

        
        try:
            aristas = list(nx.bfs_edges(self.grafo, source=inicio))
        except Exception as e:
            
            self.mostrar_mensaje(f"⚠️ Error al realizar BFS: {e}")
            return

        
        if not aristas:
            camino = [inicio]
            total = 0
            texto = f"\n🔁 Recorrido con repetición:\n{' → '.join(camino)}\nCosto total: {total}\n(Nota: no hay conexiones en el grafo)"
            self.mostrar_mensaje(texto)
            return

        
        camino = [aristas[0][0]] + [v for (_, v) in aristas] + [aristas[0][0]]

        
        total = 0
        for i in range(len(camino) - 1):
            a = camino[i]
            b = camino[i + 1]
            if self.grafo.has_edge(a, b):
                total += self.grafo[a][b].get('weight', 0)
            else:
                
                continue

        texto = f"\n🔁 Recorrido con repetición:\n{' → '.join(camino)}\nCosto total: {total}"
        self.mostrar_mensaje(texto)

    def generar_mapa(self):
        if not self.grafo.nodes:
            messagebox.showwarning("Atención", "No hay estados registrados.")
            return

        mapa = folium.Map(location=[23.6345, -102.5528], zoom_start=5)
        for estado in self.grafo.nodes:
            lat, lon = self.ubicaciones[estado]
            folium.Marker(
                location=[lat, lon],
                popup=estado,
                icon=folium.Icon(color="blue")
            ).add_to(mapa)

        for a, b, info in self.grafo.edges(data=True):
            c1 = self.ubicaciones[a]
            c2 = self.ubicaciones[b]
            folium.PolyLine(
                [c1, c2],
                color="green",
                weight=3,
                tooltip=f"{a} ↔ {b} (Costo: {info['weight']})"
            ).add_to(mapa)

        archivo = "red_mexico.html"
        mapa.save(archivo)
        webbrowser.open_new_tab('file://' + os.path.abspath(archivo))
        self.mostrar_mensaje(f"🗺️ Mapa generado: {archivo}")

    # ---------------------------------------------------------
    # Utilidad
    # ---------------------------------------------------------
    def mostrar_mensaje(self, texto):
        self.texto_salida.insert(tk.END, texto + "\n\n")
        self.texto_salida.see(tk.END)


# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = RedMexico(root)
    root.mainloop()
