# Refaça o DESAFIO 35 dos triângulos, 
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

r1 = int(input("Primeiro segmento: "))
r2 = int(input("Segundo segmento: "))
r3 = int(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Podem formar um triângulo!", end=" ")
    if r1 == r2 and r2 == r3:  # if r1 == r2 == r3: a igualdade é inclusiva
        print("Esse triângulo é EQUILÁTERO!")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Esse triângulo é ISÓSCELES!")
    elif r1 != r2 and r1 != r3 and r2 != r3:  # elif r1 != r2 != r3 != r1:
        print("Esse triângulo é ESCALENO!")
else:
    print("Não podem formar um triângulo!")
print("--FIM--")
