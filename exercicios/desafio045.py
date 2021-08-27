# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
# print(f"O computador escolheu {itens[computador]}")
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("-=-" * 11)
print(f"Computador jogou {itens[computador]}")
print(f"O jogador jogou {itens[jogador]}")
print("-=-" * 11)
if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE!")
    elif jogador == 2:
        print("COMPUTADOR VENCE!")
    else:
        print("JOGADA INVÁLIDA!")

elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE!")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE!")
    elif jogador == 1:
        print("COMPUTADOR VENCE!")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA!")




# if computador == jogador :
#     print("EMPATE")
# elif computador == 2 and jogador == 1 or computador == 1 and jogador == 0 or computador == 0 and jogador == 2:
#     print("Computador Venceu!")
# elif computador == 0 and jogador == 1 or computador == 1 and jogador == 2 or computador == 2 and jogador == 1:
#     print("Jogador venceu!")
# else:
#     print("Digite um valor entre 0 e 2!")
print("--FIM--")
