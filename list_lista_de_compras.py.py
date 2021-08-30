#O programa consiste em uma lista de compras de um mercado, onde o usuário pode ver os produtos, adicionar,remover e ver itens de seu carrinho.
#O Usuario começa o programa adicionando o seu telefone para contato, e ao longo do programa, ele tem a opção de adicionar o seu endereço para entrega e um outro telefone.
#Ao final, para finalizar sua compra, ele seleciona sua forma de pagamento e finalizamos o seu pedido, ligando para o seu número principal caso algo aconteça.

from time import sleep                      

if __name__ == '__main__':                  
    
    lista = {                               
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

    carrinho = []                         

    endereco = []

    telefone = []

    print('Bem vindo ao Menu de Compras do nosso Supermercado.')
    sleep(1)
    telefone1 = int(input('Digite um número de celular/telefone para iniciarmos as suas compras: '))
    telefone.append(telefone1)
    print('Selecione abaixo o que deseja realizar: ')
    opção = 0
    while opção != 7:                                   
        print('''        [ 1 ] Ver lista de Produtos.
        [ 2 ] Adicionar item no carrinho.
        [ 3 ] Remover item do carrinho.
        [ 4 ] Olhar carrinho.
        [ 5 ] Retirar os produtos no mercado.
        [ 6 ] Serviço de entrega.
        [ 7 ] Finalizar a compra.''')
        opção = int(input('>>>>Qual é sua opção? '))   
        print()
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
            str = input('Qual item deseja adicionar? ')
            carrinho.append(str)

        elif opção == 3:                                                   
            str = input('Digite o nome do produto que quer retirar: ')      
            carrinho.remove(str)

        elif opção == 4:
            a = ' '                             
            for item in carrinho:               
                a += item + ', '    
            print(a)

        elif opção == 5:
            print('Muito bem, para a retirada do(s) produto(s), precisamos primeiro saber a sua idade.')
            idade = int(input('Idade: '))
            if idade < 17:
                print('Só pode haver a retirada do produto com a presença de um maior de idade')
            elif idade <= 55:
                print('Você tem acesso livre para a retirada do produto')
            else:
                print('Para preservamos pela sua saúde e segurança, aconselhamos o serviço de entrega do nosso mercado.\nPara acessar o sistema de entrega, escolha a opção 7 em nosso menu.')
            print('O pagamento será feito na hora da retirada')

        elif opção == 6:
            print('Você escolheu a opção de Serviço de Entrega, por favor, nos informe as seguintes informações.')
            endereço = input('Seu endereço: ')
            endereco.append(endereço)
            telefone2 = int(input('Telefone secundário: '))
            telefone.append(telefone2)
            sleep(1)
            print(f'Estes são os seus dados: {endereco} e {telefone}')
            count = 0.0
            for prod_carrinho in carrinho:
                count += lista[prod_carrinho]
            sleep(2.5)
            print(''f'Valor total: {count:.2f}')
            print('Selecione finalizar compra para efetuar o pagamento.')
            
        elif opção == 7:
            count = 0.0
            for prod_carrinho in carrinho:      
                count += lista[prod_carrinho]

            print(''f'Valor total: {count:.2f}')
            pagamento = input('Selecione uma forma de pagamento, nós aceitamos todos cartões, de 3x a 10x sem juros e em dinheiro à vista! ').strip().capitalize()
            v = 0                               
            if 'Dinheiro' in pagamento:
                print(''f'O valor total ficará em R${count:.2f} no dinheiro à vista.')
            if 'Cartão' in pagamento:
                d = input('Quer dividir o valor? ').strip().capitalize()
                if d == 'Não':
                    print(''f'O valor total ficará em R${count:.2f} no cartão sem parcelas.')
                if d == 'Sim':
                   v = int(input('Em quantas vezes? '))
                   tot = count / v
                if v == 3 or v == 4 or v == 5 or v == 6 or v == 7 or v == 8 or v == 9 or v == 10:
                    print(''f'O valor total ficará em R${tot:.2f} por {v} meses sem juros, de um total de R${count:.2f}')
                elif v == 1 or v == 2 or v == 11 or v == 12:
                    print('Divisão do valor inválida, tente novamente.')
                    break
                print()
            telefone_principal = telefone[0:1]
            print(f'Caso tenhamos algum problema, ligaremos no telefone: {telefone_principal}.')
            print('Finalizando...')
        else:
            print('Opção Inválida. Tente Novamente.')
        print('=-=' * 10)
        sleep(1)                             
    print('Fim do seu pedido! Volte Sempre! ')
    