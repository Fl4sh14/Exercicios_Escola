import random

def lançamento_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    print(f'Dado 1: {dado1}')
    print(f'Dado 2: {dado2}')
    print(f'Soma: {soma}')
    return soma

def resultado_jogo(soma):
    if soma > 7:
        print('Ganhou!')
        return True
    else:
        print('Perdeu!')
        return False
