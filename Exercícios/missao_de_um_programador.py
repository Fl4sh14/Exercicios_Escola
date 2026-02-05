import random

def sep():
    print('-=' * 20)

# ============ MISSÃO 1 ============
Jogador1 = {
    'Nome': 'xX_Gamer67_Xx',
    'Nível': 0,
    'Energia': 50,
    'Ranking': 500
}

# ============ MISSÃO 2 ============
sep()
print(f'\033[1m Jogador 1 antes dos updates:\033[0m {Jogador1}')
Jogador1['Nível'] += 1
Jogador1['Energia'] = 100
print(f'\033[1m Jogador 1 depois dos updates:\033[0m {Jogador1}')
sep()

# ============ MISSÃO 3 ============
Jogador2 = {
    'Nome': 'Gustavinho_445',
    'Nível': 0,
    'Energia': 100,
    'Ranking': 146
}

Jogador3 = {
    'Nome': 'Marcelinoinhoinho',
    'Nível': 0,
    'Energia': 100,
    'Ranking': 250
}

Jogador4 = {
    'Nome': 'Albani',
    'Nível': 0,
    'Energia': 100,
    'Ranking': 500
}

Jogador5 = {
    'Nome': 'Travis_Scoot',
    'Nível': 0,
    'Energia': 100,
    'Ranking': 100
}

jogadores = []
jogadores.append(Jogador1)
jogadores.append(Jogador2)
jogadores.append(Jogador3)
jogadores.append(Jogador4)
jogadores.append(Jogador5)

soma = 0
for jogador in jogadores:
    soma += jogador['Ranking']
sep()

# ============ MISSÃO 4 ============

melhor_jogador = jogadores[0]
melhor_ranking = jogadores[0]['Ranking']

for jogador in jogadores:
    if jogador['Ranking'] > melhor_ranking:
        melhor_ranking = jogador['Ranking']
        melhor_jogador = jogador

print('\033[1m Jogador com o melhor ranking:\033[0m')
print(f'\033[1m Melhor Jogador:\033[0m {melhor_jogador['Nome']}  (\033[1m ranking\033[0m {melhor_jogador['Ranking']})')
print(f'\033[1m Nível:\033[0m {melhor_jogador['Nível']}  |  \033[1m Energia:\033[0m {melhor_jogador['Energia']} %')
sep()

quantidade = len(jogadores)
media = soma / quantidade

print(f'\033[1m Ranking médio da sala de espera:\033[0m {media:.2f}')
print(f' (total de {quantidade} jogadores)')
sep()

# ============ MISSÃO 5 ============

Jogador1['Pontos'] = 494
Jogador1['Número de Partidas'] = 30

Jogador2['Pontos'] = 654
Jogador2['Número de Partidas'] = 39

Jogador3['Pontos'] = 825
Jogador3['Número de Partidas'] = 57

Jogador4['Pontos'] = 105
Jogador4['Número de Partidas'] = 67

Jogador5['Pontos'] = 736
Jogador5['Número de Partidas'] = 96

maior_pontos = 0
jogador_mais_pontos = None

for jogador in jogadores:
    if jogador['Pontos'] > maior_pontos:
        maior_pontos = jogador['Pontos']
        jogador_mais_pontos = jogador

print(f'\033[1m Player com mais pontos\033[0m: {jogador_mais_pontos['Nome']} --> {maior_pontos} pontos')
sep()

# ============ MISSÃO 6 ============

fila_matchmaking = []
fila_matchmaking.append(Jogador2)
fila_matchmaking.append(Jogador3)
fila_matchmaking.append(Jogador1)
fila_matchmaking.append(Jogador4)
fila_matchmaking.append(Jogador5)

print('\033[1m Fila de espera\033[0m:')
for jogador in fila_matchmaking:
    print(f' - {jogador['Nome']}')

# primeiro a entrar é o primeiro a jogar
jogador_atual = fila_matchmaking.pop(0)
print(f'\n{jogador_atual['Nome']} saiu para jogar!')
sep()

# ============ MISSÃO 7 ============

acoes = []

acoes.append('andar')
acoes.append('saltar')
acoes.append('atacar')

print('\033[1m Ações realizadas\033[0m:')
for acao in acoes:
    print(f' - {acao}')

ultima_acao = acoes.pop()
print(f'\n\033[1m Ação desfeita\033[0m: {ultima_acao}')
sep()   

# ============ MISSÃO 8 ============

loja = []

loja.append({'Nome': 'Espada', 'Preço': 150})
loja.append({'Nome': 'Escudo', 'Preço': 100})
loja.append({'Nome': 'Poção', 'Preço': 50})
loja.append({'Nome': 'Armadura', 'Preço': 300})

print('\033[1m Loja do Jogo\033[0m:')
for item in loja:
    print(f' - {item['Nome']}: {item['Preço']} moedas')

item_mais_caro = loja[0]
for item in loja:
    if item['Preço'] > item_mais_caro['Preço']:
        item_mais_caro = item

print(f'\n\033[1m Item mais caro\033[0m: {item_mais_caro['Nome']} ({item_mais_caro['Preço']} moedas)')
sep()

# ============ MISSÃO 9 ============


jogadores = {
    "Ana": 0,
    "Bruno": 0,
    "Carlos": 0,
    "Diana": 0
}

print("=== TORNEIO FINAL ===\n")

for ronda in range(1, 4):
    print(f"--- Ronda {ronda} ---")
    
    for jogador in jogadores:
        pontos = random.randint(1, 10)
        jogadores[jogador] += pontos
        print(f"{jogador} ganhou {pontos} pontos")
    
    print()

print('=== CLASSIFICAÇÃO FINAL ===')
classificacao = []
jogadores_copia = jogadores.copy()

while jogadores_copia:
    melhor_nome = None
    melhor_pontos = -1
    for nome in jogadores_copia:
        if jogadores_copia[nome] > melhor_pontos:
            melhor_pontos = jogadores_copia[nome]
            melhor_nome = nome
    classificacao.append((melhor_nome, melhor_pontos))
    del jogadores_copia[melhor_nome]

posicao = 1
for item in classificacao:
    nome = item[0]
    pontos = item[1]
    print(f'{posicao}º - {nome}: {pontos} pontos')
    posicao += 1

vencedor = classificacao[0][0]
print(f"\n VENCEDOR: {vencedor}!")
