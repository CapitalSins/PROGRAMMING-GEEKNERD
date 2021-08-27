# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.
import time
print("-=-" * 20)
print("VIAJEM...")
print("-=-" * 20)

distancia = float(input("Qual a distância percorrida da viagem? "))

print("CALCULANDO...")
time.sleep(3)

if distancia <= 200.00:
    preço = distancia * 0.50
    print(f"O preço cobrado da viagem será de {preço:.2f} reais para viagens mais curtas.")
else:
    preço = distancia * 0.45
    print(f"O preço cobrado será de {preço:.2f} reais para viagens mais longas.")
print("--FIM--")
