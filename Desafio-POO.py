import builtins
while True:
    class Bicicleta:
        def __init__(self, cor, modelo,ano,valor):
            self.cor= cor
            self.modelo= modelo
            self.ano= ano
            self.valor= valor
        def buzinar(self):
            print("Plimm Plimm...")
        
        def parar(self):
            print('A bicliceta esta parrando..')
            print('A bicicleta parrou.')
        
        def correr(self):
            print('Vrummm.....')



    cor=builtins.input('Digite a cor da bicicleta:')
    modelo=builtins.input('Digite o modelo da bicicleta: ')
    ano=int(builtins.input('Digite o ano da bicicleta:'))    
    valor=float(builtins.input('Digite o valor da bicicleta: '))

    b1=Bicicleta(cor,modelo,ano,valor)
    b1.correr()
    b1.buzinar()
    b1.parar()

    print('===== Dados Da bicicleta =====')
    print(f'Cor: {b1.cor}')
    print(f'Modelo: {b1.modelo}')
    print(f'Ano: {b1.ano}')
    print(f'Valor: R$ {b1.valor:.2f}')
    print('==============================')
    
    resp=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    print('='*40)
    if resp in 'Nn':
        break
print('Volte sempre!')