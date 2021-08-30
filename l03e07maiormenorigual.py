'''
- Operadores de Comparação (relacionais):
Operador 	Descrição 	Exemplo 
< 	Menor que  	a < 10 
<= 	Menor ou igual 	b  <= 5 
> 	Maior que  	c  > 2 
>= 	Maior ou igual 	d  >= 8 
== 	Igual 	                 e == 5 
!= 	Diferente 	                  f  != 12

7. Construa o programa que leia dois valores quaisquer e
mostre o maior deles ou mostre a mensagem “Os valores são iguais.”
'''

# recebe os dois valores digitados
valor1=int(input('Digite o 1° valor: '))
valor2=int(input('Digite o 2° valor: '))
if(valor1>valor2):
    print('O maior valor é', valor1)
    print('A ordem decrescente é', valor1, ",",valor2)
elif(valor1==valor2):
    print('Os valores são iguais.', valor1,"=",valor2)
elif(valor1<valor2):
    print('O maior valor é', valor2)
    print('A ordem decrescente é', valor2, ",",valor1)


'''
Alterações:
a. Se eles forem diferentes, mostre os valores digitados na ordem decrescente.
b. Se eles forem iguais, mostre a mensagem e o valor digitado.
                 // Dicas abaixo:
a.	se ( valor1 > valor2 ) entao           // Verifica se o valor1 é maior que o valor2.
	   escreval ("Ordem decrescente: ", valor1, ", ", valor2)
   senao   . . .
b. escreva ("Os valores são iguais.", valor1)

---
else:                 # caso contrário
    # max(a, b) retorna o maior valor entre a e b
    print("O maior valor é", max(a, b))

'''
