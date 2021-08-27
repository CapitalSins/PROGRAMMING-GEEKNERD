from random import randint  # randomizar números inteiros
numeros = (randint(0, 100), randint(0, 100), randint(
    0, 100), randint(0, 100), randint(0, 100))
print("Os números são: ")
for n in numeros:  # para cada numero(n) em numeros
    print(f"{n} ", end='')
print(f"\nO maior número é {max(numeros)}")
print(f"O menoor número é {min(numeros)}")
