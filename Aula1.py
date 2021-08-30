print('Vamos calcular uma equação de segundo grau.')
a = int(input('Digite o valor de a: '))

if a == 0:
    print('Não é possivel dividir por 0.')

else:
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))

    print('Agora vamos tirar o delta dessa operação.')
    D = (b**2) - (4*a*c)
    x1 = (-b + (D**0.5)) / (2*a)
    x2 = (-b - (D**0.5)) / (2*a)
    if D > 0:
        print('O delta é possitivo, duas raizes na equação.')
        print(f'As raizes são:\nx1 = {x1:.4f} e x2 = {x2:.4f}')

    elif D == 0:
        print('Delta igual a zero, raiz única.')
        print(x1)

    else:
        print('Delta negativo, sem raizes nos reais.')