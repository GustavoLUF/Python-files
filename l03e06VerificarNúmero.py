'''
- Operadores de Comparação (relacionais):
Operador 	Descrição 	Exemplo 
< 	Menor que  	a < 10 
<= 	Menor ou igual 	b  <= 5 
> 	Maior que  	c  > 2 
>= 	Maior ou igual 	d  >= 8 
== 	Igual 	                 e == 5 
!= 	Diferente 	                  f  != 12

6. Elabore o programa que leia um número qualquer e verifique
se ele é positivo, negativo ou nulo.

- Sintaxe do if ... elif ... else:
if condicao1:                             # A indentação é obrigatória.
    print (“Mensagem 1”)           # Executa, se a condição1 for verdadeira
elif condicao2:
    print(“Mensagem 2”)            # Executa, se a condição2 for verdadeira
else
    print("Mensagem 3")            # Executa, se todos os testes anteriores forem falsos.
'''
#espaço para iniciar programa
# Ler um valor, converte para int e atribui à variável numero
numero=int(input('Insira um valor desejado: '))
if(numero>0):
    print('O número inserido foi', numero)
    print('O dobro do número é', numero*2)
    print('O número inserido é positivo.')
elif(numero==0):
    print('O número inserido foi', numero)
    print('O número inserido é nulo.')
elif(numero<0):
    print('O número inserido foi', numero)
    print('O triplo deste número é', numero*3)
    print('O número inserido é negativo.')




'''
Alterações:
a. Além da mensagem, mostre também o número digitado pelo usuário.
b. Se o número for positivo, mostre a mensagem, a variável numero e o dobro;
   se negativo, mostre a mensagem, a variável numero e o triplo;
   Se nulo, mostre a mensagem, a variável numero.
   --- DICAS ABAIXO:

'''
