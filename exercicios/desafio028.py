from random import randint  # da tabela random, só importar o método chamado randint.
# import random --- importar a biblioteca random. Aqui teria que chamar random.randit
from time import sleep  # da tabela time, só importar o método chamado sleep.
# import time --- importar a biblioteca time. Aqui teria que chamar time.sleep.
computador = randint(0, 5)  # Faz o computador "PENSAR"
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente advinhar...")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))  # Jogador tenta advinhar
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"GANHEI! Eu pensei no número {computador} e não no {jogador}!")
