import csv

with open('filmes.csv', newline='', encoding='utf-8') as f:
    filmes = list(csv.DictReader(f))

filmes_ord = sorted(filmes, key=lambda f: float(f['Classificacao']), reverse=True)

with open('filmes_top.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.DictWriter(f, fieldnames=['Titulo', 'Ano', 'Classificacao', 'Genero'])
    escritor.writeheader()
    escritor.writerows(filmes_ord)

with open('filmes_top.csv', newline='', encoding='utf-8') as f:
    top = list(csv.DictReader(f))

for filme in top[:3]:
    print(f'{filme['Titulo']} — {filme['Classificacao']}')
