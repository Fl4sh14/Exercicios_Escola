mochila = []
LIMITE = 5

while True:
    print('=== MOCHILA ZOMBIE ===')
    print('1 - Adicionar item')
    print('2 - Remover último item')
    print('3 - Mostrar item do topo')
    print('4 - Sair')

    opcao = int(input('Escolhe uma opção: '))

    if opcao == 1:
        if len(mochila) < LIMITE:
            item = input('Que item queres adicionar? ')
            mochila.append(item)
            print(f'{item} foi adicionado à mochila.')
        else:
            print('A mochila está cheia! (Limite de 5 itens)')

    elif opcao == 2:
        if len(mochila) > 0:
            removido = mochila.pop()
            print(f'{removido} foi removido da mochila.')
        else:
            print('A mochila está vazia! Não podes remover nada.')

    elif opcao == 3:
        if len(mochila) > 0:
            print(f'O item no topo é: {mochila[-1]}')
        else:
            print('A mochila está vazia! Não há item no topo.')

    elif opcao == 4:
        print('A sair do programa')
        break

    else:
        print('Opção inválida! Tenta novamente.')
