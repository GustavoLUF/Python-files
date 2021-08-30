#Gustavo Lopes Urio Fonsêca / RA: 22007103
#Crie um programa que dê 5 números aleatorios e um sexto número que será a soma dos números pares dados, caso não haja número par, o sexto número será sorteado novamente.

from random import randint
from time import sleep

def sorteio(lista):
    print('Vamos iniciar o sorteio dos seus números!')
    for cont in range(0, 5):
        n = randint(1, 60)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('Aqui estão os seus números!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
        if soma == 0 or soma > 60:
            soma = randint(1, 60)
    print(f'Estes são os cinco primeiros números sorteados {lista}, o sexto número será: {soma}')

    res = int(input('O sexto número está repetido?\n[ 1 ] Sim\n[ 2 ] Não\nSua resposta: '))
    while True:
        if res == 1:
            outro = randint(1, 60)
            print(f'Então o seu sexto número será {outro}')
            break

        if res == 2:
            print('Okay então, ai estão os seus números.')
            break
    print('Fim do Programa... Obrigado!')

números = list()
sorteio(números)
somaPar(números)