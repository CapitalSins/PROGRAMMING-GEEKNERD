numero = int(input("Digite um número entre 0 e 9999: "))
print(f"Analisando o número {numero}")

unidade = numero % 10
dezena = (numero - unidade) / 10 % 10
centena = (numero - dezena) / 10 % 10
milhar = (numero - centena) / 10 % 10
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena:.0f}")
print(f"Centena: {centena:.0f}")
print(f"Milhar: {milhar:.0f}")
