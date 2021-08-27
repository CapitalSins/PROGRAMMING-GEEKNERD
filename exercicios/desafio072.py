cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze",
        "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        print(f"Você digitou o número {cont[num]}")
        pergunta = input("Você quer tentar novamente? ").upper()
        if pergunta == "S":
            num = int(input("Digite um número entre 0 e 20: "))
            if 0 <= num <= 20:
                break
            else:
                print("Tente novamente. ", end='')
        else:
            break
    print("Tente novamente. ", end='')
print(f"Você digitou o número {cont[num]}")
