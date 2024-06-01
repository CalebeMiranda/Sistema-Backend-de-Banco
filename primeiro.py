# Sistema de Banco Versão 1
# Apenas 3 operações: Depósito, Saque e Estrato

# Depósito: Somente valores positivos (obviamente) somente de uma conta. E deve ser printável no extrato

# Saque: Somente 3 saques diários com limite de R$ 500,00 por saque. Todos os saques devem ser armazenados em uma variável 
# e printados no extrato

#Extrato: Deve listar o último Depósito e Saques da conta. Exibir no final o saldo. Caso não tenha sido feita movimentações, avisar.

deposito = 0
saldo = 0

flag = -1
flag2 = 0

quantidadedesaque = 0
saque = 0
saque1 = ""
saque2 = ""
saque3 = ""
historicodesaque =""

movimentacao = 0

while flag != 0:
    print("\nBem Vindo(a) ! Esse é seu primeio acesso, favor faça um depósito:")
    saldo = float(input("Deposite o valor desejado na sua conta: "))
    if saldo < 0:
        print("\nNão é possível depositar valor negativo. Operação terminada.")
        flag = 0
    else:
        print(f"Seu Saldo atual é R${saldo:.2f} \n")
        flag = 0
        flag2 = -2


print( )


while flag2 != 0:
    escolha = int(input("O que deseja fazer agora?\n[1] -Fazer Depósito \n[2] -Fazer Saque \n[3] -Retirar extrato \n[4] -Terminar Programa \n"))    
    if escolha == 1:
        movimentacao = 1
        deposito = float(input("Digite o valor desejado para depositar na sua conta: "))
        if deposito < 0:
            print("\nNão é possível depositar valor negativo. Operação terminada.")
            flag2 = 0
        else:
            saldo = saldo + deposito
            print(f"\nSeu Saldo atual é R${saldo:.2f} \n")


    elif escolha == 2:
        if quantidadedesaque >= 3:
            print("\nVocê já efetuou sua quantidade máxima de saques diários, favor volte amanhã.")
        else:
            saque = float(input("\nQual o valor que deseja sacar?\n: "))

            if saque > saldo:
                print("\n Valor de Saque maior do que o Saldo disponível. Favor, tente novamente.")
            elif saque > 500:
                print("\n Valor de Saque excede o limite de R$500,00 por saque. Favor tente um valor menor.")
            else:
                movimentacao = 1
                saldo = saldo - saque
                print(f"\nSaque de R${saque:.2f} efetuado com sucesso. Seu Saldo atual é de R${saldo:.2f} \n")
                
                if saque1 != "" and saque2 != "":
                    saque3 = f"\n Terceiro Saque = R${saque:.2f}"
                    quantidadedesaque = quantidadedesaque + 1
                elif saque1 != "":
                    saque2 = f"\n Segundo Saque = R${saque:.2f}"
                    quantidadedesaque = quantidadedesaque + 1
                else:
                    saque1 = f"\n Primeiro Saque = R${saque:.2f}"
                    quantidadedesaque = quantidadedesaque + 1

                historicodesaque = saque1 + saque2 + saque3

    elif escolha == 3:

        if movimentacao == 0:
            print("\n Não houve movimentação na conta !")
        else:
            if deposito == 0:
                print("\nNão foi feito um novo depósito, fora o primeiro !")
            else:
                print(f"Seu último valor de depósito foi: {deposito:.2f}")

            print("\nHistórico de saques:")
            print(historicodesaque)
            print(f"Seu Saldo atual é R${saldo:.2f} \n")

    elif escolha == 4:
        print("\nObrigado por usar nossos serviços, tenha um bom dia !")
        flag2 = 0
print( )

