# Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

import time
print("-=-" * 20)
print("   <<<MAIOR OU MENOR>>>   ")
print("-=-" * 20)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("\033[4;31mANALISANDO...\033[m")
time.sleep(3)

if num1 > num2:
    print("O primeiro valor é maior.")
elif num2 > num1:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")

print("\033[7;32m--FIM--\033[m")
