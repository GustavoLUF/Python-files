class Endereco(object):
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    def get_cidade(self):
        return self.cidade

    def get_estado(self):
        return self.estado


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def insere_endereco(self, cidade, estado):
        o_endereco = Endereco(cidade, estado)
        self.enderecos.append(o_endereco)
    
    def mostra_endereco(self):
        print("- Endereço do Cliente: ")
        for o_endereco in self.enderecos:
            print(o_endereco.get_cidade(), o_endereco.get_estado())
    
    def insere_endereco2(self, o_endereco):
        self.enderecos.append(o_endereco)
    
    def mostra_endereco2(self):
        print(f'- Endereços do Cliente {self.nome}')
        for o_endereco in self.enderecos:
            print(o_endereco.get_cidade(), o_endereco.get_estado())

    def mostra_endereco3(self):
        if self.enderecos == []:
            print("O Cliente não tem endereço cadastrado.")
        else:
            print(f"- Endereço do cliente {self.nome}")
            for o_endereco in self.enderecos:
                print(o_endereco.get_cidade(), o_endereco.get_estado())
    
    def remove_endereco(self, o_endereco):
        self.enderecos.remove(o_endereco)

    def remove_endereco2(self):
        cidade = input('Remover cidade: ')
        removeu = False
        for o_endereco in self.enderecos:
            self.remove_endereco(o_endereco)
            removeu = True
            break
        if removeu:
            print('Endereço removido.')
        else:
            print('Endereço não removido.')

if __name__ == "__main__":
    cliente1 = Cliente('Gustavo', 19)
    print('- Nome: ', cliente1.get_nome())
    print('Idade: ', cliente1.get_idade())
    cliente1.mostra_endereco3()
    cliente1.insere_endereco('Brasilia', 'DF')
    print('- Nome: ', cliente1.get_nome())
    cliente1.mostra_endereco()
    cliente2 = Cliente('Yan', 18)
    cliente2.insere_endereco('Taguatinga', 'DF')
    print('- Nome: ', cliente2.get_nome())
    cliente2.mostra_endereco()
    endereco = Endereco('Rio de Janeiro', 'RJ')
    cliente2.insere_endereco2(endereco)
    print('- Nome:: ', cliente2.get_nome())
    cliente2.mostra_endereco2()
    
    
    