
# ** Parte 1

# # jogadores que acabaram de entrar na sala
# jogadores = ['DarkKnight_99', 'Shadow_Player', 'ProGamer_2026']

# with open('equipa.txt', 'w') as f:
#     for player in jogadores:
#         # escreve o nome e salta para a linha seguinte
#         f.write(player + '\n')

# print('Equipa guardada com sucesso!')

# ** Parte 2

# # a lista já vem preparada com as mudanças de linha (\n)
# vencedores = ['MVP_Tiago\n', 'SkillMaster_Ana\n', 'NoobSlayer_PT\n']
# with open('equipa.txt', 'w') as f:
#     # grava a lista completa num único passo
#     f.writelines(vencedores)

# ** Parte 3

# # útil para ler textos curtos ou ficheiros que queremos processar inteiros 
# with open('equipa.txt', 'r') as f:
#     conteudo = f.read()
#     print('--- BRIEFING DA MISSÃO ---')
#     print(conteudo)

# ** Parte 4

# # abrimos o ficheiro em modo de leitura ('r')
# with open('equipa.txt', 'r') as f:
#     # lemos a primeira linha
#     jogador1 = f.readline()
#     # lemos a segunda linha
#     jogador2 = f.readline()
#     # lemos a terceira linha
#     jogador3 = f.readline()

#     # mostramos os resultados (usamos .strip() para remover o \n)
#     print('O capitão de equipa é:', jogador1.strip())
#     print('O segundo jogador da equipa é:', jogador2.strip())
#     print('O terceiro jogador da equipa é:', jogador3.strip())

# ** Parte 5

# with open('equipa.txt', 'r') as f:
#     objetivos = f.readlines()

#     # agora podemos escolher qual mostrar pelo índice
#     print(f'O teu primeiro jogador é: {objetivos[0].strip()}')
#     print(f'Tens um total de {len(objetivos)} jogadores em espera.')
