# memoria estatica
def memoria_estatica():
    calificaciones = [0] * 5  

    for i in range(5):
        calificaciones[i] = int(input(f"Captura la calificación {i+1}: "))

    print("Las calificaciones son:", calificaciones)

memoria_estatica()

#memoria dinámica
def memoria_dinamica():
    frutas = [] 

    frutas.append("Mango")
    frutas.append("Manzana")
    frutas.append("Banana")
    frutas.append("Uvas")
    print("Lista inicial:", frutas)

    frutas.pop(0)
    frutas.pop(1)

    frutas.append("Sandía")
    print("Lista final:", frutas)

memoria_dinamica()
