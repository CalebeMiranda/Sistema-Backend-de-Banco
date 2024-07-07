# Sistema de Banco Versão 2
# Apenas 3 operações: Depósito, Saque e Extrato
# Agora todas as operações são funções.
# Depósito: Somente valores positivos (obviamente) somente de uma conta. E deve ser printável no extrato
# Saque: Somente 3 saques diários com limite de R$ 500,00 por saque. Todos os saques devem ser armazenados em uma variável 
# e printados no extrato
# Extrato: Deve listar o último Depósito e Saques da conta. Exibir no final o saldo. Caso não tenha sido feita movimentações, avisar.
# Criação de Usuário: Criação de Usuários para restringir o número de contas no sistema.
# Criação de Contas: Cria contas do usuário e maior controle sobre as operações

deposito = 0
saldo = 0
flag = 0
quantidadedesaque = 0
historicodesaque = ""
usuarios = []
contas = []
numero_conta = 1
agencia = "0001"

def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")
    cpf = input("Digite o CPF (somente números): ")
    endereco = input("Digite o endereço (logradouro, numero, bairro, cidade/Sigla estado): ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado. Tente novamente.")
            return usuarios

    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuarios

def criar_conta(contas, usuarios, numero_conta):
    cpf = input("Digite o CPF do usuário para criar a conta: ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            conta = {
                'agencia': agencia,
                'numero_conta': numero_conta,
                'usuario': usuario
            }
            contas.append(conta)
            print(f"Conta criada com sucesso! Agência: {agencia}, Número da Conta: {numero_conta}")
            numero_conta += 1
            return contas, numero_conta

    print("Usuário não encontrado. Certifique-se de que o CPF está correto.")
    return contas, numero_conta

def operacao_deposito(saldo):
    deposito = float(input("Digite o valor desejado para depositar na sua conta: "))
    if deposito < 0:
        print("\nNão é possível depositar valor negativo. Operação terminada.")
    else:
        saldo += deposito
        print(f"\nSeu Saldo atual é R${saldo:.2f} \n")
    return saldo, deposito

def operacao_saque(quantidadedesaque, saldo, historicodesaque):
    if quantidadedesaque >= 3:
        print("\nVocê já efetuou sua quantidade máxima de saques diários, favor volte amanhã.")
    else:
        saque = float(input("\nQual o valor que deseja sacar?\n: "))
        if saque > saldo:
            print("\nValor de Saque maior do que o Saldo disponível. Favor, tente novamente.")
        elif saque > 500:
            print("\nValor de Saque excede o limite de R$500,00 por saque. Favor tente um valor menor.")
        else:
            saldo -= saque
            quantidadedesaque += 1
            historicodesaque += f"\nSaque {quantidadedesaque} = R${saque:.2f}"
            print(f"\nSaque de R${saque:.2f} efetuado com sucesso. Seu Saldo atual é de R${saldo:.2f} \n")
    return quantidadedesaque, saldo, historicodesaque

def operacao_extrato(deposito, historicodesaque, saldo, movimentacao):
    if movimentacao == 0:
        print("\nNão houve movimentação na conta!")
    else:
        if deposito == 0:
            print("\nNão foi feito um novo depósito, fora o primeiro!")
        else:
            print(f"Seu último valor de depósito foi: R${deposito:.2f}")
        print("\nHistórico de saques:")
        print(historicodesaque)
        print(f"Seu Saldo atual é R${saldo:.2f} \n")

def main():
    global saldo, deposito, quantidadedesaque, historicodesaque, flag, usuarios, contas, numero_conta
    movimentacao = 0

    while flag !=1:
        print("\nBem Vindo(a)! Vamos criar um novo usuário.")
        usuarios = criar_usuario(usuarios)
        
        while flag !=1:
            escolha = int(input("O que deseja fazer agora?\n[1] - Criar Conta \n[2] - Fazer Depósito \n[3] - Fazer Saque \n[4] - Retirar extrato \n[5] - Terminar Programa \n"))
            if escolha == 1:
                contas, numero_conta = criar_conta(contas, usuarios, numero_conta)
            elif escolha == 2:
                movimentacao = 1
                saldo, deposito = operacao_deposito(saldo)
            elif escolha == 3:
                movimentacao = 1
                quantidadedesaque, saldo, historicodesaque = operacao_saque(quantidadedesaque, saldo, historicodesaque)
            elif escolha == 4:
                operacao_extrato(deposito, historicodesaque, saldo, movimentacao)
            elif escolha == 5:
                print("\nObrigado por usar nossos serviços, tenha um bom dia!")
                flag = 1
                break
    

if __name__ == "__main__":
    main()
