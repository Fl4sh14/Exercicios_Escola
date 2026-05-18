import csv

with open('stock.csv', newline='', encoding='utf-8') as f:
    produtos = list(csv.DictReader(f))

pesquisa = input('Nome do produto: ')
encontrado = False

for p in produtos:
    if p['Produto'].lower() == pesquisa.lower():
        nova_qty = input(f'Nova quantidade para {p['Produto']}: ')
        p['Quantidade'] = nova_qty
        encontrado = True
        break

if encontrado:
    with open('stock.csv', 'w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=['Produto', 'Preco', 'Quantidade'])
        escritor.writeheader()
        escritor.writerows(produtos)
    print('Stock atualizado com sucesso.')
else:
    print('Produto não encontrado.')
