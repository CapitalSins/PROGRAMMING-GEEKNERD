# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é 
# o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# maiorM = menorM = 0
# mulher = 0
# soma = cont = 0
# for c in range(1, 5):
#     nome = input("Qual o seu nome? ").capitalize().strip()
#     idade = int(input("Qual a sua idade? "))
#     sexo = input("Digite seu sexo [M] [F] ").upper().strip()
#     sexo = sexo[0]
#     soma = soma + idade  # vai somar as idades
#     cont = cont + 1  # é um contador, sempre vai receber + 1 até acabar
#     media = soma / cont
#     if sexo == "M":
#         if c == 1:
#             maiorM = idade
#             menorM = idade
#             nomevelho = nome
#         else:
#             if idade > maiorM:
#                 maior = idade
#                 nomevelho = nome
#             if idade < menorM:
#                 menorM = idade
#     if sexo == "M":
#         if idade < 20:
#             mulher = mulher + 1
# print(f"A média de idade do grupo é: {media}")
# print(f"O nome do homem mais velho é: {nomevelho}")
# print(f"{mulher} mulheres tem menos de 20 anos.")

somaidade = 0
totmulher20 = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1, 5):
    print(f"----- {p} PESSOA -----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 = totmulher20 + 1
media = somaidade / 4
print(f"A média de idade do grupo é de {media} anos")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")
print(f"Tem {totmulher20} mulheres com menos de 20 anos.")
