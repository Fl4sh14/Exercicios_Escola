import csv

produtos = [
    ['Mochila', 15.99, 10],
    ['Caderno', 2.50, 50],
    ['Caneta', 0.99, 100],
    ['Régua', 1.20, 30],
    ['Borracha', 0.50, 75]
]

with open('produtos.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerow(['Nome', 'Preco', 'Quantidade'])
    escritor.writerows(produtos)

with open('produtos.csv', 'r', encoding='utf-8') as f:
    leitor = csv.reader(f)
    next(leitor)
    for linha in leitor:
        print(f'Nome: {linha[0]} | Preço: {linha[1]} euros | Qty: {linha[2]}')
