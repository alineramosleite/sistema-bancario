import textwrap
import random

# --------------------- Funções do sistema ---------------------

def menu():
    menu_text = """
    ==== Sistema Bancário ====
    1 - Criar usuário
    2 - Criar conta
    3 - Depositar
    4 - Sacar
    5 - Extrato
    6 - Listar contas
    7 - Sair
    """
    print(textwrap.dedent(menu_text))

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Erro: Valor inválido para depósito.")
        return saldo, extrato
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Erro: Número máximo de saques excedido.")
        return saldo, extrato, numero_saques
    if valor <= 0:
        print("Erro: Valor inválido para saque.")
        return saldo, extrato, numero_saques
    if valor > limite:
        print(f"Erro: Valor excede o limite de R$ {limite:.2f}")
        return saldo, extrato, numero_saques
    if valor > saldo:
        print("Erro: Saldo insuficiente.")
        return saldo, extrato, numero_saques

    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n==== Extrato ====")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=================\n")

def criar_usuario(usuarios):
    nome = input("Nome do usuário: ")
    cpf = input("CPF do usuário: ")
    if filtrar_usuario(cpf, usuarios):
        print("Erro: Usuário já cadastrado.")
        return
    usuarios.append({"nome": nome, "cpf": cpf})
    print(f"Usuário {nome} cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(usuarios):
    cpf = input("CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("Erro: Usuário não encontrado. Crie o usuário primeiro.")
        return None

    # Gerar agência e número da conta aleatórios
    agencia = str(random.randint(1000, 9999))
    numero_conta = str(random.randint(10000, 99999))

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "limite": 500,
        "numero_saques": 0,
        "limite_saques": 3
    }

    print(f"Conta criada com sucesso!\nAgência: {agencia}\nNúmero: {numero_conta}\nTitular: {usuario['nome']}")
    # Retorna apenas os dados principais
    return {"agencia": agencia, "numero_conta": numero_conta, "nome": usuario['nome']}, conta

def listar_contas(contas):
    print("\n==== Contas cadastradas ====")
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
    print("============================\n")

# --------------------- Função principal ---------------------

def main():
    usuarios = []
    contas = []

    while True:
        menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            criar_usuario(usuarios)

        elif opc == "2":
            conta_info, conta_completa = criar_conta(usuarios) or (None, None)
            if conta_completa:
                contas.append(conta_completa)

        elif opc == "3":
            numero = input("Número da conta: ")
            conta = next((c for c in contas if c["numero_conta"] == numero), None)
            if not conta:
                print("Conta não encontrada.")
                continue
            try:
                valor = float(input("Valor do depósito: "))
                conta["saldo"], conta["extrato"] = depositar(conta["saldo"], valor, conta["extrato"])
            except ValueError:
                print("Erro: Digite um valor numérico.")

        elif opc == "4":
            numero = input("Número da conta: ")
            conta = next((c for c in contas if c["numero_conta"] == numero), None)
            if not conta:
                print("Conta não encontrada.")
                continue
            try:
                valor = float(input("Valor do saque: "))
                conta["saldo"], conta["extrato"], conta["numero_saques"] = sacar(
                    saldo=conta["saldo"],
                    valor=valor,
                    extrato=conta["extrato"],
                    limite=conta["limite"],
                    numero_saques=conta["numero_saques"],
                    limite_saques=conta["limite_saques"]
                )
            except ValueError:
                print("Erro: Digite um valor numérico.")

        elif opc == "5":
            numero = input("Número da conta: ")
            conta = next((c for c in contas if c["numero_conta"] == numero), None)
            if not conta:
                print("Conta não encontrada.")
                continue
            exibir_extrato(conta["saldo"], extrato=conta["extrato"])

        elif opc == "6":
            listar_contas(contas)

        elif opc == "7":
            print("Sistema bancário encerrado.")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
