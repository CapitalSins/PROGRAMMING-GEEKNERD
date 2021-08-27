# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade 
# e quantas já são maiores.

# from datetime import date
# qme = qma  = 0
# ano_atual = date.today().year
# for i in range(0, 7):
#     nascimento = int(input("Qual o seu ano de nascimento? "))
#     idade = ano_atual - nascimento
#     if idade >= 21:
#         qma = qma + 1
#     if idade < 21:
#         qme = qme + 1
# print(f"A quantidade de pessoas maior de idade são {qma}.")
# print(f"A quantidade de pessoas menor de idade são {qme}.")

from datetime import date
totmaior = totmenor = 0
ano_atual = date.today().year
for pess in range(1, 8):
    nascimento = int(input(f"Em que ano a {pess} pessoa nasceu? "))
    idade = ano_atual - nascimento
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print(f"A quantidade de pessoas maior de idade são {totmaior}.")
print(f"A quantidade de pessoas menor de idade são {totmenor}.")
