# s = 0
# c = 0
# for c in range(1, 501, 1):
#     if c % 2 == 1:
#         if c % 3 == 0:
#             c = c + 1
#             s = s + c

# s = 0
# c = 0
# for c in range(1, 501, 1):
#     if c % 3 == 0:  # aqui ele vai ver quem é divisel por 3 e
#         c = c + 1  # jogar dentro do bloco, mas vai fazer todos
#         s = s + c  # os números
# print(f"A soma de todos os {c} valores é: {s}")

soma = 0  # acumulador, ele acumula os elementos.
cont = 0  # contador, ele que conta a quantidade dos elementos.
for c in range(1, 501, 2):
    if c % 3 == 0:  # se c for múltiplos de 3 ou divisível por 3.
        cont = cont + 1  # um contador ele geralmente conta + 1, é mais que achou.
        #  cont += 1
        #  soma += c
        soma = soma + c  # um acumulador ele geralmente vai acumulando os valores, vai somando, vai multiplicando.
print(f"A soma de todos os {cont} valores solicitados é {soma}")
