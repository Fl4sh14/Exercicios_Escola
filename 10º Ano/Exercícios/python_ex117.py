def verificar_simbolos(mensagem):
    pilha = []
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for i, caractere in enumerate(mensagem):
        if caractere in '([{':
            pilha.append((caractere, i))
        elif caractere in ')]}':
            if not pilha:
                print(f'Invalida - Fecho "{caractere}" na posicao {i} sem abertura correspondente')
                return
            topo, posicao = pilha.pop()
            if pares[caractere] != topo:
                print(f'Invalida - Simbolo "{caractere}" na posicao {i} nao corresponde ao "{topo}" na posicao {posicao}')
                return

    if pilha:
        topo, posicao = pilha.pop()
        print(f'Invalida - Simbolo "{topo}" na posicao {posicao} nao foi fechado')
    else:
        print('Valida')


mensagem = input('Mensagem: ')
while mensagem != 'sair':
    verificar_simbolos(mensagem)
    mensagem = input('Mensagem: ')
    