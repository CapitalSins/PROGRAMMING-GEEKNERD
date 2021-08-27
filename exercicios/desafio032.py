# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
import calendar
import time
print("-=-" * 20)
print("ANO...") 
print("-=-" * 20)

ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
print("ANALISANDO...")
time.sleep(3)
calendar.isleap(ano)

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")
print("--FIM--")
