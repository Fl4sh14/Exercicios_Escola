with open('identidade.txt', 'w') as f:
    f.write('Claudio\n')
    f.write('Perafita\n')

print('Ficheiro identidade.txt criado com sucesso!')

with open('identidade.txt', 'r') as f:
    conteudo = f.read()
    print(conteudo)

with open('identidade.txt', 'a', encoding='utf-8') as f:
    f.write('16' + '\n')

with open('identidade.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    print('\nConteúdo do ficheiro:')
    print(conteudo)
