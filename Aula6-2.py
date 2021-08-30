class Veiculo(object):
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_valor(self):
        return self.valor

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print('Valor inconsistente, valor negativo.')
    
    def mostra_dados(self):
        print('Modelo: ', self.modelo)
        print('Ano: ', self.ano)
        print('Valor: ', self.valor)

    def retorna_dados(self):
        dados = self.modelo + ' - ' + str(self.ano) + ' - ' + str(self.valor)
        return dados

    def aumento_valor(self, valor):
        
    


if __name__ == "__main__":
    carro1 = Veiculo('HB', 2000, 30000)
    carro2 = Veiculo('Corolla', 2019, 70000)
    retorno = carro1.get_modelo()
    print('Modelo: ', retorno)
    print('Modelo: ', carro2.get_modelo())
    carro1.set_modelo('HB20')
    print(carro1.get_modelo())
    carro1.set_valor(32000)
    print(carro1.get_valor())
    carro2.set_valor(-12000)
    print(carro2.get_valor())
    carro1.mostra_dados()
    carro2.mostra_dados()
    print('Dados Concatenados: ', carro1.retorna_dados())
    carro1.aumento_valor(400)
    print('Novo valor: ', carro1.retorna_dados())
    vl_aumento = float(input('Valor aumento'))
    carro2.aumento_valor(vl_aumento)
    print(carro2.get_valor())