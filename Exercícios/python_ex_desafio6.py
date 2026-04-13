#Parte 1

# a) Criação da lista
Palcos = [
    'Palco_principal',
    'Palco_Indie',
    'Palco_eletrónico'
]

# b) Criação do dicionário
artistas = {
    'Drake': {
        'genero': 'Hip-Hop',
        'palco': 'Palco_principal',
        'hora': '22:00',
        'bilhetes_vendidos': 50000
    },
    'Taylor Swift': {
        'genero': 'Pop',
        'palco': 'Palco_principal',
        'hora': '20:00',
        'bilhetes_vendidos': 60000
    },
    'Bad Bunny': {
        'genero': 'Reggaeton',
        'palco': 'Palco_Indie',
        'hora': '23:00',
        'bilhetes_vendidos': 45000
    },
    'Coldplay': {
        'genero': 'Rock',
        'palco': 'Palco_principal',
        'hora': '21:00',
        'bilhetes_vendidos': 55000
    },
    'Billie Eilish': {
        'genero': 'Pop Alternativo',
        'palco': 'Palco_Indie',
        'hora': '19:00',
        'bilhetes_vendidos': 40000
    }
}

# c) Criação da lista de dicionários
participantes = [
    {'nome': 'Cláudio',  'tipo': 'VIP', 'idade': 15},
    {'nome': 'Marcelino',   'tipo': 'VIP', 'idade': 16},
    {'nome': 'Povoa',   'tipo': 'Geral',    'idade': 15},
    {'nome': 'Lukas',   'tipo': 'Geral',    'idade': 16}
]


# Parte 2
def cartaz(artistas):
    print('=' * 50)
    print('         FESTIVAL CARTAZ COMPLETO ')
    print('=' * 50)
    for nome, info in artistas.items():
        linha = f'{nome.upper()} | {info["palco"].upper()} | {info["hora"]}'
        print(linha)
    print('=' * 50)


def pesquisar_por_palco(artistas, nome_palco):
     return [
        nome
        for nome, info in artistas.items()
        if info['palco'].lower() == nome_palco.lower()
    ]


def headliner(artistas):
    if not artistas:
        return None
    artista_top = max(artistas.items(), key=lambda item: item[1].get('bilhetes_vendidos', 0))
    return artista_top[0]


def credencial(participante):
    tipo = participante['tipo'].upper()
    nome = participante['nome']
    idade = participante['idade']

    conteudo = f'{tipo} | {nome} | {idade} anos'
    return f'===[{conteudo.center(len(conteudo) + 2)}]==='


def estatisticas(artistas, participantes):
    total_artistas = len(artistas)
    total_participantes = len(participantes)
    num_vips = sum(1 for p in participantes if p['tipo'].upper() == 'VIP')

    contagem_generos = {}
    for info in artistas.values():
        genero = info.get('genero', 'N/A')
        contagem_generos[genero] = contagem_generos.get(genero, 0) + 1

    genero_top = max(contagem_generos, key=contagem_generos.get) if contagem_generos else 'N/A'

    print('\n' + '=' * 40)
    print('       ESTATÍSTICAS DO FESTIVAL')
    print('=' * 40)
    print(f'  Artistas no festival  : {total_artistas}')
    print(f'  Total de participantes: {total_participantes}')
    print(f'  Participantes VIP     : {num_vips}')
    print(f'  Género mais popular  : {genero_top}')
    print('=' * 40)


def adicionar_artista(artistas, palcos):
    print('\nAdicionar novo artista:')
    nome = input('Nome do artista: ').strip()
    if not nome:
        print('Nome inválido. Não foi possível adicionar o artista.')
        return

    if nome in artistas:
        print('Já existe um artista com esse nome. Nenhuma alteração foi feita.')
        return

    genero = input('Género musical: ').strip() or 'Indefinido'
    palco = input(f'Palco ({", ".join(palcos)}): ').strip()
    if palco.lower() not in (p.lower() for p in palcos):
        print('Palco não existe na lista de palcos. Artista não foi adicionado.')
        return

    hora = input('Hora da atuação (ex: 18:30): ').strip()
    bilhetes_texto = input('Bilhetes vendidos (número): ').strip()
    try:
        bilhetes_vendidos = int(bilhetes_texto)
    except ValueError:
        print('Número de bilhetes inválido. Artista não foi adicionado.')
        return

    artistas[nome] = {
        'genero': genero,
        'palco': palco,
        'hora': hora,
        'bilhetes_vendidos': bilhetes_vendidos
    }
    print(f'Artista "{nome}" adicionado com sucesso ao palco "{palco}".')


def main():
    print('--- Desafio Extra: Gestão de Festival ---')
    cartaz(artistas)

    print(f'Headliner: {headliner(artistas)}')
    estatisticas(artistas, participantes)

    print('\nCredenciais dos participantes:')
    for p in participantes:
        print(credencial(p))

    palco_escolhido = input('\nIntroduza o nome de um palco para ver quem atua nele: ').strip()
    artistas_no_palco = pesquisar_por_palco(artistas, palco_escolhido)
    if artistas_no_palco:
        print(f'Artistas no palco "{palco_escolhido}":')
        for nome in artistas_no_palco:
            info = artistas[nome]
            print(f' - {nome} ({info["genero"]}, {info["hora"]})')
    else:
        print(f'Não foram encontrados artistas no palco "{palco_escolhido}".')

    adicionar_artista(artistas, Palcos)
    print('\nCartaz atualizado:')
    cartaz(artistas)


if __name__ == '__main__':
    main()
