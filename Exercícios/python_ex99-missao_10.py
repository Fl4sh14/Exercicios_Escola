import random

jogadores = []  
pontuacoes = {}  


def jogar():
    if len(jogadores) == 0:
        print("\n Não há jogadores registados. Adiciona um jogador primeiro.")
        return

    print("\n Jogadores registados:")
    for i in range(len(jogadores)):
        print(f"{i + 1} - {jogadores[i]}")

    escolha = int(input("Escolhe o número do jogador: ")) - 1

    if escolha < 0 or escolha >= len(jogadores):
        print(" Jogador inválido!")
        return

    nome = jogadores[escolha]

    numero_secreto = random.randint(1, 10)
    tentativas = 0

    print("\n ADIVINHA O NÚMERO (1 a 10)")

    while True:
        palpite = int(input("Adivinha o número: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f" Acertaste! O número era {numero_secreto}.")
            print(f" Tentativas: {tentativas}")

            pontuacoes[nome] = tentativas
            break
        elif palpite < numero_secreto:
            print(" Muito baixo!")
        else:
            print(" Muito alto!")


def inserir_jogador():
    nome = input("\nNome do jogador: ")
    jogadores.append(nome)
    print(" Jogador adicionado!")


def alterar_jogador():
    if len(jogadores) == 0:
        print("\n Não há jogadores para alterar.")
        return

    print("\n Jogadores:")
    for i in range(len(jogadores)):
        print(f"{i + 1} - {jogadores[i]}")

    escolha = int(input("Qual jogador queres alterar? ")) - 1

    if escolha < 0 or escolha >= len(jogadores):
        print(" Jogador inválido!")
        return

    novo_nome = input("Novo nome: ")

    nome_antigo = jogadores[escolha]
    jogadores[escolha] = novo_nome

    if nome_antigo in pontuacoes:
        pontuacoes[novo_nome] = pontuacoes[nome_antigo]
        del pontuacoes[nome_antigo]

    print(" Jogador alterado!")


def remover_jogador():
    if len(jogadores) == 0:
        print("\n Não há jogadores para remover.")
        return

    print("\n Jogadores:")
    for i in range(len(jogadores)):
        print(f"{i + 1} - {jogadores[i]}")

    escolha = int(input("Qual jogador queres remover? ")) - 1

    if escolha < 0 or escolha >= len(jogadores):
        print(" Jogador inválido!")
        return

    nome = jogadores.pop(escolha)

    if nome in pontuacoes:
        del pontuacoes[nome]

    print(" Jogador removido!")


def mostrar_pontuacoes():
    if len(pontuacoes) == 0:
        print("\n Ainda não há pontuações.")
        return

    print("\n PONTUAÇÕES (menos tentativas é melhor):")
    for nome, tentativas in pontuacoes.items():
        print(f"{nome} - {tentativas} tentativas")


while True:
    print("\n==============================")
    print(" JOGO: ADIVINHA O NÚMERO")
    print("==============================")
    print("1 - Jogar")
    print("2 - Inserir jogador")
    print("3 - Alterar jogador")
    print("4 - Remover jogador")
    print("5 - Ver pontuações")
    print("0 - Sair")

    opcao = input("Escolhe uma opção: ")

    if opcao == "1":
        jogar()
    elif opcao == "2":
        inserir_jogador()
    elif opcao == "3":
        alterar_jogador()
    elif opcao == "4":
        remover_jogador()
    elif opcao == "5":
        mostrar_pontuacoes()
    elif opcao == "0":
        print("\n A sair do jogo...")
        break
    else:
        print("\n Opção inválida!")

# Eu escolhi uma lista para guardar os jogadores porque é fácil adicionar, remover e alterar nomes.
# Eu escolhi um dicionário para guardar as pontuações porque assim consigo associar cada jogador ao seu número de tentativas.

# Os nomes dos jogadores ficam guardados numa lista chamada jogadores.
# As pontuações ficam guardadas num dicionário chamado pontuacoes, onde a chave é o nome do jogador e o valor é o número de tentativas.

# Para inserir um jogador eu uso append() para adicionar o nome à lista.
# Para alterar um jogador eu troco o nome diretamente na posição escolhida da lista.
# Para remover um jogador eu uso pop() e também apago a pontuação desse jogador no dicionário.
# Quando o jogador joga, o programa guarda automaticamente a pontuação no dicionário.
