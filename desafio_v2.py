def saque (*,saldo, valor, extrato, limite ,numero_saques, limite_saques):
    valor = float(input("\nValor que deseja sacar => "))
    if valor > 0:
        if valor <= saldo and numero_saques < limite_saques:
            if valor <= limite:
                saldo-=valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques+=1
                print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("\nNão foi possível realizar o saque, pois valor limite de saque é R$ 500.00")
        elif valor > saldo:
            print("\nNão foi possível realizar o saque, pois está saldo insuficiente.")
        else:
            print("\nNão foi possível realizar o saque, pois o limite de saque diário foi atingido.")
    else:
        print("\nValor inválido!")
    return saldo, extrato, numero_saques
# ///////////////////////////////////////////////////
def deposito(saldo,valor,extrato,/):
    valor = float(input("\nValor que deseja depositar => "))
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nValor inválido!")
    return saldo, extrato
# ///////////////////////////////////////////////////
def extrato(saldo,*,extrato):
    if extrato == "":
        print("\nNão foi realizado nenhuma movimentação.\n")
    else:
        print(f"\n{extrato}")
        print(f"Saldo atual: R$ {saldo:.2f}\n")
# ///////////////////////////////////////////////////
def criar_usuario(verificacao_user,/):
    cpf, endereco, name, date = "", "", "", ""
    while True:
        retorno = False
        cpf = input("Digite o CPF => ")
        for indice, x in enumerate(verificacao_user):
            if cpf in verificacao_user[indice]["cpf"]:
                print("\nUsuário já cadastrado!\n")
                retorno = True
                break
        if retorno: return 0
        name = input("Digite o nome => ")
        date = input("Digite a data de nascimento (dia/mes/ano) => ")
        endereco = input("Digite seu endereço (logradouro - bairro - cidade/sigla estado)=>")
        break
    user = [{"nome":name,"data":date, "cpf":cpf, "endereco":endereco}]
    return user
# ///////////////////////////////////////////////////
def candastrar_conta_corrente(verificacao_conta, verificacao_user,/):
    AGENCIA = "0001"
    numero_conta = 0
    retorno = False
    cpf = input("Digite o CPF que queira criar a conta => ")
    for indice_cpf, x in enumerate(verificacao_user):
        if cpf in verificacao_user[indice_cpf]["cpf"]:
            numero_conta = len(verificacao_conta) + 1
            retorno = True
            break
    conta = [{"numero_conta":numero_conta, "agencia":AGENCIA, "cpf":cpf}]
    if retorno:
        print("\nConta Criada com Sucesso!\n")
        return conta
    else:
        print("\nUsauário não Cadastrado!\n")
        return 0
# ///////////////////////////////////////////////////
menu = '''

========= MENU =========

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastrar Usuário
    [5] - Cadastrar Conta
    [6] - Mostrar Usuários
    [7] - Mostrar Contas
    [0] - Sair

========================

=> '''

saldo = 0.00
valor = 0.00
limite = 500.00
info = ""
users = [{"nome":"Jonathan","data":"21/03/1998", "cpf":"10958756473", "endereco":"Rua Deão faria"}, {"nome":"Bianca","data":"04/07/2002", "cpf":"123", "endereco":"Rua 11 Fevereior"}]
contas = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("### Depósito ###")
        saldo, info = deposito(saldo,valor,info)

    elif opcao == 2:
        print("### Sacar ###")
        saldo, info, numero_saques = saque(saldo=saldo,valor=valor,limite=limite, extrato=info, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == 3:
        print("### Extrato ###")
        extrato(saldo, extrato=info)
        print("###############")

    elif opcao == 4:
        print("### Criar Usuário ###")
        analisador = criar_usuario(users)
        if analisador != 0:
            users.extend(analisador)

    elif opcao == 5:
        print("### Cadastrar Conta Corrente ###")
        analisador = candastrar_conta_corrente(contas,users)
        if analisador != 0:
            contas.extend(analisador)

    elif opcao == 6:
        print("### Mostrar Usuários ###")
        if len(users) == 0:
            print("\nNenhuma conta foi cadastrada.\n")
        else:
            for x in users:
                print(x)

    elif opcao == 7:
        print("### Mostrar Contas ###")
        if len(contas) == 0:
            print("\nNenhuma conta foi cadastrada.\n")
        else:
            for x in contas:
                print(x)

    elif opcao == 0:
        print("### Sair ###")
        break

    else:
        print('Apresemte apenas uma das opções válidas!')