# lanche = ("hamburguer", "suco", "pizza", "pudim", "Batata Frita")
# Tuplas são imutáveis
# print(lanche[-2:])  # fatiamento, manipulação de tuplas
# for comida in lanche:  # para cada comida em lanche:
#     print(f"Eu vou comer {comida}")
# for cont in range(0, len(lanche)):
#     print(f"Eu vou comer {lanche[cont]} na posição {cont}")
# print("Comi pra caramba!")
# for pos, comida in enumerate(lanche):
#     print(f"Eu vou comer {comida} na posição {pos}")

# print(sorted(lanche))  # mostra em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))  # quantas vezes está aparecendo o número 5 dentro de c
print(c.index(8))  # em que posição está o 8, pega a 1 ocorrência

pessoa = ("Gustavo", 39, "M", 99.88)
del(pessoa)
print(pessoa)
