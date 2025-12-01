import os
import hashlib
import shutil

def hash_archivo(nombre_archivo):
    h = hashlib.sha256()
    h.update(nombre_archivo.encode())
    return h.hexdigest()

def ordenar_por_hash(ruta):
    if not os.path.isdir(ruta):
        print("La ruta no existe.")
        return

    archivos = os.listdir(ruta)
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_archivo):
            h = hash_archivo(archivo)

            
            subcarpeta = h[:2]
            ruta_subcarpeta = os.path.join(ruta, subcarpeta)

            
            if not os.path.exists(ruta_subcarpeta):
                os.makedirs(ruta_subcarpeta)

            
            shutil.move(ruta_archivo, os.path.join(ruta_subcarpeta, archivo))
            print(f"Movido: {archivo} → {subcarpeta}/")

    print("\nArchivos ordenados correctamente por hash.")



ruta = input("Ingresa la ruta de la carpeta: ")
ordenar_por_hash(ruta)
