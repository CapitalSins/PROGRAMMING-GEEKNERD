# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar 
# ao serviço militar, se é a hora exata de se alistar 
# ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta 
# ou que passou do prazo.
from time import sleep
from datetime import date
print("-=-" * 20)
print("   <<<ALISTAMENTO MILITAR>>>   ")
print("-=-" * 20)

nascimento = int(input("Digite o ano que anasceu: "))
ano_atual = date.today().year
idade = ano_atual - nascimento

print("\033[4;34mANALISANDO...\033[m")
sleep(3)

print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.")
if idade < 18:
    saldo = 18 - idade
    print(f"Ainda vai se alistar ao serviço militar, falta {saldo} ano(s).")
    ano = ano_atual + saldo
    print(f"Seu alistamento será em {ano}.")
elif idade == 18:
    print("Está na hora de se alistar ao serviço militar.")
elif idade > 18:
    saldo = idade - 18
    print(f"Já passou do tempo de se alistar, tem {saldo} ano(s) que passou.")
    ano = ano_atual - saldo
    print(f"Seu alistamento foi em {ano}.")
else:
    print("Digite um ano correto!")
print("\033[4;31m--FIM--\033[m")
