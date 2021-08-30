def menu():
    l_opcoes = ['c', 'r', 'u', 'd', 'e']
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')
    while True:
        opcao = input('Opção: ').lower()
        if opcao not in l_opcoes:
            print('Opção Inválida, tente novamente.')
        else:
            break
    return opcao

def create():
    nome = input('Nome: ')
    lista.append(nome)

def read():
    if lista != []:
        #ct = 0
        for indice, v in enumerate(lista):
            print(indice, '-', v)
            #print(ct, ' - ', v)
            #ct += 1

def update():
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

def delete():
    v = input('Qual nome: ')
    lista.remove(v)

if __name__ == "__main__":
    lista = []
    while True:
        op = menu()
        if op == 'c':
            create()

        elif op == 'r':
            read()

        elif op == 'u':
            update()

        elif op == 'd':
            delete()

        else:
            break