# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10 % de desconto
# – à vista no cartão: 5 % de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20 % de juros
from time import sleep

print("-=-" * 20)
print("   <<<PROGRAMA DE COMPRAS>>>   ")
print("-=-" * 20)

valor = float(input("Digite o valor do produto: R$"))
print("""\033[1;33mDigite a forma de pagamento:
[ 1 ] para pagar à vista ou cheque com 10% de desconto:
[ 2 ] para pagar à vista no cartão com 5% de desconto:
[ 3 ] para pagar em até 2x no cartão pago formalmente:
[ 4 ] para pagar 3x ou mais no cartão 20% de juros:
\033[m""")
opcao = int(input("Digite a sua opção: "))
print("\033[1;31mCARREGANDO...\033[m")
sleep(3)


if opcao == 1:
    novo_valor = valor - valor * 0.1
    print(f"\033[4;34mO valor que era de R${valor:.2f} a ser pago, será de R${novo_valor:.2f}.\033[m")
elif opcao == 2:
    novo_valor = valor - valor * 0.05
    print(f"\033[4;34mO valor que era de R${valor:.2f} a ser pago, será de R${novo_valor:.2f}.\033[m")
elif opcao == 3:
    novo_valor = valor / 2  # novo_valor = valor - parcela = novo_valor / 2
    print(f"\033[4;34mSua compra será parcelada em {2}x de R${novo_valor:.2f} SEM JUROS.")
    print(f"\033[4;34mSua compra de R${valor:.2f} vai custar R${novo_valor * 2:.2f}\033[m")
elif opcao == 4:
    quantidade_de_parcelas = int(input("Digite a quantidade de parcelas: "))
    novo_valor = (valor / quantidade_de_parcelas) * 0.2 + (valor / quantidade_de_parcelas)
    #  novo_valor = valor + (valor * 0.2)
    # parcela = novo_valor / quantidade_de_parcelas
    print("\033[1;31mPROCESSANDO...\033[m")
    sleep(3)
    print(f"\033[4;34mSua compra será parcelada em {quantidade_de_parcelas}x de R${novo_valor:.2f} COM JUROS.\033[m")
    print(f"\033[4;34mSua compra de R${valor:.2f} vai custar R${novo_valor * quantidade_de_parcelas:.2f} no final.\033[m")
else:
    novo_valor = valor
    print("\033[1;35;46mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m")
print("\033[1;32m--FIM--\033[m")
