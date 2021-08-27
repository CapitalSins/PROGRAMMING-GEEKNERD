# Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo.
from time import sleep
print("-=-" * 20)
print("Analisador de Triângulos ")
print("-=-" * 20)
# a medida de qualquer um dos lados seja menor que a soma 
# das medidas dos outros dois e maior que o valor absoluto da 
# diferença entre essas medidas. | b - c | < a < b + c ou a < b + c
# REF: https://brasilescola.uol.com.br/matematica/triangulo.htm

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

print("<<<ANALISANDO>>>")
sleep(3)

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR triângulo!")
else:
    print("Os segmentos acima não PODEM FORMAR triângulo!")
print("--FIM--")

# if b - c < a < b + c and a - c < b < a + c and a - b <  c < a + b:
#     print("Os segmesntos acima PODEM FORMAR triângulo!")
# else:
#     print("Os segmentos acima não PODEM FORMAR triângulo!")
# print("--FIM--")
