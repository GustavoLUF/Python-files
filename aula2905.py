from random import randint
lista = []
for i in range(0, 5):
    n = randint(1, 5)
    lista.append(n)
tam_lista = len (lista)
print(lista)


somapar = 0
somaimpar = 0

for i in range(0, tam_lista, 2):
    somapar += lista[i]

for i in range(1, tam_lista, 2):
    somaimpar += lista[i]

print('A soma dos valores Pares na lista é igual a: ', somapar)
print('A soma dos valore Impares na lista é igual a: ', somaimpar)