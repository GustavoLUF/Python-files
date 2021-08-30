def update():
    opcoesup = ['p', 'n', 's']
    print('[p] - Atualizar usando uma posição e o novo nome.')
    print('[n] - Atualizar usando o nome na lista e o novo nome.')
    print('[s] - Sair.')
    opcaoup = input('Opção: ').lower()
    if opcaoup == 'p':
        try:
            p = int(input('Qual posição: '))
            novo_nome = input('Novo nome: ')
            lista[p]
    if lista != []:
        read()
        p = int(input('Qual posição: '))
        novo_nome = input('Novo nome: ')
        lista.pop(p)
        lista.insert(p, novo_nome)
        try:
            lista[p] = novo_nome

        except IndexError as e:
            print('Erro IndexError: ', e)

        except Exception as e:
            print('Erro Exception: ', e)
    
    else:
        print('Lista Vazia.')