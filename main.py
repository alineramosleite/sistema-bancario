# Sistema Bancário - Projeto DIO

# Lista de contas
contas = []

# Função para buscar conta pelo nome
def buscar_conta(nome):
    """Retorna a conta do cliente pelo nome ou None se não existir"""
    for conta in contas:
        if conta["nome"] == nome:
            return conta
    return None

# Função para criar uma nova conta
def criar_conta():
    nome = input("Nome do cliente: ")
    if buscar_conta(nome):
        print("Erro: Já existe uma conta com esse nome.")
        return
    conta = {"nome": nome, "saldo": 0}
    contas.append(conta)
    print(f"Conta criada para {nome}!")

# Função para depositar valores
def depositar():
    nome = input("Nome do cliente: ")
    conta = buscar_conta(nome)
    if not conta:
        print("Erro: Usuário não cadastrado.")
        return
    valor = float(input("Valor do depósito: "))
    if valor <= 0:
        print("Erro: Valor inválido.")
        return
    conta["saldo"] += valor
    print(f"Depósito de R$ {valor:.2f} realizado para {nome}")

# Função para sacar valores
def sacar():
    nome = input("Nome do cliente: ")
    conta = buscar_conta(nome)
    if not conta:
        print("Erro: Usuário não cadastrado.")
        return
    valor = float(input("Valor do saque: "))
    if valor <= 0:
        print("Erro: Valor inválido.")
        return
    if conta["saldo"] >= valor:
        conta["saldo"] -= valor
        print(f"Saque de R$ {valor:.2f} realizado para {nome}")
    else:
        print("Saldo insuficiente.")

# Função para consultar saldo
def consultar_saldo():
    nome = input("Nome do cliente: ")
    conta = buscar_conta(nome)
    if not conta:
        print("Erro: Usuário não cadastrado.")
        return
    print(f"Saldo de {nome}: R$ {conta['saldo']:.2f}")

# Função para exibir o menu
def menu():
    while True:
        print("\n====Sistema Bancário==== ")
        print("\n1 - Criar conta\n2 - Depositar\n3 - Sacar\n4 - Consultar saldo\n5 - Sair")
        opc = input("Escolha uma opção: ")
        if opc == "1":
            criar_conta()
        elif opc == "2":
            depositar()
        elif opc == "3":
            sacar()
        elif opc == "4":
            consultar_saldo()
        elif opc == "5":
            break
        else:
            print("Opção inválida!")

# Execução do programa
if __name__ == "__main__":
    menu()
    print("Sistema bancário encerrado.")
    

