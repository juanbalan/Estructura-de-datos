import random
import time

# ----------------- GENERACIÓN DE DATOS -----------------

# Generar matriz alumno → materias
def generar_matriz_alumno_materia(n_alumnos, n_materias):
    return [[random.randint(0, 100) for _ in range(n_materias)] for _ in range(n_alumnos)]

# Generar matriz materia → alumnos
def generar_matriz_materia_alumno(n_materias, n_alumnos):
    return [[random.randint(0, 100) for _ in range(n_alumnos)] for _ in range(n_materias)]


# ----------------- IMPRESIÓN ADAPTATIVA -----------------

def mostrar_matriz(matriz, modo="Alumno/Materia"):
    num_filas = len(matriz)
    num_columnas = len(matriz[0]) if num_filas > 0 else 0

    if modo == "Alumno/Materia":
        encabezados = [modo] + [f"M{j}" for j in range(num_columnas)]
        tabla = [[f"Alumno {i}"] + [str(matriz[i][j]) for j in range(num_columnas)] for i in range(num_filas)]
    else:  # Materia/Alumno
        encabezados = [modo] + [f"A{j}" for j in range(num_columnas)]
        tabla = [[f"Materia {i}"] + [str(matriz[i][j]) for j in range(num_columnas)] for i in range(num_filas)]

    # Calcular anchos máximos
    columnas = list(zip(*([encabezados] + tabla)))
    anchos = [max(len(str(item)) for item in col) + 2 for col in columnas]

    # Encabezado
    encabezado_str = "".join(encabezados[i].ljust(anchos[i]) for i in range(len(encabezados)))
    print(encabezado_str)
    print("-" * len(encabezado_str))

    # Filas
    for fila in tabla:
        fila_str = "".join(fila[i].ljust(anchos[i]) for i in range(len(fila)))
        print(fila_str)


# ----------------- BÚSQUEDA CON TIEMPO -----------------

def buscar_en_matriz(matriz, forma, alumno, materia, repeticiones=100000):
    """
    Busca un valor en la matriz repitiendo muchas veces para medir el tiempo.
    """
    inicio = time.time()
    for _ in range(repeticiones):
        if forma == "alumno-materia":
            valor = matriz[alumno][materia]
        else:  # materia-alumno
            valor = matriz[materia][alumno]
    fin = time.time()
    return valor, fin - inicio


# ----------------- PROGRAMA PRINCIPAL -----------------

num_alumnos = 10000   # cambia a 1000, 10000, etc.
num_materias = 1000    # cambia a 100, 500, etc.

# Generar ambas matrices
matriz1 = generar_matriz_alumno_materia(num_alumnos, num_materias)
matriz2 = generar_matriz_materia_alumno(num_materias, num_alumnos)

# Mostrar ejemplos de las tablas
print("\n=== Matriz Alumno → Materia ===")
mostrar_matriz(matriz1, "Alumno/Materia")

print("\n=== Matriz Materia → Alumno ===")
mostrar_matriz(matriz2, "Materia/Alumno")

# Búsqueda
alumno_buscar = 321
materia_buscar = 5

valor1, tiempo1 = buscar_en_matriz(matriz1, "alumno-materia", alumno_buscar, materia_buscar)
valor2, tiempo2 = buscar_en_matriz(matriz2, "materia-alumno", alumno_buscar, materia_buscar)

print(f"\n🔎 Búsqueda Alumno {alumno_buscar}, Materia {materia_buscar}:")
print(f"  Forma Alumno-Materia → Valor: {valor1}, Tiempo: {tiempo1:.6f} segundos (100,000 repeticiones)")
print(f"  Forma Materia-Alumno → Valor: {valor2}, Tiempo: {tiempo2:.6f} segundos (100,000 repeticiones)")
