class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

def infija_a_postfija(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    pila = Pila()
    salida = []
    for token in expresion.split():
        if token.isdigit():
            salida.append(token)
        elif token in precedencia:
            while (not pila.esta_vacia() and pila.ver_tope() in precedencia
                   and precedencia[pila.ver_tope()] >= precedencia[token]):
                salida.append(pila.desapilar())
            pila.apilar(token)
        elif token == '(':
            pila.apilar(token)
        elif token == ')':
            while pila.ver_tope() != '(':
                salida.append(pila.desapilar())
            pila.desapilar()
    while not pila.esta_vacia():
        salida.append(pila.desapilar())
    return " ".join(salida)


def infija_a_prefija(expresion):

    tokens = expresion.split()[::-1]
    for i in range(len(tokens)):
        if tokens[i] == '(':
            tokens[i] = ')'
        elif tokens[i] == ')':
            tokens[i] = '('
    expresion_invertida = " ".join(tokens)
    postfija = infija_a_postfija(expresion_invertida)
    prefija = postfija.split()[::-1]
    return " ".join(prefija)

def evaluar_postfija(expresion):
    pila = Pila()
    for token in expresion.split():
        if token.isdigit():
            pila.apilar(int(token))
        else:
            b = pila.desapilar()
            a = pila.desapilar()
            if token == '+': pila.apilar(a + b)
            elif token == '-': pila.apilar(a - b)
            elif token == '*': pila.apilar(a * b)
            elif token == '/': pila.apilar(a / b)
    return pila.desapilar()


def evaluar_prefija(expresion):
    pila = Pila()
    tokens = expresion.split()[::-1]
    for token in tokens:
        if token.isdigit():
            pila.apilar(int(token))
        else:
            a = pila.desapilar()
            b = pila.desapilar()
            if token == '+': pila.apilar(a + b)
            elif token == '-': pila.apilar(a - b)
            elif token == '*': pila.apilar(a * b)
            elif token == '/': pila.apilar(a / b)
    return pila.desapilar()


def menu():
    print("=== Conversor de Expresiones con Pilas ===")
    expresion_infija = input("Ingresa una expresión en notación INFija (ej: ( 3 + 4 ) * 2 ): ")

    while True:
        print("\nOpciones:")
        print("1. Convertir a Posfija")
        print("2. Convertir a Prefija")
        print("3. Evaluar en Posfija")
        print("4. Evaluar en Prefija")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            posfija = infija_a_postfija(expresion_infija)
            print("Expresión en Posfija:", posfija)

        elif opcion == "2":
            prefija = infija_a_prefija(expresion_infija)
            print("Expresión en Prefija:", prefija)

        elif opcion == "3":
            posfija = infija_a_postfija(expresion_infija)
            print("Expresión Posfija:", posfija)
            print("Resultado:", evaluar_postfija(posfija))

        elif opcion == "4":
            prefija = infija_a_prefija(expresion_infija)
            print("Expresión Prefija:", prefija)
            print("Resultado:", evaluar_prefija(prefija))

        elif opcion == "5":
            print("¡Programa terminado!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


menu()
