#Gustavo Lopes Urio Fonsêca /  RA: 22007103
#Crie um programa usando if, elif e else, em que o usuário responda se ele quer jogar ou não 'Jokenpô' e que ele responda qual opção quer, logo depois a maquina escolhe o dela, dando a mensagem final se o usuário ganhou ou perdeu.

import random
from time import sleep
x = input('Vamos uma partidinha de Jokenpô? ').strip().capitalize()

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
    print('Você veneu...')
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

