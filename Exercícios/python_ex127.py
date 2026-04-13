matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f'Digite o valor para posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

soma = 0

for i in range(4):
    soma += matriz[i][i]

print('Soma da diagonal principal:', soma)

if soma > 100:
    print('Risco: Alto')
else:
    print('Risco: Baixo')
