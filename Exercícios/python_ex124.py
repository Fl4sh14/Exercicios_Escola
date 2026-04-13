pontuacoes = []

for i in range(1, 5):
    partidas = []
    for j in range(1, 5):
        pontos = int(input(f'Equipa {i} - Partida {j}: '))
        partidas.append(pontos)
    pontuacoes.append(partidas)

equipa = int(input('Escolhe uma equipa (1-4): '))

partidas = pontuacoes[equipa - 1]
media = sum(partidas) / len(partidas)

print(f'Equipa {equipa}: {partidas}')
print(f'Média: {media:.1f} pontos')

if media >= 80:
    print('Desempenho estável e forte!')
elif media >= 60:
    print('Desempenho moderado.')
else:
    print('Desempenho instável.')
