#Gustavo Lopes Urio Fonsêca /  RA: 22007103
#Crie um programa que leia número e tira sua média, apresentando somente duas casas decimais, caso haja, apresentando o maior número digitado e o comando de saída sendo o digito 0.

from time import sleep

n = 1
soma = 0
contador = 0
print('Adicione os números que gostaria de tirar a média, no fim, digite 0 para sair.')
while n != 0:
    sleep(0.5)
    n = int(input('Digite um número: '))

    soma += n
    contador += 1
    media = (soma) / contador
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if n == 0:
        print(f'A média entre todos números é {media:.2f}, o maior número digitado foi {maior}.')
        break

        