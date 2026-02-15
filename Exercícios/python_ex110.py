# Dicionário Gamer
dicionario = {
    'GG': 'Good Game (bom jogo)',
    'AFK': 'Away From Keyboard (longe do teclado)',
    'Nerf': 'Quando algo é enfraquecido no jogo'
}

while True:
    print('\n=== Dicionário Gamer ===')
    print('1 - Adicionar novo termo')
    print('2 - Pesquisar termo')
    print('3 - Mostrar todo o dicionário')
    print('4 - Sair')

    opcao = int(input('Escolhe uma opção: '))

    if opcao == 1:
        termo = input('Escreve o termo: ').upper()
        significado = input('Escreve o significado: ')
        dicionario[termo] = significado
        print(f'Termo {termo} adicionado com sucesso!')

    elif opcao == 2:
        termo = input('Qual termo queres pesquisar? ').upper()

        if termo in dicionario:
            print(f'{termo} significa: {dicionario[termo]}')
        else:
            print('Esse termo não existe no dicionário!')

    elif opcao == 3:
        print('\n=== Todos os Termos ===')
        for termo, significado in dicionario.items():
            print(f'{termo} -> {significado}')

    elif opcao == 4:
        print('A sair do dicionário gamer...')
        break

    else:
        print('Opção inválida! Escolhe entre 1 e 4.')
