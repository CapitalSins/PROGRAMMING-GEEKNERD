# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

# a1 = int(input("Qual vai ser o 1° termo? "))
# n = 10
# r = int(input("Qual vai ser a razão? "))
# an = a1 + (n - 1) * r
# n = 0
# for c in range(a1, an + 1, r):
#     n = n + 1
#     print(f"O {n} termo é: {c}")

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f"{c} ", end='-> ')
print("ACABOU")
