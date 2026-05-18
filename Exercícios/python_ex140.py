import csv

with open('musicas.csv', encoding='utf-8') as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        print(f'{linha['Artista']} — {linha['Título']}')
