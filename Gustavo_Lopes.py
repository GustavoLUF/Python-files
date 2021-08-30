#Gustavo Lopes Urio Fonseca / RA: 22007103
#Questão 1
lista = []
print('Insira o número 0 para encerrar a lista.')
while True:
    valor = int(input("Insira um valor: "))
    if valor == 0:
        break
    lista.append(valor)
print('Aqui está a sua lista:\n', lista)
print('Vamos substituir o segundo valor na lista por 77.')
lista.pop(1)
lista.insert(1, 77)
print(lista)
valor = int(input('Digite o valor que quer encontrar na lista: '))
if valor in lista:
    print(f"\nO número {valor} foi encontrado na lista.")
    posicao = lista.index(valor)
    print(f'O número foi encontrado na posição: {posicao}')
else:
    print('Valor não encontrado.')

#===========================================================================================================================================================
#Questão 2
class Time:
    def __init__ (self, nome, estado, titulos=0, valor=0.0):
        self.nome = nome
        self.estado = estado
        self.titulos = titulos
        self.valor = valor

    def get_nome(self):
        return self.nome

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def atualiza_valor(self, atualiza_valor):
        self.valor += self.valor * atualiza_valor / 100

    def __str__(self):
        dados = f'Time: {self.nome}\nEstado: {self.estado}\nTitulos: {self.titulos}\nValor: {self.valor}'
        return dados
    
    def compara_titulos(self, outro_time):
        if time1.titulos > outro_time.titulos:
            print(f'O time com mais titulos é o {time1.nome}')
        else:
            print(f'O time com mais titulos é o {outro_time.nome}')

if __name__ == "__main__":

    quantos_times = int(input('O gerente está organizando uma lista com quantos times estão participando, digite a quantidade de participadores: '))
    print(f'O gerente verificou que extistem {quantos_times} times participando do campeonato.\n')
    time1 = Time('Bayern', '')
    time2 = Time('Atletic', '', 10)
    time3 = Time('Barcelona', '', '', 100)
    print(f'Nome do primeiro time: {time1.nome}')
    print(f'Nome do segundo time: {time2.nome}')
    print(f'Nome do terceiro time: {time3.nome}')
    time1.set_valor(150)
    time2.set_valor(140)
    time3.set_valor(120)
    print('Time 1:\n', time1)
    time1.atualiza_valor(20)
    time2.atualiza_valor(10)
    time3.atualiza_valor(5)
    print(f'Time 1:\n{time1}')
    print(f'Time 2:\n{time2}')
    print(f'Time 3:\n{time3}')
    time1.compara_titulos(time2)

#===========================================================================================================================================================
#Questão 3
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
        print('Acesso não consedido, você não tem acesso ao carro ou errou a senha.')