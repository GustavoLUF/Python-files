#Primeiro Programa
def maximo():

    maior = 0

    if numero1 > numero2 and numero1 > numero3:
        maior = numero1
        print(f'O maior dentre todos é o número {maior}')
        return maior

    elif numero2 > numero1 and numero2 > numero3:
        maior = numero2
        print(f'O maior dentre todos é o número {maior}')
        return maior

    else:
        maior = numero3
        print(f'O maior dentre todos é o número {maior}')
        return maior

if __name__ == "__main__":
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um número: '))
    numero3 = int(input('Digite um número: '))
    maximo()
