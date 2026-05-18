import easygui
import csv
import os
from datetime import datetime

import os

pasta_base = os.path.dirname(os.path.abspath(__file__))
pasta = os.path.join(pasta_base, 'torneio')

ficheiro_jogadores = os.path.join(pasta, 'jogadores.csv')
ficheiro_historico = os.path.join(pasta, 'historico.csv')

cabecalho_jogadores = ['nome', 'jogo_favorito', 'vitorias', 'derrotas']
cabecalho_historico = ['vencedor', 'perdedor', 'data']


def inicializar():
    os.makedirs(pasta, exist_ok=True)

    if not os.path.exists(ficheiro_jogadores):
        with open(ficheiro_jogadores, 'w', newline='', encoding='utf-8') as f:
            csv.DictWriter(f, fieldnames=cabecalho_jogadores).writeheader()

    if not os.path.exists(ficheiro_historico):
        with open(ficheiro_historico, 'w', newline='', encoding='utf-8') as f:
            csv.DictWriter(f, fieldnames=cabecalho_historico).writeheader()


def carregar_jogadores():
    jogadores = []
    with open(ficheiro_jogadores, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            row['vitorias'] = int(row['vitorias'])
            row['derrotas'] = int(row['derrotas'])
            jogadores.append(row)
    return jogadores


def guardar_jogadores(jogadores):
    with open(ficheiro_jogadores, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=cabecalho_jogadores)
        writer.writeheader()
        writer.writerows(jogadores)


def carregar_historico():
    with open(ficheiro_historico, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def guardar_historico(historico):
    with open(ficheiro_historico, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=cabecalho_historico)
        writer.writeheader()
        writer.writerows(historico)


def registar_jogador():
    nome = easygui.enterbox('Nome do novo jogador:', title='Registar Jogador')
    if not nome:
        return
    nome = nome.strip()

    jogadores = carregar_jogadores()
    nomes = [j['nome'].lower() for j in jogadores]

    if nome.lower() in nomes:
        easygui.msgbox(f'O jogador {nome} ja esta registado!', title='Erro')
        return

    jogo = easygui.enterbox(f'Jogo favorito de {nome}:', title='Registar Jogador')
    if not jogo:
        return

    jogadores.append({
        'nome': nome,
        'jogo_favorito': jogo.strip(),
        'vitorias': 0,
        'derrotas': 0
    })
    guardar_jogadores(jogadores)
    easygui.msgbox(f'Jogador {nome} registado com sucesso!', title='Sucesso')


def registar_resultado():
    jogadores = carregar_jogadores()
    nomes = [j['nome'] for j in jogadores]

    if len(nomes) < 2:
        easygui.msgbox('Sao necessarios pelo menos 2 jogadores!', title='Erro')
        return

    vencedor = easygui.choicebox('Quem GANHOU?', title='Registar Resultado', choices=nomes)
    if not vencedor:
        return

    outros = [n for n in nomes if n != vencedor]

    if len(outros) == 1:
        perdedor = outros[0]
    else:
        perdedor = easygui.choicebox('Quem PERDEU?', title='Registar Resultado', choices=outros)
    if not perdedor:
        return

    for j in jogadores:
        if j['nome'] == vencedor:
            j['vitorias'] += 1
        elif j['nome'] == perdedor:
            j['derrotas'] += 1

    guardar_jogadores(jogadores)

    historico = carregar_historico()
    historico.append({
        'vencedor': vencedor,
        'perdedor': perdedor,
        'data': datetime.now().strftime('%d/%m/%Y %H:%M')
    })
    guardar_historico(historico)

    easygui.msgbox(f'Resultado registado!\n\n{vencedor} venceu {perdedor}', title='Sucesso')


def ver_classificacao():
    jogadores = carregar_jogadores()

    if not jogadores:
        easygui.msgbox('Nenhum jogador registado ainda.', title='Classificacao')
        return

    ordenados = sorted(jogadores, key=lambda j: j['vitorias'], reverse=True)

    linhas = ['CLASSIFICACAO GERAL\n']
    linhas.append(f"{'Pos':<5} {'Nome':<20} {'Jogo Favorito':<20} {'V':>4} {'D':>4}")
    linhas.append('-' * 55)

    for i, j in enumerate(ordenados, 1):
        pos = f'{i}.'
        linhas.append(
            f"{pos:<5} {j['nome']:<20} {j['jogo_favorito']:<20} {j['vitorias']:>4} {j['derrotas']:>4}"
        )

    easygui.textbox('', title='Classificacao', text='\n'.join(linhas))


def ver_historico():
    historico = carregar_historico()

    if not historico:
        easygui.msgbox('Ainda nao ha jogos registados.', title='Historico')
        return

    linhas = ['HISTORICO DE JOGOS\n']
    linhas.append(f"{'#':<5} {'Data':<18} {'Vencedor':<20} {'Perdedor':<20}")
    linhas.append('-' * 63)

    for i, jogo in enumerate(historico, 1):
        linhas.append(
            f"{i:<5} {jogo['data']:<18} {jogo['vencedor']:<20} {jogo['perdedor']:<20}"
        )

    easygui.textbox('', title='Historico', text='\n'.join(linhas))


def remover_jogador():
    jogadores = carregar_jogadores()
    nomes = [j['nome'] for j in jogadores]

    if not nomes:
        easygui.msgbox('Nenhum jogador para remover.', title='Erro')
        return

    escolha = easygui.choicebox('Qual jogador remover?', title='Remover Jogador', choices=nomes)
    if not escolha:
        return

    confirmar = easygui.ynbox(
        f"Tens a certeza que queres remover '{escolha}'?\n\n(O historico de jogos e mantido.)",
        title='Confirmar'
    )
    if not confirmar:
        return

    jogadores = [j for j in jogadores if j['nome'] != escolha]
    guardar_jogadores(jogadores)
    easygui.msgbox(f'Jogador {escolha} removido.', title='Sucesso')


opcoes = [
    'Registar Jogador',
    'Registar Resultado',
    'Ver Classificacao',
    'Ver Historico',
    'Remover Jogador',
    'Sair'
]

def menu():
    inicializar()
    while True:
        escolha = easygui.buttonbox(
            'Bem-vindo ao Gestor de Torneio!\nEscolhe uma opcao:',
            title='Torneio de Jogos',
            choices=opcoes
        )

        if escolha is None or escolha == 'Sair':
            easygui.msgbox('Ate a proxima!', title='Sair')
            break
        elif escolha == opcoes[0]:
            registar_jogador()
        elif escolha == opcoes[1]:
            registar_resultado()
        elif escolha == opcoes[2]:
            ver_classificacao()
        elif escolha == opcoes[3]:
            ver_historico()
        elif escolha == opcoes[4]:
            remover_jogador()


if __name__ == '__main__':
    menu()