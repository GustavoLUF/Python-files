class Aluno:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def nome_metodo(self):
        ...

    def mostra_dados(self):
        dados = self.nome + ' - ' + str(self.idade)
        print(dados)

    def retorna_dados(self):
        dados = self.nome + ' - ' + str(self.idade)
        return dados


    
if __name__ == "__main__":
    aluno1 = Aluno('Gustavo', 1000, 18)
    print('Mostra a classe e a posição de memória onde o objeto foi criado: ', aluno1)
    print('Aluno 1: ')
    print('Nome: ', aluno1.nome)
    print('Mensalidade: ', aluno1.mensalidade)
    print('Idade: ', aluno1.idade)
