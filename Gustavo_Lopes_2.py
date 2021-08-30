def mostravalor():
    valorrecebido = int(input('Digite o valor que quer encontrar na lista: '))
    
    if valorrecebido in lista:
        print(f'O valor {valorrecebido} foi encontrado e está na posição {lista.index(valorrecebido)}')

    else:
        print('Este valor não está na lista.')

def nummaiorque10():
    contador = 0
    for valor in lista:
        if valor > 10:
            contador += 1
        else:
            print('Não tem-se valor maior que 10 na lista.')
    maiorque10 = (contador / len(lista)) * 100
    print(f'{maiorque10}% dos números são/é maior que 10.')

def crescente():
    lista.sort()
    print('* Esta é a lista na ordem crescente: *')
    print(lista,'\n')

def decrescente():
    lista.sort(reverse=True)
    print('* Esta é a lista na ordem decrescente: *')
    print(lista,'\n')

def valor33():
    lista.insert(1, 33)
    print(lista)

def menu():
    while True:
        escolha = int(input('''                     MENU
        [ 1 ] - Mostrar a lista de forma crescente...
        [ 2 ] - Mostrar a lista de forma decrescente...
        [ 3 ] - Mostrar um valor específico da lista...
        [ 4 ] - Inserir o número 33 na primeira posição da lista...
        [ 5 ] - Números maiores que 10 na lista...
        [ ENTER ] para sair.
    Escolha: '''))

        if escolha == 1:
            crescente()

        elif escolha == 2:
            decrescente()

        elif escolha == 3:
            mostravalor()

        elif escolha == 4:
            valor33()

        elif escolha == 5:
            nummaiorque10()

        elif escolha == '':
            break

if __name__ == '__main__':
    lista = []
    cont = 0
    while True:
        lista.append(input('Digite os números que deseja adicionar em sua lista: '))
        print('Quando desejar sair, precione a tecla (ENTER)')
        cont += 1

        if '' in lista:
            break

        else:
            continue

    if '' in lista:
        lista.remove('')
    menu()