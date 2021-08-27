frase = input("Digite uma letra ou palavra: ").upper().strip()
print(f"Aparece {frase.count('A')} vezes a letra A.")
print(f"Aparece na posição {frase.find('A') + 1} a primeira vez.")  # coloca + 1 pra ficar melhor de contar
print(f"Aparece na posição {frase.rfind('A') + 1} a última vez.")  # coloca + 1 pra ficar melhor de contar
