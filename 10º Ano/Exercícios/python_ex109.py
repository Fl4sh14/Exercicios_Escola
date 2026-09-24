personagem1_nome = 'Guerreiro'
personagem1_forca = 90
personagem1_velocidade = 50
personagem1_inteligencia = 30

personagem2_nome = 'Ninja'
personagem2_forca = 60
personagem2_velocidade = 95
personagem2_inteligencia = 50

personagem3_nome = 'Mago'
personagem3_forca = 30
personagem3_velocidade = 40
personagem3_inteligencia = 100

print('=== Criador de Personagens ===')
print('Escolhe uma personagem:')
print('1 - Guerreiro')
print('2 - Ninja')
print('3 - Mago')

escolha = int(input('Digite o número da personagem: '))

print('\n=== Personagem Escolhida ===')

if escolha == 1:
    print(f'Nome: {personagem1_nome}')
    print(f'Força: {personagem1_forca}')
    print(f'Velocidade: {personagem1_velocidade}')
    print(f'Inteligência: {personagem1_inteligencia}')

elif escolha == 2:
    print(f'Nome: {personagem2_nome}')
    print(f'Força: {personagem2_forca}')
    print(f'Velocidade: {personagem2_velocidade}')
    print(f'Inteligência: {personagem2_inteligencia}')

elif escolha == 3:
    print(f'Nome: {personagem3_nome}')
    print(f'Força: {personagem3_forca}')
    print(f'Velocidade: {personagem3_velocidade}')
    print(f'Inteligência: {personagem3_inteligencia}')

else:
    print('Opção inválida! Escolhe 1, 2 ou 3.')
