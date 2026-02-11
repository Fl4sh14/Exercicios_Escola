matchmaking = []

jogador1 = {'nome': 'Gaspar'}
jogador2 = {'nome': 'Lukas'}
jogador3 = {'nome': 'Albani'}
jogador4 = {'nome': 'Marcelino'}

matchmaking.append(jogador1)
matchmaking.append(jogador2)
matchmaking.append(jogador3)

resposta = input('Digite [Ready] quando estiver pronto!: ').lower().strip()

while resposta != 'ready':
    resposta = input('Digite [Ready] quando estiver pronto!: ').lower().strip()
if resposta == 'ready':
    matchmaking.append(jogador4)
    print(matchmaking) 
    
