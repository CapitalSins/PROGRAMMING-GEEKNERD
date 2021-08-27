# print("Oi")
# for c in range(0, 3):  # o último ele ignora
#     c = "Oi"
#     print(c)
# for c in range(6, 0, -1):  # vai contar de 6 até 1, no final você vai dizer qual é a iteração, o que vai acontecer no final do laço.
#     print(c)
# for c in range(0, 7, 2):
#     print(c)
# n = int(input("Digite um número: "))
# for c in range(0, n + 1):
#     print(c)
# i = int(input("Início: "))
# f = int(input("Fim: "))
# p = int(input("Passo: "))
# for c in range(i, f+1, p):
#     print(c)

s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s = s + n
print(f"O somatório de todos os valores foi {s} e foram {c+1} números")
