lista = [15, 6, 11, 8]
'''print(len(lista))

print(sum(lista))

print(max(lista))

print(min(lista))

pesquisa = int(input('Valor de pesquisa: '))
if pesquisa in lista:
    print('Valor encontrado.')
    posicao = lista.index(pesquisa)
    print('Posição do valor pesquisado: ', posicao)
else:
    print('Valor não encontrado.')

lista.sort()
print('Lista na ordem crescente: ', lista)

lista.insert(1, 29)
print(lista)

lista.sort(reverse=True)
print('Decrescente: ', lista)'''

count = 0
for v in lista:
    if v > 10:
        count += 1
porc = count / len(lista) * 100
print('Porcentagem dos maiores de 10: ', porc)