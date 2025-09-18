import sys
from functools import lru_cache


sys.set_int_max_str_digits(1000000)

# ----------------------------
# Sin recursividad (iterativo)
# ----------------------------
def fibonacci_10000_digits_iterativo():
    a, b = 0, 1
    index = 1

    while len(str(b)) < 10000:
        a, b = b, a + b
        index += 1

    return index, b 

indice, numero = fibonacci_10000_digits_iterativo()
print("=== Iterativo ===")
print(f"El primer número de Fibonacci con 10,000 dígitos es F({indice}).")
print(f"Tiene {len(str(numero))} dígitos.\n")


# ----------------------------
# Con recursividad (con memoización)
# ----------------------------
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_10000_digits_recursivo():
    n = 1
    while True:
        num = fibonacci(n)
        if len(str(num)) >= 10000: 
            return n, num
        n += 1

indice, numero = fibonacci_10000_digits_recursivo()
print("=== Recursivo ===")
print(f"El primer número de Fibonacci con 10,000 dígitos es F({indice}).")
print(f"Tiene {len(str(numero))} dígitos.")
