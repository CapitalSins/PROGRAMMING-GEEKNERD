# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.
import time
print("-=-" * 20)
print("MAIOR, MENOR...")
print("-=-" * 20)

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

print("<<<PROCESSANDO>>>")
time.sleep(3)

# if num1 > num2 and num2 > num3:
#     print(f"Esse {num1} é o maior número.")
# else:
#     if num2 > num1 and num2 > num3:
#         print(f"Esse {num2} é o maior número.")
#     else:
#         print(f"Esse {num3} é o maior número.")

# if num1 < num2 and num1 < num3:
#     print(f"Esse {num1} é o menor número.")
# else:
#     if num2 < num3 and num2 < num1:
#         print(f"Esse {num2} é o menor número.")
#     else:
#         print(f"Esse {num3} é o menor número.")
# print("--FIM--")

# if num1 > num2 and num1 > num3:
#     print(f"Esse {num1} é o maior número.")
# if num2 > num1 or num3 > num1 :
#     if num2 > num1 and num2 > num3:
#         print(f"Esse {num2} é o maior número.")
#     else:
#         print(f"Esse {num3} é o maior número.")

# if num1 < num2 and num1 < num3:
#     print(f"Esse {num1} é o menor número.")
# if num2 < num1 or num3 < num1:
#     if num2 < num3 and num2 < num1:
#         print(f"Esse {num2} é o menor número.")
#     else:
#         print(f"Esse {num3} é o menor número.")
# print("--FIM--")

#  Verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f"O maior valor digitado foi {maior}")
#  Verificando quem é o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f"O menor valor digitado foi {menor}")
print("--FIM--")
