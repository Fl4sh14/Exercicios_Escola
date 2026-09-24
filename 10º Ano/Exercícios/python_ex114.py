perfil = {
    'nome_utilizador': input('Nome de utilizador: '),
    'seguidores': int(input('Número de seguidores: ')),
    'publicacoes': int(input('Número de publicações: '))
}

print('--- PERFIL ---')
print(f'Utilizador: {perfil['nome_utilizador']}')
print(f'Seguidores: {perfil['seguidores']}')
print(f'Publicações: {perfil['publicacoes']}')

atualizar = input('Queres atualizar o número de seguidores? [s/n]: ')

if atualizar.lower() == 's':
    novos_seguidores = int(input('Novo número de seguidores: '))
    perfil["seguidores"] = novos_seguidores
    print("Seguidores atualizados com sucesso!")

if perfil['publicacoes'] > 0:
    engagement = perfil['seguidores'] / perfil['publicacoes']
else:
    engagement = 0

print(f'Taxa de engagement: {engagement:.2f}')

if perfil['seguidores'] < 10000:
    print('Classificação: Microinfluencer')
else:
    print('Classificação: Influencer')
