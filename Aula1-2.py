a = int(input('Comprimento da reta a: '))
b = int(input('Comprimento da reta b: '))
c = int(input('Comprimento da reta c: '))

if a < b + c and b < a + c and c < a + b:
    print('Os lados formam um triângulo.')
    if a == b and b == c:
        print('O triângulo é equilátero')
    
    elif a != b and b != c and c != a:
        print('O triângulo é escaleno')
    
    else:
        print('O triângulo é isósceles')

else:
    print('Os lados não formam um triângulo')