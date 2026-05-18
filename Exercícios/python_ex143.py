import csv

with open('corridas.csv', newline='', encoding='utf-8') as f:
    dados = list(csv.DictReader(f))

tempos = [float(d['Tempo']) for d in dados]
media = round(sum(tempos) / len(tempos), 2)

mais_rapido = dados[0]
mais_lento = dados[0]

for d in dados:
    if float(d['Tempo']) < float(mais_rapido['Tempo']):
        mais_rapido = d
    if float(d['Tempo']) > float(mais_lento['Tempo']):
        mais_lento = d

print(f'Média: {media}s')
print(f'Mais rápido: {mais_rapido['Nome']} — {mais_rapido['Tempo']}s')
print(f'Mais lento: {mais_lento['Nome']} — {mais_lento['Tempo']}s')

