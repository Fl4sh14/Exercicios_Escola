loja = {
    'Teclado Mecânico': 79.99,
    'Rato Gaming': 49.99,
    'Headset': 59.99,
    'Monitor 144Hz': 199.99,
    'Comando': 39.99
}

carrinho = []

print('=== LOJA GAMING ONLINE ===')

print('Produtos disponíveis:')
for produto, preco in loja.items():
    print(f'- {produto}: {preco:.2f}€')

while True:
    escolha = input('Que produto queres adicionar? (ou [sair] para terminar): ')
    
    if escolha.lower() == 'sair':
        break
    
    if escolha in loja:
        carrinho.append(escolha)
        print('Produto adicionado ao carrinho!')
    else:
        print('Produto não existe!')

print('=== RESUMO DA COMPRA ===')

if len(carrinho) == 0:
    print('Não compraste nenhum produto.')
else:
    total = 0
    mais_caro = carrinho[0]
    
    for produto in carrinho:
        total += loja[produto]
        if loja[produto] > loja[mais_caro]:
            mais_caro = produto
    
    desconto = 0
    if total > 100:
        desconto = total * 0.10
        total -= desconto
    
    print('Produtos comprados:')
    for produto in carrinho:
        print(f'- {produto}')
    
    print(f'Número total de artigos: {len(carrinho)}')
    print(f'Produto mais caro comprado: {mais_caro} ({loja[mais_caro]:.2f}€)')
    
    if desconto > 0:
        print(f'Desconto aplicado: {desconto:.2f}€')
    
    print(f'Total a pagar: {total:.2f}€')
