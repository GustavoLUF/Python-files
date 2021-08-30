#Gustavo Lopes Urio Fonsêca / RA: 22007103
#Crie um programa para que o usuário digite um número e que de como resposta se o número é primo ou não.

n = int(input('Digite o número ao qual você questiona se é primo: '))
total = 0
for z in range(1, n + 1):
    if n % z == 0:
        total += 1
if total == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))