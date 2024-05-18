def menu():
    menu = """
    ================ EXTRATO ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair
    =========================================
    => """
    
    return input(menu)

def depositar(saldo, operacao, extrato, /):
    if operacao > 0:
        saldo += operacao
        extrato += f"Deposito: R$ {operacao:.2f}\n"
        print("Transação realizada com sucesso!")    
    else:
        print("Valor invalido! Tente novamente.")
        
    return saldo, extrato
    
def sacar(*, saldo, operacao, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = operacao > saldo
    excedeu_limite = operacao > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nSaldo insuficiente!")

    elif excedeu_limite:
        print(f"\nO valor desejada excede o limite de saque. O limite de saque da conta é de R$ {limite:.2f}")

    elif excedeu_saques:
        print("\nNúmero de saques diário excedido! Volte amanhã!")

    elif operacao > 0:
        saldo -= operacao
        extrato += f"Saque: R$ {operacao:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente os números): ")
    usuario = consultar_usuario(cpf, usuarios)
    
    if usuario:
        print ("Usuário já é o nosso cliente!")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, numero - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereco":endereco})
    
    print("Usuário criado!")

def consultar_usuario(cpf, usuarios):
    consulta = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return consulta[0] if consulta else None
        
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = consultar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}

    print("Usuario não encontrado.")

def listar_contas(contas):
    for conta in contas:
        dados_bancarios = f"""\
            Agência:\t{conta['agencia']}
            Conta:\t\t{conta['numero_conta']}
            Cliente:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(dados_bancarios)
        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0.0 
    limite = 500.0
    extrato = ""    
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            operacao = float(input("Informe o valor a ser depositado: "))
            
            saldo, extrato = depositar(saldo, operacao, extrato)

        elif opcao == "2":
            operacao = float(input("Informe o valor do saque desejado: "))
            
            saldo, extrato = sacar(
                saldo = saldo,
                operacao = operacao,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES 
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            criar_usuario(usuarios)
            
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)    
 
        elif opcao == "6":
            listar_contas(contas)
            
        elif opcao == "0":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
                      
main()    