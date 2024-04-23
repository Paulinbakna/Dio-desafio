menu="""========================================
[1] = Depositar
[2] = Sacar
[3] = Visualizar Extrato
[4] = Sair do Bamco DIO
========================================
Opção Selecionada =>"""
saldo=0
limite=500
extrato=" "
numero_saques=0
LIMITE_SAQUES= 3
print('='*40)
print('Bem vindo ao Banco DIO!'.center(40))
while True:
    n=input(menu)
    if n == "1":
        print('='*40)
        valor=int(input('Digite o Valor que você deseja  depositar R$: '))
        if valor> 0:
            saldo+=valor
            print(f'Deposito de R$ {valor} realizado com sucesso')
            extrato+= f"Deposito: R$ {valor:.2f}\n"
        else:
            print(' Operação falhou! O valor informado é invalido')
    elif n == "2":
        valor=float(input("Digite  o valor que deseja sacar R$: "))
        
        excedeu_saldo=valor>saldo
        
        excedeu_limite=valor>limite
        
        excedeu_saques=numero_saques>LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Operação falhou! Você não possui saldo suficiente para sacar.')
        
        elif excedeu_limite:
            print('Operação falhou! O valor digitado passou do limite .')
        elif excedeu_saques:
            print('Operação Falhou! Você passou do limite de saques diario!')
        elif valor > 0:
            saldo-=valor
            numero_saques +=1
            print(f'Saque no valor de R$ {valor} realizado com sucesso')
            extrato+= f'Saque R$ {valor:.2f}\n '
        else:
            print('Operação Falhou! O valor digitado e invalido')
    elif n == '3':
        print('='*40)
        print('EXTRATO'.center(40))
        print('Até o momento nao foram realizadas movimentações na sua conta.' if not extrato else extrato)
        print(f'Saldo da conta: R$ {saldo:.2f}')
    elif n == '4':
        break
    else:
        print('Não Indentifiquei a opção selecionada, por favor digite novamente.')
print('='*40)
print('Obrigado por usar o Banco-DIO! Volte sempre!')
print('='*40)
