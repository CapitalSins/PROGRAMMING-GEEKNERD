# Crie um programa que leia uma frase qualquer 
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input("Digite uma frase: ").upper().strip()
palavras = frase.split()  # vai dividir essas palavras, separar num vetor, numa lista
junto = ''.join(palavras)
# inverso = ''
inverso = junto[::-1]  # vai começar do início até o fim, só que de trás pra frente, ou do último ao primeiro
# for letra in range(len(junto) - 1, - 1, - 1):  # começá do total - 1 e vai até o 0 e vai voltar -1
#     inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palídromo!")
else:
    print("A frase digitada não é um palíndromo!")
print(junto, inverso)
