musicas = []
duracao = []
duracao_playlist = 0

for i in range(1, 6):
    nomes_musicas = str(input('Qual é o nome da música?: '))
    duracao_musica = float(input('Qual é a duração da música?: '))
    musicas.append(nomes_musicas)
    duracao.append(duracao_musica)
    duracao_playlist += duracao_musica


duracao_playlist = sum(duracao)
duracao_media = duracao_playlist / len(duracao)

indice_mais_longa = duracao.index(max(duracao))
indice_mais_curta = duracao.index(min(duracao))

print('-=' * 20)
print('--- Resultados ---')
print(f'Duração total da playlist: {duracao_playlist:.2f} minutos')
print(f'Música mais longa: {musicas[indice_mais_longa]} ({duracao[indice_mais_longa]} min)')
print(f'Música mais curta: {musicas[indice_mais_curta]} ({duracao[indice_mais_curta]} min)')
print(f'Duração média: {duracao_media:.2f} minutos')

if duracao_playlist > 15.00:
    print('-=' * 20)
    print('A playlist tem mais de 15 minutos!')
