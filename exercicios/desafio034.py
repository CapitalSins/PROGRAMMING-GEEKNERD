# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10 %. 
# Para os inferiores ou iguais, o aumento é de 15 % .

import time
print("-=-" * 20)
print("<<<SALÁRIO>>>")
print("-=-" * 20)

salario = float(input("Informe o seu salário R$"))
print("<<<CALCULANDO AUMENTOS>>>")
time.sleep(3)

if salario >= 1250.00:
    salario = (salario * 0.10) + salario
else:
    salario = (salario * 0.15) + salario
print(f"O seu salário vai para R${salario:.2f} com o aumento.")
print("--FIM--")
