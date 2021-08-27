# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
import time
print("-=-" * 20)
print("PROJETINHO")
print("-=-" * 20)
num = int(input("Digite um número inteiro positivo: "))
print("DESVENDANDO...")
time.sleep(3)
if num % 2 == 0:  # todo resto divido por 2 que dá 0 é par se der 1 é ímpar
    print("Ele é PAR!")
else:
    print("Ele é ÍMPAR!")
print("--FIM--")
