# sistema de registos de jogos favoritos
import pathlib as path
import easygui as eg

pasta = path.Path(__file__).parent / 'Sistema'  # fix 1
jogos = pasta / 'jogos.txt'
nomes = []
jogo_fav = []

def verificar_se_existe():
    pasta.mkdir(parents=True, exist_ok=True)  
    if not jogos.exists():
        with open(jogos, 'w', encoding='utf-8') as f:
            f.write('')

def guardar_nomes_jogos(nome, jogo_fav):
    with open(jogos, 'a', encoding='utf-8') as f:
        f.write(f'{nome} - {jogo_fav}\n')

def adicionar_jogador():
    verificar_se_existe()
    nome = eg.enterbox('Digite o seu nome: ', title='Nome')
    if nome:
        nome = nome.strip()
        jogo_fav = eg.enterbox('Digite o seu jogo favorito: ', title='Jogo')
        if jogo_fav:
            jogo_fav = jogo_fav.strip()
            guardar_nomes_jogos(nome, jogo_fav)
            eg.msgbox(f'Jogador {nome} adicionado com sucesso!', title='Sucesso')
        else:
            eg.msgbox('Jogo não pode estar vazio!', title='Erro')
    else:
        eg.msgbox('Nome não pode estar vazio!', title='Erro')

def remover_jogador():
    nome = eg.enterbox('Nome a remover: ', title='Remover')
    if not nome:
        return
    nome = nome.strip().lower()
    linhas = []
    with open(jogos, 'r', encoding='utf-8') as f:
        for linha in f:
            linha_limpa = linha.strip()
            if not linha_limpa:
                continue
            partes = linha_limpa.split(' - ', 1)
            nome_arquivo = partes[0].strip().lower()
            if nome_arquivo != nome:
                linhas.append(linha)
    with open(jogos, 'w', encoding='utf-8') as f:
        f.writelines(linhas)

def mostrar_jogadores():
    verificar_se_existe()
    mensagem = ''
    with open(jogos, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if linha and ' - ' in linha:
                partes = linha.split(' - ', 1)
                nome = partes[0].strip()
                jogo = partes[1].strip() if len(partes) > 1 else ''
                mensagem += f'{nome} | {jogo}\n'
    if mensagem:
        eg.textbox(title='Jogadores Registados', text=mensagem)
    else:
        eg.msgbox('Nenhum jogador registado!', title='Vazio')

opcoes = [
    'Adicionar Jogador',
    'Mostrar lista de jogadores',
    'Remover Jogador',
    'Sair'
]

def menu(opcoes):
    verificar_se_existe() 
    while True:
        escolha = eg.buttonbox(
            'Bem-vindo ao Sistema de registos de jogos favoritos!\nEscolhe uma opcao:',
            title='sistema de registos de jogos favoritos',
            choices=opcoes
        )
        if escolha is None or escolha == 'Sair':
            eg.msgbox('Até a proxima!', title='Sair')
            break
        elif escolha == opcoes[0]:
            adicionar_jogador()
        elif escolha == opcoes[1]:
            mostrar_jogadores()
        elif escolha == opcoes[2]:
            remover_jogador()

if __name__ == '__main__':
    menu(opcoes)  