somaidade = 0
mediadeidade = 0
nomedohmaisvelho = 0
mulheres20anos = 0
maioridadehomem = 0
for c in range(1, 5):
    print('----{}ª PESSOA----'.format(c))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo == 'Masculino':
        maioridadehomem = idade
        nomedohmaisvelho = nome
    if sexo == 'Masculino' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedohmaisvelho = nome
    if sexo == 'Feminino' and idade < 20:
        mulheres20anos += 1

mediadeidade = somaidade / 4
print()
print('A média de idade é {}. O homem mais velho tem {} anos e se chama {}. Ao todo temos {} mulheres abaixo dos 20 anos de idade'.format(mediadeidade,maioridadehomem,nomedohmaisvelho,mulheres20anos))