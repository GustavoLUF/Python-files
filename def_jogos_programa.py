'''Este é um programa que emula jogos clássicos de lógica, incluindo pedra,papel e tesoura, par ou ímpar e até uma adivinhação com números de 0 a 10'''
import random
from time import sleep
from random import choice
from time import sleep
def main():
    while True:
        lin()
        print('\033[34;1m         BEM-VINDO!\033[m')
        lin()
        sleep(1)
        print()
        ast()
        print('\033[32m *Este é o emulador de jogos!*\033[m')
        ast()
        print()
        sleep(1)
        equal()
        print('\033[32m~~~~~~~~~~~~~MENU~~~~~~~~~~~~~\033[m')
        sleep(0.3)
        equal()
        p = '''\033[31;1m       [1] PAR OU ÍMPAR\033[m'''
        q = '''\033[31;1m       [2] PEDRA, PAPEL E TESOURA\033[m'''
        r = '''\033[31;1m       [3] ADIVINHAÇÃO\033[m'''

        s = '''\033[31;1m       [4] Sair\033[m'''

        for c in range(1):
            print(p)
            sleep(0.5)
        for c in range(1):
            print(q)
            sleep(0.5)
        for c in range(1):
            print(r)
            sleep(0.5)
        for c in range(1):
            print(s)
            sleep(0.5)
        print()
        esc = input('\033[32mFaça sua escolha:\033[m ')
        if esc == '1':
            print()
            parouimpar()

        elif esc == '2':
            print()
            pedrapapeltesoura()

        elif esc == '3':
            print()
            palpite()
        elif esc == '4':
            print('\033[31;1;4mVolte sempre!\033[m \033[31;1m:)\033[m')
            break
        else:
            print('\033[31mERROR. Tente novamente.\033[m')

def ast():
    print('\033[35;1m*\033[m'*30)

def equal():
    print('\033[35;1m=\033[m'*30)

def lin():
    print('\033[35;1m-\033[m'*30)

def parouimpar():
    print('\033[34m=' * 20, '\033[1;4;35mPAR OU ÍMPAR\033[m', '\033[34m=' * 20)
    cont = 0
    while True:
        answer = input('\033[32mPronto para jogar?! ').strip().lower()
        if answer == 'n' or answer == 'não':
            print('Ah...Okay. Tchau!')
            break
        print('Que bom! ', end='')
        sleep(0.4)
        print(
            'Pois bem, esolha seu número, e se quer ímpar ou par, e eu escolherei o meu ao mesmo tempo! Simbora!\033[m')
        print()
        pi = input('\033[1;31mPAR\033[m \033[32mou\033[m \033[1;31mÍMPAR?\033[m ').strip().upper()
        if pi == 'PAR':
            print('\033[32mTudo bem! Fico com \033[4;31mímpar\033[m \033[32mentão\033[m.')
            print()
            jogador = int(input('\033[32mSeu número: '))
            print('\033[32mBeleza!! Vamos lá, minha vez...')
            sleep(1)
            computador = random.choice(range(1, 101))
            print('Ok, escolhi \033[1;33m{}\033[m!'.format(computador))
            cej = jogador + computador
            resultado = str(cej)[-1]
            if resultado in '0' or resultado in '2' or resultado in '4' or resultado in '6' or resultado in '8':
                print('\033[32mVocê venceu!')
                print('Vamos novamente!')
                cont += 1
                print()
            else:
                print('\033[32mVocê perdeu!')
                break
        elif pi == 'ÍMPAR' or pi == 'IMPAR':
            print('\033[32mOk. Sou \033[4;31mpar\033[m \033[32mentão!\033[m')
            print()
            jogador = int(input('\033[32mSeu número: '))
            print('\033[32mBeleza!! Vamos lá, minha vez...')
            sleep(1)
            computador = random.choice(range(1, 101))
            print('Ok, escolhi \033[1;33m{}\033[m!'.format(computador))
            cej = jogador + computador
            resultado = str(cej)[-1]
            if resultado in '1' or resultado in '3' or resultado in '5' or resultado in '7' or resultado in '9':
                print('\033[32mVocê venceu!')
                print('Vamos novamente!')
                cont += 1
                print()
            else:
                print('\033[32mVocê perdeu!')
                break
    print('\033[32mVocê venceu {} rodadas consecutivas!\033[m'.format(cont))

def pedrapapeltesoura():
    x = input('Vamos uma partidinha de Pedra, Papel e Tesoura? ').strip().capitalize()
    if x == 'Sim':
        print('Então vamos lá!!! Voce primeiro! Prometo não roubar!')
    else:
        print('Okay então... ')
        exit()
    sleep(2)
    print()
    escolhadohumano = input('Escolha entre Pedra Papel ou Tesoura: ').capitalize().strip()
    lista = ['Papel', 'Pedra', 'Tesoura']
    EXZKYH = random.choice(lista)
    print('Hm...Então lá vai. Minha vez.')
    sleep(1)
    print('HA!')
    sleep(0.5)
    print('EU ESCOLHO: {}'.format(EXZKYH))
    sleep(1)
    if 'Papel' == escolhadohumano and 'Tesoura' == EXZKYH:
        print('EU GANHEI MUAHAHAHHAH!')
    elif 'Papel' == escolhadohumano and 'Pedra' == EXZKYH:
        print('Você venceu...')
    elif 'Papel' == escolhadohumano and 'Papel' == EXZKYH:
        print('HAHAH, não valeu! Vamos de novo.')
        exit()
    elif 'Pedra' == escolhadohumano and 'Tesoura' == EXZKYH:
        print('Você venceu...')
    elif 'Pedra' == escolhadohumano and 'Papel' == EXZKYH:
        print('EU GANHEI MUAHAHAHHAH!')
    elif 'Pedra' == escolhadohumano and 'Pedra' == EXZKYH:
        print('HAHAH, não valeu! Vamos de novo.')
        exit()
    elif 'Tesoura' == escolhadohumano and 'Pedra' == EXZKYH:
        print('EU GANHEI MUAHAHAHHAH!')
    elif 'Tesoura' == escolhadohumano and 'Papel' == EXZKYH:
        print('Você vencêu...')
    elif 'Tesoura' == escolhadohumano and 'Tesoura' == EXZKYH:
        print('HAHAH, não valeu! Vamos de novo.')
        exit()
    else:
        print('ERROR_#404#')

def palpite():
    tentativas = 0
    print('\033[32mVou escolher um número 0 a 10 aleatoriamente...\033[m')
    sleep(1)
    palpit = int(input('\033[32mQual seu palpite? '))
    print('Então vamos lá...')
    z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = choice(z)
    sleep(0.5)
    while palpit != x:
        palpite = int(input('Você \033[31mnão\033[m \033[32macertou...tente novamente: '))
        tentativas += 1
    if palpit == x:
        print('Você acertou! E foram necessárias \033[31m{}\033[m \033[32mtentativas.\033[m '.format(tentativas))

if __name__ == '__main__':
    main()
