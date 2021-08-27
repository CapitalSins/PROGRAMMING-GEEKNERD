# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
from time import sleep

print("-=-" * 20)
print("   <<<CALCULO MÉDIA>>>   ")
print("-=-" * 20)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print("\033[1;35mCALCULANDO...\033[m")
sleep(3)

print(f"Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}")
if media < 5.0:
    print("Você está REPROVADO!")
elif 7 > media >= 5.0:
    print("Você está de RECUPERAÇÃO!")
elif media >= 7.0:
    print("Você está APROVADO!")
else:
    print("Insira notas válidas!")
print("\033[1;34m--FIM--\033[m")
