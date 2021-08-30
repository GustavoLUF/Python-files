class Aluno:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def mostra_dados(self):
        dados = self.nome + ' - ' + str(self.idade)
        print(dados)

    def retorna_dados(self):
        dados = self.nome + ' - ' + str(self.idade)
        return dados

    def pode_cnh(self):
        if self.idade >= 18:
            print('Maior de Idade e pode obter a CNH.')
        else:
            print('Menor de Idade e não pode obter a CNH.')


if __name__ == "__main__":
    aluno1 = Aluno("Gustavo", 1000, 18)
    print('Mostra a classe e a posição de memória onde o objeto foi criado: ', aluno1)
    print('Aluno 1: ')
    print('Nome: ', aluno1.nome)
    print('Mensalidade: ', aluno1.mensalidade)
    print('Idade: ', aluno1.idade)
    aluno2 = Aluno('Adriane', 800, 35)
    print('Aluno 2: ')
    print("Nome: ", aluno2.nome)
    print("Mensalidade: ", aluno2.mensalidade)
    print('Idade: ', aluno2.idade)
    nova_mensalidade = input('Digite a nova mensalidade: ')
    aluno2.mensalidade = nova_mensalidade
    print('A nova mensalidade do aluno 2 é: ', aluno2.mensalidade)
    aluno3 = Aluno('Luca', 600, 8)
    print('Aluno 3: ')
    print('Nome: ', aluno3.nome)
    print('Mensalidade: ', aluno3.mensalidade)
    print('Idade: ', aluno3.idade)
    aluno1.mostra_dados()
    aluno2.mostra_dados()
    aluno3.mostra_dados
    print(aluno1.retorna_dados())
    print(aluno2.retorna_dados())
    print(aluno3.retorna_dados())
    aluno1.pode_cnh()
    aluno2.pode_cnh()
    aluno3.pode_cnh()
