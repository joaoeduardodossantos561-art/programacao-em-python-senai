import random

# 1, 2 e 3: Funções de números aleatórios
def n_aleatorio(a, b): return random.randint(a, b)

def tres_aleatorios(): return [random.randint(1, 100) for _ in range(3)]

def aleatorio_range(a, b): return random.choice(range(a, b + 1))

# 4: Contagem regressiva
def contagem():
    for i in range(10, 0, -1): print(i)
    print("Fogo!")

# 5: Soma de pares
def somar_pares(n): return sum(i for i in range(2, n + 1, 2))

# --- Execução dos testes ---
print(f"1 - Aleatório (5-10): {n_aleatorio(5, 10)}")
print(f"2 - Três aleatórios: {tres_aleatorios()}")
print(f"3 - Aleatório Range (10-30): {aleatorio_range(10, 30)}")
print("4 - Contagem:")
contagem()

num = int(input("\n5 - Digite um número positivo para somar os pares: "))
print(f"Soma dos pares: {somar_pares(num)}")