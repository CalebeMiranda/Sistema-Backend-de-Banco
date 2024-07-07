class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"


class Conta:
    agencia = "0001"

    def __init__(self, numero_conta, cliente):
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0.0
        self.historico = Historico()
        self.quantidade_saque_diario = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_movimentacao(f"Depósito de R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if self.quantidade_saque_diario >= 3:
            print("Limite de saques diários atingido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 500:
            print("Valor de saque excede o limite de R$500,00.")
        else:
            self.saldo -= valor
            self.quantidade_saque_diario += 1
            self.historico.adicionar_movimentacao(f"Saque de R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def extrato(self):
        self.historico.exibir_extrato(self.saldo)

    def __str__(self):
        return f"Conta Número: {self.numero_conta}, Agência: {Conta.agencia}, Cliente: {self.cliente.nome}, Saldo: R${self.saldo:.2f}"


class Historico:
    def __init__(self):
        self.movimentacoes = []

    def adicionar_movimentacao(self, movimentacao):
        self.movimentacoes.append(movimentacao)

    def exibir_extrato(self, saldo):
        if not self.movimentacoes:
            print("Não houve movimentações na conta.")
        else:
            print("Extrato da conta:")
            for movimentacao in self.movimentacoes:
                print(movimentacao)
            print(f"Saldo atual: R${saldo:.2f}")


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.numero_conta = 1

    def criar_cliente(self):
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")
        cpf = input("Digite o CPF (somente números): ")
        endereco = input("Digite o endereço (logradouro, numero, bairro, cidade/Sigla estado): ")

        for cliente in self.clientes:
            if cliente.cpf == cpf:
                print("CPF já cadastrado. Tente novamente.")
                return

        cliente = Cliente(nome, data_nascimento, cpf, endereco)
        self.clientes.append(cliente)
        print("Usuário cadastrado com sucesso!")

    def criar_conta(self):
        cpf = input("Digite o CPF do usuário para criar a conta: ")

        for cliente in self.clientes:
            if cliente.cpf == cpf:
                conta = Conta(self.numero_conta, cliente)
                self.contas.append(conta)
                print(f"Conta criada com sucesso! Agência: {Conta.agencia}, Número da Conta: {self.numero_conta}")
                self.numero_conta += 1
                return

        print("Usuário não encontrado. Certifique-se de que o CPF está correto.")

    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        print("Conta não encontrada.")
        return None


def main():
    banco = Banco()

    while True:
        print("\nBem Vindo(a) ao Sistema de Banco!")
        print("[1] - Criar Usuário")
        print("[2] - Criar Conta")
        print("[3] - Fazer Depósito")
        print("[4] - Fazer Saque")
        print("[5] - Retirar Extrato")
        print("[6] - Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            banco.criar_cliente()
        elif escolha == 2:
            banco.criar_conta()
        elif escolha == 3:
            numero_conta = int(input("Digite o número da conta: "))
            conta = banco.buscar_conta(numero_conta)
            if conta:
                valor = float(input("Digite o valor do depósito: "))
                conta.deposito(valor)
        elif escolha == 4:
            numero_conta = int(input("Digite o número da conta: "))
            conta = banco.buscar_conta(numero_conta)
            if conta:
                valor = float(input("Digite o valor do saque: "))
                conta.saque(valor)
        elif escolha == 5:
            numero_conta = int(input("Digite o número da conta: "))
            conta = banco.buscar_conta(numero_conta)
            if conta:
                conta.extrato()
        elif escolha == 6:
            print("Obrigado por usar nossos serviços. Tenha um bom dia!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
