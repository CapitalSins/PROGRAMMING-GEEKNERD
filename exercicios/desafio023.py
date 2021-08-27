# num = input("Digite um número entre 0 e 9999: ")
# print(f"unidade: {num[-1]}")
# print(f"dezena: {num[-2]}")
# print(f"centena: {num[-3]}")
# print(f"milhar: {num[-4]}")
num = int(input("Informe um número: "))
unidade = num % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f"Analisando o número {num}")
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
