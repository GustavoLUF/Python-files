class Veículo(object):
    def __init__(self, tipo, marca, valor):
        self.tipo = tipo
        self.marca = marca
        self.valor = valor

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, novo_tipo):
        self.nome = novo_tipo

    def get_marca(self):
        return self.marca

    def get_valor(self):
        return self.valor

    def __str__(self):
        s = f'Tipo: {self.tipo}, Marca: {self.marca}, Valor: {self.valor:.2f} '
        return s

    def valor_total(self):
        total = self.valor + self.imposto()
        return total

class CarrodeLuxo(Veículo):
    def __init__(self, tipo, marca, valor, senha, potencia):
        super().__init__(tipo, marca, valor)  
        self.senha = senha
        self.potencia = potencia

    def get_qtd_gerencia(self):
        return self.qtd_gerencia

    def autentica(self, senha):
        if self.senha == senha:
            print('Acesso concedido ao carro de luxo.')
            return
        else:
            print('Acesso negado ao carro de luxo..')
            return

    def __str__(self):
        s1 = super().__str__()       
        s = s1 + f'Quantidade de cavalos: {self.potencia}'
        return s

    def valor_total(self):
        total =  super().valor_total() + 1000
        return total

if __name__ == '__main__':
    v1 = Veículo('Moto', 'Yamaha', 7000)
    (v1.get_tipo())
    (v1.get_marca())
    (v1.get_valor())
    r = v1
    print(r)
    carro1 = CarrodeLuxo('Mercedez C180', 'Mercedez', 200.000, 'M180', 5)
    (carro1.get_tipo())
    print(carro1.__str__())
    print('Acesso ao carro de luxo.')
    user = input('Carro: ')
    if user == carro1.get_tipo():
        print('Prossiga para a senha para desbloquear a compra do carro.')
        senha = input('Senha: ')
        if senha == carro1.senha:
            ver_senha = carro1.autentica('M180')
            print(ver_senha)
        else:
            print('Acesso negado!')
    else:
        print('Acesso não concedido, você não tem acesso ao carro ou errou a login/senha.')