# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar 
# até acertar, mostrando no final 
# quantos palpites foram necessários para vencer.
from random import randint
tentativas = 1
computador = randint(0, 10)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10. Tente advinhar...")
print("-=-" * 20)
jogador = int(input("Digite um número: "))
while jogador != computador:
    tentativas = tentativas + 1
    print("Tente Novamente!")
    jogador = int(input(f"Tentativa N°{tentativas}, digite um número: "))
print(f"Foi necessário {tentativas} tentativas, para acertar!")
print("--Fim--")
