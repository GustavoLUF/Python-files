'''  8. Analise o resultado de uma transação comercial. Verifique a situação final do
comerciante trabalhando com os valores lidos, ou seja, o preço de compra e o
preço de venda. Gere a tela de saída com uma das seguintes mensagens:
“Teve lucro.”, “Teve prejuízo.” ou “Os valores são iguais.”.

    9. Refaça o programa anterior. Se os valores forem diferentes, mostre também
o valor do lucro em reais ou o valor do prejuízo em reais.

Testes: compra = 1000 e venda = 1200. Resposta: Lucro = 200
Testes: compra = 1200 e venda = 1000. Resposta: Prejuízo = 200
- Sintaxe do if ... elif ... else:
if condicao1:                             # A indentação é obrigatória.
    print (“Mensagem 1”)           # Executa, se a condição1 for verdadeira
elif condicao2:
    print(“Mensagem 2”)            # Executa, se a condição2 for verdadeira
else
    print("Mensagem 3")            # Executa, se todos os testes anteriores forem falsos.
   print("A transação teve lucro de R$ {:.2f}" .format (lucro) )        
'''
# recebe os valores de compra e venda
compra=float(input('Qual foi o valor de compra dos produtos: '))
venda=float(input('Qual foi o valor de venda recebido: '))
if(compra<venda):
    print("O valor de compra foi de", compra, '\nO valor de venda foi de', venda,'\nVocê teve lucro de', venda-compra)
elif(compra==venda):
    print('O valor de compra foi de', compra,'\nO valor de venda foi de', venda,'\nOs valores de compra e venda são iguais')
elif(compra>venda):
    print("O valor de compra foi de", compra,"\nO valor de venda foi de", venda,'\nE você teve prejuízo de', compra-venda)



