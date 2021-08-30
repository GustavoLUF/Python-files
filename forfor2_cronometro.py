#Gustavo Lopes Urio Fonsêca / RA: 22007103
#Crie um programa usando For encadeado que sirva como um cronometro até o minuto 5

from time import sleep
ini = int(input('Você gostaria de iniciar o cronometro de 5 minutos?\n[ 1 ] Sim\n[ 2 ] Não'))

for m in range(5):
    for s in range(60):
        sleep(1)
        print(m,'Minutos', s,'Segundos')