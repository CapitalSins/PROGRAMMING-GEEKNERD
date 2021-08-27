# from math import factorial
# n = int(input("Digite um número para calcular seu Fatorial: "))
# f = factorial(n)
# print(f"O fatorial de {n} é {f}")

# n = int(input("Digite um número para calcular seu Fatorial: "))
# c = n
# f = 1
# print(f"Calculando {n}! = ", end='')
# while c > 0:
#     print(f"{c}", end="")
#     print(" x " if c > 1 else " = ", end="")
#     f = f * c
#     c = c - 1
# print(f"{f}")

n = int(input("Digite um número para calcular seu Fatorial: "))
f = 1
print(f"Calculando {n}! = ", end='')
for i in range(n, 0, -1):
    print(f"{i}", end='')
    print(" x " if i > 1 else " = ", end='')
    f = f * i
print(f"{f}")
