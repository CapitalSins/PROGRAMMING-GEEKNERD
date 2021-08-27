# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

# maiorpeso = 0  # se coloca esse valor pq o que for maior que isso vai ser tornar o maior
# menorpeso = 9999999  # se coloca esse valor pq o que for menor que isso vai ser tornar o menor
# for i in range(0, 5):
#     peso = float(input("Qual o seu peso? "))

maior = 0
menor = 0    
for pess in range(1, 6):
    peso = float(input(f"Peso da {pess} pessoa: "))
    if pess == 1:  # essa condição é verdadeira
        maior = peso  # o peso da 1 pessoa vira maior
        menor = peso  # o peso da 1 pessoa também vira menor
    else:  # chegando na 2 pessoa vem pra cá pq pess não mas 1 e sim 2 pra frente
        if peso > maior:  # se o peso que acabeo de ler, for maior que o meu maior peso
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi de {maior}Kg.")
print(f"O menor peso lido foi de {menor}Kg.")
