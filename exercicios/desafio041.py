# A Confederação Nacional de Natação precisa de um programa 
# que leia o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from time import sleep
from datetime import date

print("-=-" * 20)
print("   <<<CATEGORIA>>>   ")
print("-=-" * 20)

ano_atual = date.today().year
nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - nascimento

print("\033[1;35mANALISANDO...\033[m")
sleep(3)

if idade <= 9:
    print(f"Você tem {idade} anos e está na categoria MIRIM.")
elif idade <= 14:
    print(f"Você tem {idade} anos e está na categoria INFANTIL.")
elif idade <= 19:
    print(f"Você tem {idade} anos e está na categoria JÚNIOR.")
elif idade <= 25:
    print(f"Você tem {idade} anos e está na categoria SÊNIOR.")
elif idade >= 25:
    print(f"Você tem {idade} anos e está na categoria MASTER.")
else:
    print(f"Por favor inserir um ano de nascimento correto.")
print("\033[7;34;43m--FIM--\033[m")
