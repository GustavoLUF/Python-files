
'''
- Operadores de Comparação (relacionais):
Operador 	Descrição 	Exemplo 
< 	Menor que  	a < 10 
<= 	Menor ou igual 	b  <= 5 
> 	Maior que  	c  > 2 
>= 	Maior ou igual 	d  >= 8 
== 	Igual 	                 e == 5 
!= 	Diferente 	                  f  != 12

8. Analise o resultado de uma transação comercial. Verifique a situação final
do comerciante trabalhando com os valores lidos, ou seja, o preço de compra
e o preço de venda. Gere a tela de saída com uma das seguintes mensagens:
“Teve lucro.”, “Teve prejuízo.” ou “Os valores são iguais.”.
- Sintaxe do if ... elif ... else:
if condicao1:                             # A indentação é obrigatória.
    print (“Mensagem 1”)           # Executa, se a condição1 for verdadeira
elif condicao2:
    print(“Mensagem 2”)            # Executa, se a condição2 for verdadeira
else
    print("Mensagem 3")            # Executa, se todos os testes anteriores forem falsos.
'''
# ler um valor, converte para float e atribui à variável numero
compra=float(input('Qual foi o valor de compra dos produtos: '))
venda=float(input('Qual foi o valor de venda recebido: '))
if(compra<venda):
    print("O valor de compra foi de", compra, '\nO valor de venda foi de', venda,'\nVocê teve lucro')
elif(compra==venda):
    print('O valor de compra foi de', compra,'\nO valor de venda foi de', venda,'\nOs valores de compra e venda são iguais.')
elif(compra>venda):
    print("O valor de compra foi de", compra,"\nO valor de venda foi de", venda,'\nE você teve prejuízo')



'''
Alterações:
a. Na tela de saída, mostre também o valor do preço de compra e do preço de venda.
'''
