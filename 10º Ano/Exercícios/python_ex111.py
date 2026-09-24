print('=== Perfil de Streamer ===')

nome_canal = input('Nome do canal: ')
idade = int(input('Idade: '))
seguidores = int(input('Número de seguidores: '))
jogo_favorito = input('Jogo favorito: ')

views1 = int(input('Visualizações da stream 1: '))
views2 = int(input('Visualizações da stream 2: '))
views3 = int(input('Visualizações da stream 3: '))

media_views = (views1 + views2 + views3) / 3

print('=== Perfil Completo ===')
print(f'Nome do canal: {nome_canal}')
print(f'Idade: {idade}')
print(f'Seguidores: {seguidores}')
print(f'Jogo favorito: {jogo_favorito}')
print(f'Visualizações da stream 1: {views1}')
print(f'Visualizações da stream 2: {views2}')
print(f'Visualizações da stream 3: {views3}')
print(f'Média de visualizações: {media_views:.2f}')
