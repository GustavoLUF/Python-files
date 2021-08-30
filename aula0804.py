from abc import ABC, abstractmethod
class Carro(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.preco_base = 100.00
    
    def get_nome(self):
        return self.nome
    
    def get_preco_base(self):
        return self.preco_base

    def get_diario(self):
        return self.get_diario

class Economico(Carro):
    def __init__(self, nome):
        super().__init__(nome)

    def retorna_preco_diaria(self):
        return self.get_preco_base() * 1.05


if __name__ == '__main__':
    o_eco = Economico('Uno')
    print(f'Nome: {o_eco.get_nome()}')
    print(f'Preço base: {o_eco.get_preco_base()}')
    print(f'Diário R$ {:.2f}' .format(o_eco.retorna_preco_diaria()))
    o_int = Intermediario('HB20')
    print(f'- O carro {o_int.get_nome()} com:')
    print(f'Preço básico: {o_int.get_preco_base()}')
    print(f'Diário R$ {:.2f}' .format(o_int.retorna_preco_diaria()))