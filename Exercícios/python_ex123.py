stock = []

for loja in range(3):
    linha = []
    for produto in range(3):
        quantidade = int(input(f'Quantidade do Produto {produto+1} na Loja {loja+1}: '))
        linha.append(quantidade)
    stock.append(linha)

print('=== Tabela de Stock: ===')

print(f'{'':10} {'Produto 1':10} {'Produto 2':10} {'Produto 3':10}')

for loja in range(3):
    print(f'{"Loja "+str(loja+1):<10}', end='')
    for produto in range(3):
        print(f'{stock[loja][produto]:>10}', end='')
    print()
