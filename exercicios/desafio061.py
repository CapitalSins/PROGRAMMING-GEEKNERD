# primeiro = int(input("Digite o primeiro termo: "))
# razão = int(input("Digite a razão: "))
# décimo = primeiro + (10 - 1) * razão
# while primeiro < décimo:
#     print(f"{primeiro}", end=' -> ')
#     primeiro = primeiro + razão
# print("Acabou")

primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))
cont = 1
while cont <= 10:
    print(f"{primeiro} -> ", end='')
    primeiro = primeiro + razão
    cont = cont + 1
print("FIM")
