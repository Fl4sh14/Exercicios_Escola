n1 = int(input('Escreva um nº para ser subtraído: '))
n2 = int(input('Escreva outro nº para ser subtraído: '))
if n1 > n2:
    print(f'A diferença de {n1} com {n2} é', (n1 - n2))
else:
    print(f'A diferença de {n2} com {n1} é', (n2 - n1))
