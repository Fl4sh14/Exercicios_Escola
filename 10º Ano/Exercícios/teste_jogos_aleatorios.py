import random
from Bibliotecas import jogos_aleatorios as ja

def separador():
    print('-=' * 20)

escolha = ''
separador()
while escolha != 'N':
    print('Escolha um jogo aleatório:')
    print('[1] - Sortear número de um dado')
    print('[2] - Escolher elemento aleatório de uma lista')
    print('[3] - Gerar senha aleatória')
    escolha = int(input('Digite o número do jogo que deseja jogar: '))

    if escolha == 1:
        faces = ja.numero_faces()
        resultado = random.randint(1, faces)
        print(f'O número sorteado no dado de {faces} faces foi: {resultado}')
    elif escolha == 2:
        elemento = ja.elemento_aleatorio()
        print(f'O elemento aleatório escolhido foi: {elemento}')
    elif escolha == 3:
        comprimento = int(input('Digite o comprimento da senha desejada: '))
        password = ja.gerar_password(comprimento)
        print(f'Senha gerada: {password}')
    else:
        print('Opção inválida!')
    separador()

    escolha = input('Quer jogar novamente? [S/N]: ').strip().upper()

    if escolha == 'N':
        print('Obrigado por jogar! Até a próxima.')
        separador()
        separador()
