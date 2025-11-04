from typing import List, Dict, Optional


def find_postre_index(postres: List[Dict], nombre: str) -> Optional[int]:

    for i, p in enumerate(postres):
        if p["nombre"].strip().lower() == nombre.strip().lower():
            return i
    return None


def imprimir_ingredientes(postres: List[Dict], nombre: str):

    idx = find_postre_index(postres, nombre)
    if idx is None:
        print(f"\nEl postre '{nombre}' no existe.\n")
        return
    print(f"\nIngredientes de {postres[idx]['nombre']}:")
    for ing in postres[idx]["ingredientes"]:
        print(f"  - {ing}")
    print()


def insertar_ingrediente(postres: List[Dict], nombre: str, ingrediente: str):

    idx = find_postre_index(postres, nombre)
    if idx is None:
        print(f"\nEl postre '{nombre}' no existe.\n")
        return
    if ingrediente in postres[idx]["ingredientes"]:
        print(f"\nEl ingrediente '{ingrediente}' ya existe en '{nombre}'.\n")
    else:
        postres[idx]["ingredientes"].append(ingrediente)
        print(f"\n'{ingrediente}' agregado a '{nombre}'.\n")


def eliminar_ingrediente(postres: List[Dict], nombre: str, ingrediente: str):

    idx = find_postre_index(postres, nombre)
    if idx is None:
        print(f"\nEl postre '{nombre}' no existe.\n")
        return
    try:
        postres[idx]["ingredientes"].remove(ingrediente)
        print(f"\n'{ingrediente}' eliminado de '{nombre}'.\n")
    except ValueError:
        print(f"\n'{ingrediente}' no se encontró en '{nombre}'.\n")


def alta_postre(postres: List[Dict], nombre: str, ingredientes: List[str]):

    if find_postre_index(postres, nombre) is not None:
        print(f"\nEl postre '{nombre}' ya existe.\n")
        return
    postres.append({"nombre": nombre, "ingredientes": ingredientes})
    print(f"\nPostre '{nombre}' agregado con {len(ingredientes)} ingredientes.\n")


def baja_postre(postres: List[Dict], nombre: str):

    idx = find_postre_index(postres, nombre)
    if idx is None:
        print(f"\nEl postre '{nombre}' no existe.\n")
        return
    postres.pop(idx)
    print(f"\nPostre '{nombre}' eliminado.\n")


# -------------------------------
# SUBPROGRAMA (eliminar duplicados)
# -------------------------------

def eliminar_duplicados(postres: List[Dict]):
    vistos = {}
    nuevos = []
    for p in postres:
        nombre = p["nombre"].strip().lower()
        if nombre not in vistos:
            vistos[nombre] = set(ing.lower() for ing in p["ingredientes"])
            nuevos.append({
                "nombre": p["nombre"],
                "ingredientes": p["ingredientes"].copy()
            })
        else:
            for ing in p["ingredientes"]:
                if ing.lower() not in vistos[nombre]:
                    vistos[nombre].add(ing.lower())
                    for postre in nuevos:
                        if postre["nombre"].strip().lower() == nombre:
                            postre["ingredientes"].append(ing)
    postres.clear()
    postres.extend(nuevos)
    print("\nDuplicados eliminados. Ingredientes fusionados sin pérdida de datos.\n")



def menu():
    POSTRES = [
        {"nombre": "Flan", "ingredientes": ["Leche", "Azúcar", "Huevo"]},
        {"nombre": "Brownie", "ingredientes": ["Chocolate", "Harina", "Mantequilla"]},
        {"nombre": "brownie", "ingredientes": ["Azúcar", "Cacao"]},  # duplicado
    ]

    while True:
        print("""
=====================================
        MENÚ DE POSTRES
=====================================
1. Mostrar ingredientes de un postre
2. Insertar nuevo ingrediente
3. Eliminar un ingrediente
4. Dar de alta un nuevo postre
5. Dar de baja un postre
6. Eliminar duplicados (subprograma)
7. Mostrar todos los postres
0. Salir
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre del postre: ")
            imprimir_ingredientes(POSTRES, nombre)

        elif opcion == "2":
            nombre = input("Postre: ")
            ing = input("Ingrediente a agregar: ")
            insertar_ingrediente(POSTRES, nombre, ing)

        elif opcion == "3":
            nombre = input("Postre: ")
            ing = input("Ingrediente a eliminar: ")
            eliminar_ingrediente(POSTRES, nombre, ing)

        elif opcion == "4":
            nombre = input("Nuevo postre: ")
            ingredientes = input("Ingrese ingredientes separados por coma: ").split(",")
            ingredientes = [i.strip() for i in ingredientes if i.strip()]
            alta_postre(POSTRES, nombre, ingredientes)

        elif opcion == "5":
            nombre = input("Postre a eliminar: ")
            baja_postre(POSTRES, nombre)

        elif opcion == "6":
            eliminar_duplicados(POSTRES)

        elif opcion == "7":
            print("\nLista actual de postres:")
            for p in POSTRES:
                print(f" - {p['nombre']}: {p['ingredientes']}")
            print()

        elif opcion == "0":
            print("\nSaliendo del programa...\n")
            break

        else:
            print("\nOpción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    menu()
