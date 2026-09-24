a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

def multiplicar(a, b, c):
    resultado = a * b * c
    print(f'O resultado da multiplicação entre {a}, {b} e {c} é: {resultado}')
multiplicar(a, b, c)