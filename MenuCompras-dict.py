
from time import sleep                      #Importar a função sleep para o programa

if __name__ == '__main__':                  #Abrir a função main para adicionar listas ao programa principal

    lista = {                               #Dict que possibilita adicionar valor ao item
        'Arroz': 19.99,
        'Feijão': 6.99,
        'Sal refinado': 2.69,
        'Óleo de Soja': 3.89,
        'Leite Integral': 3.49,
        'Açucar Cristal': 10.99,
        'Café': 10.98,
        'Farinha de Trigo': 4.69,
        'Carne Alcatra': 28.61,
        'Ovo Branco': 14.99,
        'Macarrão': 6.99,
        'Biscoito': 3.35,
        'Detergente': 1.59,
        'Desinfetante': 5.39,
        'Álcool Gel': 8.99,
        'Pão de Forma': 6.99,
        'Manteiga': 23.99,
        'Margarina': 4.79,
        'Queijo': 25.99,
        'Presunto': 10.99,
    }

    carrinho = []                           #Lista vazia aberta para adicionar itens

    print('Bem vindo ao Menu de Compras do nosso Supermercado.\nSelecione abaixo o que deseja realizar: ')
    opção = 0
    while opção != 5:                                   #
        print('''        [ 1 ] Ver lista de Produtos.
        [ 2 ] Adicionar item no carrinho.
        [ 3 ] Remover item do carrinho.
        [ 4 ] Olhar carrinho.
        [ 5 ] Finalizar compra.
        [ 6 ] Retirar o produto
        [ 7 ] Serviço de entrega''')
        opção = int(input('>>>>Qual é sua opção? '))   #Variável que ia salvar a opção que o usuária selecionar e ativar os ifs
        print()
        if opção == 1:                                 #Se o usuario digitar 1, irá printar a lista
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
        Macarrão = 6.99
        Biscoito = 3.35
        Detergente Líquido = 1.59
        Desinfetante = 5.39
        Álcool Gel = 8.99
        Pão de Forma = 6.99
        Manteiga = 23.99
        Margarina = 4.79
        Queijo = 25.99
        Presunto = 10.99
        ''')

        elif opção == 2:                               
            str = input('Qual item deseja adicionar? ')             #Variável que ira salvar a escolha do usuário
            carrinho.append(str)                                    #Adiciona a palavra escrita à lista carrinho

        elif opção == 3:                                                   
            str = input('Digite o nome do produto que quer retirar: ')      #Variável que será retirada da lista 'carrinho'
            carrinho.remove(str)                                            #Remove o item adicionado a lista

        elif opção == 4:
            a = ' '                             #Variável vazia, para se adicionar itens depois
            for item in carrinho:               #Comando for que irá listar cada item no carrinho
                a += item + ', '                #Adiciona uma virgula a cada item colocado na lista
            print(a)

        elif opção == 5:
            count = 0.0                         #Variável que irá receber os valores da lista dict
            for prod_carrinho in carrinho:      
                count += lista[prod_carrinho]   #Vai entregar o valor ou somar os valores de cada item adicionado no carrinho

            print(''f'Valor total: {count:.2f}')    #O valor total dos itens vai ser printado com apenas duas casas decimais após a virgula
            pagamento = input('Selecione uma forma de pagamento, nós aceitamos todos cartões, de 3x a 10x sem juros e em dinheiro à vista! ').strip().capitalize()
            v = 0                               
            if 'Dinheiro' in pagamento:
                print(''f'O valor total ficará em R${count:.2f} no dinheiro à vista.')          #Se o usuário digitar 'dinheiro', o valor total irá aparecer com 2 casas decimais após a virgula
            if 'Cartão' in pagamento:
                d = input('Quer dividir o valor? ').strip().capitalize()        #Variável que irá a reposta do usuário 'Sim' ou 'Não'
                if d == 'Não':
                    print(''f'O valor total ficará em R${count:.2f} no cartão sem parcelas.')       #Caso a resposta seja 'não' o valor total será printado
                if d == 'Sim':
                   v = int(input('Em quantas vezes? '))               #Variável que irá receber a quantia do parcelamento do cartão
                   tot = count / v
                if v == 3 or v == 4 or v == 5 or v == 6 or v == 7 or v == 8 or v == 9 or v == 10:
                    print(''f'O valor total ficará em R${tot:.2f} por {v} meses sem juros, de um total de R${count:.2f}')         #Após a variável 'v' possuir um valor, ela irá dividir o valor total dos itens e printar
                elif v == 1 or v == 2 or v == 11 or v == 12:
                    print('Divisão do valor inválida, tente novamente.')
                    break
                print()
            print('Finalizando...')
        elif opção == 6:
            print('Muito bem, para a retirada do(s) produto(s), precisamos primeiro saber a sua idade.')
            idade = int(input('Idade: '))
            if idade < 17:
                print('Só pode haver a retirada do produto com a presença de um maior de idade')
            elif idade <= 55:
                print('Você tem acesso livre para a retirada do produto')
            elif idade >= 56:
                print('Para preservamos pela sua saúde e segurança, aconselhamos o serviço de entrega do nosso mercado.\nPara acessar o sistema de entrega, escolha a opção 7 em nosso menu.')
        else:
            print('Opção Inválida. Tente Novamente.')
        print('=-=' * 10)
        sleep(1)                             #Função sleep a partir do import
    print('Fim do seu pedido! Volte Sempre! ')
    