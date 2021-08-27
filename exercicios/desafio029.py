# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7, 00 por cada Km acima do limite.
import time
print("-=-" * 20)
print("PROGRAMA DE VELOCIDADE...")
print("-=-" * 20)
velocidade = float(input("Qual é a velocidade atual do carro? "))
limite = 80.00
ultrapassagem = velocidade - limite
multa = 7.00 * ultrapassagem
print("PROCESSANDO...")
time.sleep(3)
if velocidade > 80.00:
    print(f"Você foi MULTADO! E terá que pagar R${multa}\n"
    f"por ter ultrapasso a velocidade de {limite}Km/h\n"
    f"e estava correndo na velocidade de {ultrapassagem}Km/h há mais.")
else:
    print(f"Você NÃO ultrapassou a velocidade limite de {limite}km/h e não será multado! ")
print("--FIM--")
