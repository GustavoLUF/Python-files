
from abc import ABC, abstractmethod


class Remedio(ABC):
    def __init__(self, nome, preco, tarja):
        self.nome = nome
        self.preco = preco
        self.classificacao = ['de marca', 'Genérico', 'Similar']
        self.tarja = tarja

    def get_tarja(self):
        return self.tarja

    def set_tarja(self):
        tarjas = input('Possui tarja, se sim, qual?')

        if tarjas == 'Vermelha':
            self.tarja = 'Vermelha.'

        elif tarjas == 'Preta':
            self.tarja = 'Preta.'

        elif tarjas == 'Amarela':
            self.tarja = 'Amarela.'

        else:
            self.tarja = 'Nenhuma.'

    def get_nome(self):
        return self.preco

    def set_nome(self, ):
        valor = input('Digite o nome do remédio: ')

    def get_preco(self):
        return self.preco

    def set_preco(self):
        valor = float(input('Digite o valor do remédio: R$ '))
        self.preco = valor

    def get_classificacaoremedio(self):
        return self.classificacao

    def set_classificacaoremedio(self):
        classif = input("""Classificação do remédio:\n
                        [1] De marca
                        [2] Genérico
                        [3] Similar\n\nEm qual se encaixa o remédio apresentado? """).capitalize().strip()
        if classif == 1:
            self.classificacao = self.classificacao[0]
        elif classif == 2:
            self.classificacao = self.classificacao[1]
        elif classif == 3:
            self.classificacao = self.classificacao[2]

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def prescricao(self):
        pass


class Bacteriana(Remedio):
    def __init__(self, nome, preco, tarja):
        super().__init__(nome, preco, tarja)

    def tipo(self):
        return 'Antibiótico.'

    def prescricao(self):
        if self.tarja == 'Vermelha.':
            print('Prescrição opcional, de acordo com a retenção da receita.')

        elif self.tarja == 'Preta.':
            print('Prescrição necessária.')

        elif self.tarja == 'Amarela.':
            print('Prescrição não necessária.')

        else:
            print('Prescrição não necessária.')

    def get_classificacaoremedio(self):
        return self.classificacao

    def set_classificacaoremedio(self):
        classif = input("""Classificação do remédio:\n
                        [1] De marca
                        [2] Genérico
                        [3] Similar\n\nEm qual se encaixa o remédio apresentado? """).capitalize().strip()
        if classif == 1:
            self.classificacao = self.classificacao[0]
            return
        elif classif == 2:
            self.classificacao = self.classificacao[1]
            return
        elif classif == 3:
            self.classificacao = self.classificacao[2]
            return

    def mostradados(self):
        print(f"""Indicação para doenças/gripes/infecções bacterianas:\n
         * {self.nome}
         * {self.preco:.2f}
         * {self.tipo()}
         * {self.get_classificacaoremedio()}
         * {self.get_tarja()}
         * {self.prescricao()}
""")


class Dor(Remedio):
    def __init__(self, nome, preco, tarja):
        super().__init__(nome, preco, tarja)

    def tipo(self):
        return 'Analgésico.'

    def prescricao(self):
        if self.tarja == 'Vermelha.':
            print('Prescrição opcional, de acordo com a retenção da receita.')

        elif self.tarja == 'Preta.':
            print('Prescrição necessária.')

        elif self.tarja == 'Amarela.':
            print('Prescrição não necessária.')

        else:
            print('Prescrição não necessária.')

    def get_classificacaoremedio(self):
        return self.classificacao

    def set_classificacaoremedio(self):
        classif = input("""Classificação do remédio:\n
                        [1] De marca
                        [2] Genérico
                        [3] Similar\n\nEm qual se encaixa o remédio apresentado? """).capitalize().strip()
        if classif == 1:
            self.classificacao = self.classificacao[0]
            return
        elif classif == 2:
            self.classificacao = self.classificacao[1]
            return
        elif classif == 3:
            self.classificacao = self.classificacao[2]
            return

    def mostradados(self):
        print(f"""Indicação para dores:\n
         * {self.nome}
         * {self.preco:.2f}
         * {self.tipo()}
         * {self.get_classificacaoremedio()}
         * {self.get_tarja()}
         * {self.prescricao()}
""")


