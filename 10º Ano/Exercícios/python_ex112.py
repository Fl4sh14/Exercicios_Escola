jogos = []
nome = input('Insere o nome de um jogo (ou [sair] para terminar): ').strip().lower()

for i in range(0,9):
    nome = input('Insere o nome de um jogo (ou [sair] para terminar): ').strip().lower()
    if nome == 'sair':
        break
    elif nome not in jogos:
        jogos.append(nome)
    else:
        print('Este jogo já está na lista!')

print('-=' * 20)
print('Lista de jogos:')
for i, jogo in enumerate(jogos, start=1):
    print(f'{i}. {jogo}')

print(f'Total de jogos inseridos: {len(jogos)}')

print('-=' * 20)
print('Lista ordenada alfabeticamente:')
for jogo in sorted(jogos):
    print('-> ', jogo)

remover = input('Qual jogo queres remover?: ')

if remover in jogos:
    jogos.remove(remover)
    print('Jogo removido com sucesso.')
else:
    print('Jogo não encontrado.')

print('Lista final atualizada:')
for i, jogo in enumerate(jogos, start=1):
    print(f'{i}. {jogo}')
