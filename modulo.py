import random

# 1 - Número aleatório simples
def n_aleatorio(a, b): 
    return random.randint(a, b)

# 2 - Três números aleatórios
def tres_aleatorios(): 
    return [random.randint(1, 100) for _ in range(3)]

# 3 - Aleatório usando range
def aleatorio_range(a, b): 
    return random.choice(range(a, b + 1))

# 4 - Contagem regressiva
def contagem():
    for i in range(10, 0, -1): 
        print(i)
    print("Fogo!")

# 5 - Soma de pares
def somar_pares(n): 
    return sum(i for i in range(2, n + 1, 2))