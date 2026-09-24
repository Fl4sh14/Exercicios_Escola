from pathlib import Path

pasta_saves = Path('esbn_python')


if not pasta_saves.exists():
    pasta_saves.mkdir()
    print('Pasta de invasores criada!')
    ficheiro = pasta_saves / 'progresso.txt'
    ficheiro.write_text('Nivel 1-100 XP')

print(f'Progresso guardado em: (ficheiro.absolute())')
