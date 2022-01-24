#Desafio ByLearner
# Classe Carro:
#   
#   Modelo => Definidos pelo construtor ("Quem define é a loja (classe)") =>␣ 
#       →Tem um valor inicial para cada um
#   Ano => Definidos pelo construtor ("Quem define é a loja (classe)") =>␣ 
#       →Tem um valor inicial para cada um
#   Estado => Definidos pelo construtor ("Quem define é a loja (classe)") =>␣
#       ,→Tem um valor inicial para cada um
#   Comprado => Vai ser Falso para todos => Valor inicial Padrão => É uma␣
#       →variáel de classe (e não de instância)
#
#
#   liga_desliga() => Liga e Desliga o carro => Obrigatório antes de dirigir/
#       fazer test drive
#   acelerar() => Só pode acelerar depois de comprar o carro... Mas vai
#       tentar mesmo assim
#   test_drive() => Só pode fazer antes de comprar => Não posso acelerar
#   comprar() => Só pode comprar uma vez
#   dirigir() => Você pode somente depois de comprar o carro => Pode acelerar
#   
# Modelo, Ano e Estado => São Atributos de Instância (Construtor)
# Comprado => Atributo da Classe (valor padrão inicial)
# Ligar e Desligar, Acelerar, Fazer Test Drive, Comprar e Dirigir => São Métodos


class Carro(object):
    comprado = False

    def __init__(self, modelo, ano, estado):
        self.modelo = modelo
        self.ano = ano
        self.estado = estado
        
    def comprar(self):
        if(self.comprado):
            print('Você já comprou, não pode comprar novamente!')
            return
        self.comprado = True
        print('Parabéns, você comprou o carro!')
    
    def test_drive(self):
        if(not self.comprado):
            print('Você vai fazer o Test Drive.')
            self.liga_desliga(True)
            print('Você está fazendo o Test Drive, espero que goste do carro!')
            if(self.acelerar()):
                print('Você está acelerando.')
            else:
                print('Você não pode acelerar enquanto não comprar.')
            self.liga_desliga(False)
            print('Você terminou o Test Drive.')
        else:
            print('Você não pode mais fazer o Test Drive pois já comprou o carro. Já pode dirigir.')

    def dirigir(self):
        if(self.comprado):
            print('Você vai dirigir.')
            self.liga_desliga(True)
            print('Você está dirigindo.')
            if(self.acelerar()):
                print('Você está acelerando.')
            else:
                print('Você não pode acelerar.')
            self.liga_desliga(False)
            print('Você terminou de dirigir')
        else:
            print('Você só pode dirigir depois de comprar o carro.')
    
    def acelerar(self):
        return self.comprado

    def liga_desliga(self, status):
            if status:
                print('Você ligou o carro!')
            else:
                print('Você desligou o carro!')

# Criação de carros

fusca = Carro('Fusca', '1984', 'usado')
gol = Carro('Gol', '1996', 'usado')

# Testes

print('***FAZENDO TEST DRIVE DO FUSCA***')
fusca.test_drive()

print('***TENTANDO DIRIGIR FUSCA ANTES DE COMPRAR***')
fusca.dirigir()

print('***COMPRANDO FUSCA***')
fusca.comprar()

print('***DIRIGINDO FUSCA COMPRADO***')
fusca.dirigir()

print('***TENTANDO FAZER TEST DRIVE DO FUSCA DEPOIS DE COMPRAR***')
fusca.test_drive()

print('***FAZENDO TEST DRIVE DO GOL***')
gol.test_drive()

print('***TENTANDO DIRIGIR GOL ANTES DE COMPRAR***')
gol.dirigir()