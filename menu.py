from time import sleep
if __name__ == "__main__":
    lista = []
print('Bem vindo ao Menu de Compras do nosso Supermercado.\nSelecione abaixo o que deseja realizar: ')
opção = 0
while opção != 5:
    print('''    [ 1 ] Ver lista de Produtos.
    [ 2 ] Adicionar item no carrinho.
    [ 3 ] Remover item do carrinho.
    [ 4 ] Olhar carrinho.
    [ 5 ] Finalizar compra.''')
    opção = int(input('>>>>Qual é sua opção? '))
    if opção == 1:
        print('''Estes são os itens que nosso mercado possui:
        Arroz = R$19.99
        Feijão = R$6.99
        Sal refinado = 2.69
        Óleo de Soja = 3.89
        Leite Integral = 3.49
        Açucar Cristal = 10.99
        Café = 10.98
        Farinha de Trigo = 4.69
        Carne Alcatra = 28.61
        Ovo Branco = 14.99
        Macarrão Espaghetti = 6.99
        Biscoito Cream Cracker Pacote = 3.35
        Detergente Líquido = 1.59
        Desinfetante = 5.39
        Álcool Gel = 8.99
        Pão de Forma = 6.99
        Manteiga = 23.99
        Margarina = 4.79
        Queijo Mussarela  = 25.99
        Presunto = 10.99
        ''')
    elif opção == 2:
        str = lista.append(input('Qual item deseja adicionar? '))
    elif opção == 3:
        str = input('Digite o nome do produto que quer retirar: ')
        lista.remove(str)
    elif opção == 4:
        a = ' '
        for item in lista:
            a += item + ', '
        print(a)
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente Novamente.')
    print('=-=' * 10)
    sleep(1)
print('Fim do seu pedido! Volte Sempre! ')