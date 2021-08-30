''' 11. Projete o programa que calcule as raízes de uma equação do 2° grau, levando em
consideração a análise da existência de raízes reais. Se o valor de delta for menor que
zero, não existem raízes nos reais; se delta for igual a zero, existem duas raízes iguais
e se delta for maior que zero, existem duas raízes diferentes.
Expressão: ax^2 + bx + c = 0
x = - b +-  raiz ( b^2 - 4 a c )                 delta = b^2 - 4 a c
                  2a
T este 1: a=0, b= 2 e c = 3.    Resposta: Não posso dividir por zero.
Teste 2: a=1, b= 2 e c = 3.    Resposta: Não existem raízes nos reais.
Teste 3: a = 1, b = 9 e c = 2. Resposta: x1 = - 0.22 ... e x2 = - 8.77 ...
Teste 4: a = 3, b = 9 e c = 2. Resposta: x1 = - 0,24 ... e x2 = - 2,76 ...
 '''
import sys
import math     # bliblioteca de funcões matemáticas para usar a função sqrt (raiz quadrada)
print('Para resolvermos uma equação de 2° grau, ax^2 + bx + c = 0, preciso de:')
a=int(input('Insira o valor de a: '))
b=int(input('Insira o valor de b: '))
c=int(input('Insira o valor de c: '))
if(a==0):
    print('Não posso dividir por zero.')
    sys.exit(0)
delta=b**2 - 4*a*c
if(delta>0):
    print('Essa função vai possuir duas raizes reais')
    print('x = -b +- delta**1/2 / 2*a')
    x1=((-b + math.sqrt(delta))/ (2*a))
    x2=((-b - math.sqrt(delta))/ (2*a))
    print('x1 = {:.2f}'.format(x1))
    print('x2 = {:.2f}'.format(x2))
elif(delta==0):
    print('Essa função vai possuir uma raíz real')
    x=((-b + math.sqrt(delta))/ (2*a))
    print('x= {:.2f}'.format(x))
elif(delta<0):
    print('Essa função não vai possuir raízes nos reais')