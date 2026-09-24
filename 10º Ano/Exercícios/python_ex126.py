linhas = int(input('Número de linhas: '))
colunas = int(input('Número de colunas: '))

imagem = []

for i in range(linhas):
    linha = list(map(int, input(f'Valores da linha {i+1} separados por espaço: ').split()))
    imagem.append(linha)

transposta = []

for j in range(colunas):
    nova_linha = []
    for i in range(linhas):
        nova_linha.append(imagem[i][j])
    transposta.append(nova_linha)

print('Imagem original:')
for linha in imagem:
    print(linha)

print('\nImagem transposta:')
for linha in transposta:
    print(linha)
