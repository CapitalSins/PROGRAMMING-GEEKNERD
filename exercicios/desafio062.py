# primeiro = int(input("Digite o primeiro termo: "))
# razão = int(input("Digite a razão: "))
# quantidade_termos = 0
# cont = 1
# mais = 10
# while mais != 0:
#     quantidade_termos = quantidade_termos + mais
#     while cont <= quantidade_termos:
#         print(f"{primeiro} -> ", end='')
#         primeiro = primeiro + razão
#         cont = cont + 1
#     print("PAUSA")
#     mais = int(input("Quantos termos você quer mostrar a mais? "))
# print(f"Progressão finalizada com {quantidade_termos} termos mostrados.")

primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{primeiro} -> ", end='')
        primeiro = primeiro + razão
        cont = cont + 1
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Acabou")
