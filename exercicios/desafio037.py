# Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.
import time

print("-=-" * 20)
print("   <<<CONVERSOR>>>   ")
print("-=-" * 20)

num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opcao = int(input("Sua opção: "))

print("\033[4;31mCONVERTENDO...\033[m")
time.sleep(3)

if opcao == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Opção inválida. Tente novamente.")

print("\033[4;31m--FIM--\033[m")
