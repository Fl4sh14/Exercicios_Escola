def adicionar_sala(estacao, nome_sala):
	if nome_sala in estacao:
		print(f"A sala '{nome_sala}' já existe.")
		return False
	estacao[nome_sala] = []
	print(f"Sala '{nome_sala}' criada com sucesso.")
	return True


def adicionar_sala(estacao, nome_sala):
    if nome_sala in estacao:
        print(f'A sala "{nome_sala}" já existe.')
        return False
    estacao[nome_sala] = []
    print(f'Sala "{nome_sala}" criada com sucesso.')
    return True


def adicionar_equipamento(estacao, nome_sala, objeto):
    if nome_sala not in estacao:
        print(f'A sala "{nome_sala}" não existe. Crie-a primeiro.')
        return False
    estacao[nome_sala].append(objeto)
    print(f'Equipamento "{objeto}" adicionado à sala "{nome_sala}".')
    return True


def listar_estacao(estacao):
    if not estacao:
        print('A estação está vazia. Ainda não existem salas.')
        return
    print('\nEstado atual da Estação Lunar:')
    for sala, equipamentos in estacao.items():
        print(f'- {sala}:')
        if equipamentos:
            for idx, eq in enumerate(equipamentos, start=1):
                print(f'  {idx}. {eq}')
        else:
            print('  (vazia)')
    print('')


estacao = {}
while True:
    print('ARQUITETO DA ESTAÇÃO ESPACIAL')
    print('Escolha uma opção:')
    print('[1] Construir nova Sala')
    print('[2] Adicionar Equipamento')
    print('[3] Listar toda a Estação')
    print('[4] Sair')
    escolha = input('Opção: ').strip()

    if escolha == '1':
        nome = input('Nome da nova sala: ').strip()
        if nome:
            adicionar_sala(estacao, nome)
        else:
            print('Nome inválido.')


    elif escolha == '2':
        nome = input('Sala onde adicionar o equipamento: ').strip()
        if not nome:
            print('Nome de sala inválido.')
            continue
        objeto = input('Nome do equipamento: ').strip()
        if not objeto:
            print('Nome de equipamento inválido.')
            continue
        adicionar_equipamento(estacao, nome, objeto)


    elif escolha == '3':
        listar_estacao(estacao)


    elif escolha == '4':
        print('A sair. Até breve, Arquiteto!')
        break


    else:
        print('Opção inválida. Tente novamente.')
