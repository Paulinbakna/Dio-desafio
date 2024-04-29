def menu():        
    menu_text = """========================================
[1] = Depositar
[2] = Sacar
[3] = Visualizar Extrato
[4] = Criar Conta
[5] = Criar Usuário
[6] = Lista de Contas
[7] = Sair do Banco DIO
========================================
Opção Selecionada => """
    return menu_text

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        print(f'Depósito de R$ {valor} realizado com sucesso')
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print('\n Operação falhou! O valor informado é inválido')

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques
    if excedeu_saldo:
        print('\nOperação falhou! Você não possui saldo suficiente para sacar.')
    
    elif excedeu_limite:
        print('\nOperação falhou! O valor digitado ultrapassou o limite.')
    
    elif excedeu_saques:
        print('\nOperação falhou! Você ultrapassou o limite de saques diários!')
    
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        print(f'Saque no valor de R$ {valor} realizado com sucesso')
        extrato += f'Saque R$ {valor:.2f}\n '
    
    else:
        print('\nOperação falhou! O valor digitado é inválido')
    return saldo, extrato
    
def exibir_extrato(saldo, extrato):
    print('=' * 40)
    print('EXTRATO'.center(40))
    print('Até o momento não foram realizadas movimentações na sua conta.' if not extrato else extrato)
    print(f'Saldo da conta: R$ {saldo:.2f}')

def criar_usuario(usuarios):
    cpf = input("Informe o número do seu CPF (digite somente os números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\nCPF já cadastrado no banco!')
        return
    nome = input("Digite seu nome completo: ")
    data_nascimento = input('Digite sua data de nascimento: ')
    endereco = input('Digite o seu endereço completo (Ex: Setor-bairro-n° da rua): ')
    cidade = input('Informe a cidade onde você mora: ')
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "cidade": cidade})
    print('=' * 40)
    print(f'O usuário {nome} foi cadastrado com sucesso no Banco-DIO!')
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.get("cpf") == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
        
    if usuario:
        print("=" * 40)
        print('Conta no Banco-DIO criada com sucesso!')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado! Para visualizar sua conta no Banco-DIO você precisa criar um usuario (digite 5 para criar)")

def listar_contas(contas):
    if contas:
        for conta in contas:
            linha = f"""
                Agência: {conta['agencia']}
                Conta: {conta['numero_conta']}
                Titular: {conta['usuario']['nome']}
                """
            print('=' * 40)
            print(linha)  # Corrigindo a indentação e adicionando a linha para impressão
    else:
        print("\nNão possui contas cadastradas.")  # Mensagem quando não há contas

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    usuario_criado = False  # Variável para controlar se o usuário foi criado ou não
    
    print('=' * 40)
    print('Bem vindo ao Banco DIO!'.center(40))
    while True:
        opcao = input(menu())
        
        if opcao == "1" and usuario_criado:  # Verificando se o usuário foi criado
            print('=' * 40)
            valor = int(input('Digite o valor que você deseja depositar R$: '))
            saldo, extrato = depositar(saldo, valor, extrato)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    usuario_criado = False  # Variável para controlar se o usuário foi criado ou não
    
    print('=' * 40)
    print('Bem vindo ao Banco DIO!'.center(40))
    while True:
        opcao = input(menu())
        
        if opcao == "1" and usuario_criado:  # Verificando se o usuário foi criado
            print('=' * 40)
            valor = int(input('Digite o valor que você deseja depositar R$: '))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        if opcao == '1' and usuario_criado == False:
            print('\nPara poder depositar você precisa criar um usuario no Banco-DIO! (Selecione a opção 5 para realizar seu cadastro)')
        
        if opcao == "2" and usuario_criado:  # Verificando se o usuário foi criado
            valor = float(input("Digite o valor que deseja sacar R$: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES)
            
        if opcao =='2' and usuario_criado ==False:
            print('\nPara poder realizar um saque e necessario criar um usuario no Banco-DIO!(Selecione a opção 5 para realizar seu cadastro)')    
        
        if opcao == '3' and usuario_criado: 
            exibir_extrato(saldo, extrato=extrato)
            
        if opcao == '3' and usuario_criado == False:
            print('\nPara visualizar o extrato e necessario criar um usuario no Banco-DIO!(Selecione a opção 5 para realizar seu cadastro)')    
        
        if opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)  
        
        if opcao =='5':
            criar_usuario(usuarios)
            usuario_criado = True  # Marcando que o usuário foi criado
        
        if opcao =='6': 
            if contas:
                listar_contas(contas)
            else:
                print("\nNão possui contas cadastradas.")
        
        
        if opcao == '7':
            print('=' * 40)
            print('Obrigado por usar o Banco-DIO! Volte sempre!')
            print('=' * 40)
            break
        
        if opcao not in '1''2''3''4''5''6''7':
            print('Opção não reconhecida, por favor digite novamente.')

main()
