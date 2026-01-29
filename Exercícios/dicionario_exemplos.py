produto = {
    'nome': 'Telemóvel Samsung',
    'preço': 299.99,
    'stock': 15,
    'categoria': 'Eletrónica'
}
# print(f'{produto['nome']}, {produto['preço']}, {produto['stock']}')

produto['stock'] -= 3
print(produto)
