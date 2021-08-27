# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30 % do salário
# ou então o empréstimo será negado.
print("-=-" * 20)
print("EMPRESTIMO...")
print("-=-" * 20)

import time

casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
tempo = int(input("Quantos anos de financiamneto? "))
prestacao = casa / (12 * tempo)
minimo = salario * 0.3

print("   <<<ANALISANDO>>>   ")
time.sleep(3)
print(f"Para pagar uma casa de R${casa:.2f} em {tempo} anos a prestação será de R${prestacao:.2f}.")

if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO.")
else:
    print("EMPRÉSTIMO NEGADO!")
print("--FIM--")