class Infeccao(Remedio):
    def __init__(self, nome, preco, tarja):
        super().__init__(nome, preco, tarja)

    def tipo(self):
        return 'Anti-inflamatório.'

    def prescricao(self):
        if self.tarja == 'Vermelha.':
            print('Prescrição opcional, de acordo com a retenção da receita.')

        elif self.tarja == 'Preta.':
            print('Prescrição necessária.')

        elif self.tarja == 'Amarela.':
            print('Prescrição não necessária.')

        else:
            print('Prescrição não necessária.')

    def get_classificacaoremedio(self):
        return self.classificacao

    def set_classificacaoremedio(self):
        classif = input("""Classificação do remédio:\n
                        [1] De marca
                        [2] Genérico
                        [3] Similar\n\nEm qual se encaixa o remédio apresentado? """).capitalize().strip()
        if classif == 1:
            self.classificacao = self.classificacao[0]
            return
        elif classif == 2:
            self.classificacao = self.classificacao[1]
            return
        elif classif == 3:
            self.classificacao = self.classificacao[2]
            return

    def mostradados(self):
        print(f"""Indicação para infecções de outros tipos e inflamações:\n
         * {self.nome}
         * {self.preco:.2f}
         * {self.tipo()}
         * {self.get_classificacaoremedio()}
         * {self.get_tarja()}
         * {self.prescricao()}
""")


class Cronica(Remedio):
    def __init__(self, nome, preco, tarja):
        super().__init__(nome, preco, tarja)

    def tipo(self):
        return 'Analgésico.'

    def prescricao(self):
        if self.tarja == 'Vermelha.':
            print('Prescrição opcional, de acordo com a retenção da receita.')

        elif self.tarja == 'Preta.':
            print('Prescrição necessária.')

        elif self.tarja == 'Amarela.':
            print('Prescrição não necessária.')

        else:
            print('Prescrição não necessária.')

    def get_classificacaoremedio(self):
        return self.classificacao

    def set_classificacaoremedio(self):
        classif = input("""Classificação do remédio:\n
                        [1] De marca
                        [2] Genérico
                        [3] Similar\n\nEm qual se encaixa o remédio apresentado? """).capitalize().strip()
        if classif == 1:
            self.classificacao = self.classificacao[0]
            return
        elif classif == 2:
            self.classificacao = self.classificacao[1]
            return
        elif classif == 3:
            self.classificacao = self.classificacao[2]
            return

    def mostradados(self):
        print(f"""Indicação para doenças crônicas, psicológicas:\n
         * {self.nome}
         * {self.preco:.2f}
         * {self.tipo()}
         * {self.get_classificacaoremedio()}
         * {self.get_tarja()}
         * {self.prescricao()}
""")


class Vermes(Remedio):
    def __init__(self, nome, preco, tarja):
        super().__init__(nome, preco, tarja)

    def tipo(self):
        return 'Vermicida.'

    def prescricao(self):
        if self.tarja == 'Vermelha.':
            print('Prescrição opcional, de acordo com a retenção da receita.')

        elif self.tarja == 'Preta.':
            print('Prescrição necessária.')

        elif self.tarja == 'Amarela.':
            print('Prescrição não necessária.')

        else:
            print('Prescrição não necessária.')

    def get_classificacaoremedio(self):
        return self.classificacao

    def set_classificacaoremedio(self):
        classif = input("""Classificação do remédio:\n
                        [1] De marca
                        [2] Genérico
                        [3] Similar\n\nEm qual se encaixa o remédio apresentado? """).capitalize().strip()
        if classif == 1:
            self.classificacao = self.classificacao[0]
            return
        elif classif == 2:
            self.classificacao = self.classificacao[1]
            return
        elif classif == 3:
            self.classificacao = self.classificacao[2]
            return

    def mostradados(self):
        print(f"""Indicação para doenças crônicas, psicológicas:\n
         * {self.nome}
         * {self.preco:.2f}
         * {self.tipo()}
         * {self.get_classificacaoremedio()}
         * {self.get_tarja()}
         * {self.prescricao()}
""")


if __name__ == '__main__':
    bac = Bacteriana('Amoxicilina', 30.00, 'Vermelho')
    bac.set_classificacaoremedio()
    bac.set_tarja()
    bac.mostradados()

    dor = Dor('Dorflex', 14.59, 'Nenhuma')
    dor.set_nome()
    dor.get_nome()
    dor.set_preco()
    dor.get_preco()
    dor.set_classificacaoremedio()
    dor.get_classificacaoremedio()
    dor.set_tarja()
    dor.get_tarja()
    dor.mostradados()

    infec = Infeccao('Cetoconazol', 9.70, 'Nenhuma')
    infec.set_classificacaoremedio()
    infec.set_tarja()
    infec.mostradados()

    cron = Cronica('Ritalina', 79.90, 'Preta')
    cron.set_classificacaoremedio()
    cron.set_tarja()
    cron.mostradados()

    verm = Vermes('Annita', 22.79, 'Vermelho')
    verm.set_classificacaoremedio()
    verm.set_tarja()
    verm.mostradados()
