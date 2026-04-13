radar = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

while True:
    linha = int(input('Linha (0-4): '))
    coluna = int(input('Coluna (0-4): '))

    if radar[linha][coluna] == 1:
        print(f'Sinal detetado nas coordenadas [{linha}][{coluna}]')
        break
    else:
        print('Nenhum sinal encontrado. Continuar busca')
