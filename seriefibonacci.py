import sys
from functools import lru_cache

sys.set_int_max_str_digits(1000000)

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci_hasta(n_max):
    for i in range(n_max + 1):
        print(f"F({i}) = {fibonacci(i)}")

def fibonacci_10000_digits():
    n = 1
    while True:
        num = fibonacci(n)
        if len(str(num)) >= 10000:
            return n, num
        n += 1


print("Mostrando la secuencia hasta F(100)...\n")
mostrar_fibonacci_hasta(100)

indice, numero = fibonacci_10000_digits()
print("\n---------------------------------------------")
print(f"El primer número de Fibonacci con 10,000 dígitos es F({indice}).")
print(f"Tiene {len(str(numero))} dígitos.")
