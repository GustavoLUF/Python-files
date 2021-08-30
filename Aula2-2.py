from datetime import date

nome = input('Digite o seu nome: ')
dia_nasc = int(input('Qual Dia do seu nascimento? '))
mes_nasc = int(input('Qual Mês do seu nascimento? '))
ano_nasc = int(input('Qual Ano do seu nascimento? '))

data_atual = date.today()
dia = data_atual.day
mes = data_atual.month
ano = data_atual.year

if mes_nasc > mes:
    idade = ano - ano_nasc - 1
    print(f'{nome}, hoje ({dia}/{mes}/{ano}), você tem {idade} anos.')

elif mes_nasc == mes and dia_nasc > dia:
    print(f'{nome}, hoje ({dia}/{mes}/{ano}), você tem {idade} anos.')

else:
    idade = ano - ano_nasc
    print(f'{nome}, hoje ({dia}/{mes}/{ano}), você tem {idade} anos.')