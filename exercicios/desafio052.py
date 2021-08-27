# Faça um programa que leia um número inteiro e diga se ele é ou 
# não um número primo.

núm = int(input("Digite um número: "))
tot = 0  # pra saber o número de divisíveis
for c in range(1, núm + 1):
    if núm % c == 0:  # vai dividir valor de núm por 1 até núm e se o resto for igual a 0 essa condição vai se satisfazer
        print("\033[33m", end='')
        tot += 1
    else:  # se não for resto 0 vem pra cá
        print("\033[31m", end='')
    print(f"{c}", end=' ')
print(f"\n\033[mO número {núm} foi divisível {tot} vezes")
if tot == 2:
    print("E por isso ele É PRIMO!")  # O número só é primo se for divisível por 1 e ele mesmo
else:
    print("E por isso ele NÃO É PRIMO!")
