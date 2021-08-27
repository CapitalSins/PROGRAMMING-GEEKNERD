# tempo = int(input("Quantos anos tem seu carro? "))
# print("Carro novo" if tempo <= 3 else "Carro velho")
# if tempo <= 3:
#     print("Carro novo")
# else:
#     print("Carro velho")
# print("--FIM--")

# nome = input("Qual é seu nome? ")
# if nome == "Gustavo":
#     print("Que nome lindo você tem!")
# else:
#     print("Seu nome é tão normal!")
# print(f"Bom dia {nome}!")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print(f"A sua média foi {m:.1f}")
# if m >= 6:
#     print("Sua média foi boa! PARABÉNS!")
# else:
#     print("Sua média foi ruim! ESTUDE MAIS!")
print("PARABÉNS!" if m >= 6 else "ESTUDE MAIS!")
