class Aluno(object):
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
    
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_mensalidade(self):
        return self.mensalidade

    def set_mensalidade(self, valor):
        self.mensalidade = valor
    
    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def mostra_dados(self):
        print('Nome: ', self.nome)
        print('Mensalidade: ', self.mensalidade)
        print('Idade: ', self.idade)
    
    def mostra_dados_2(self):
        print('Nome: ', self.get_nome())
        print('Mensalidade: ', self.get_mensalidade())
        print('Idade: ', self.get_idade())

    def retorna_dados(self):
        dados = self.nome + ' - ' + str(self.mensalidade) + ' - ' + str(self.idade)
        #dados = self.get_nome() + ' - ' + str(self.get+mensalidade()) + ' - ' + str(self.get_idade())
        return dados

    def aumento_mensalidade_valor(self, valor):
        self.mensalidade += valor

    def aumento_mensalidade_porcentagem(self, pct):
        self.mensalidade += self.mensalidade * pct / 100


if __name__ == "__main__":
    aluno1 = Aluno('Gustavo', 756, 18)
    aluno2 = Aluno('Luca', 800, 8)
    print('Aluno 1:')
    print('Nome: ', aluno1.get_nome())
    print('Mensalidade: ', aluno1.get_mensalidade())
    print('Idade: ', aluno1.get_idade())
    print('Aluno 2:')
    print('Nome: ', aluno2.get_nome())
    print('Mensalidade: ', aluno2.get_mensalidade())
    print('Idade: ', aluno2.get_idade())
    novo_nome = input('Novo nome: ')
    aluno1.set_nome(novo_nome)
    aluno2.set_nome('João')
    aluno1.mostra_dados()
    aluno2.mostra_dados()
    aluno1.mostra_dados_2()
    aluno2.mostra_dados_2()
    print('Dados concatenados: ', aluno1.retorna_dados())
    print('Dados concatenados: ', aluno2.retorna_dados())