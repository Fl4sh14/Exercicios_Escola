import csv

with open('marcadores.csv', 'w', newline='') as f:
    escritor = csv.writer(f)
    escritor.writerow(['nome', 'pontos'])
    escritor.writerow(['Albana', 150])
    escritor.writerow(['Bruninho', 200])

with open('marcadores.csv', 'a', newline='') as f:
    escritor = csv.writer(f)
    escritor.writerow(['Vitor', 180])
    escritor.writerow(['Diana', 220])

with open('marcadores.csv', 'a', newline='') as f:
    escritor = csv.writer(f)
    escritor.writerow(['Eva', 310])

print('=== Marcadores ===')
with open('marcadores.csv', 'r') as f:
    leitor = csv.reader(f)
    jogadores = list(leitor)
    for linha in jogadores:
        print(linha)

total = len(jogadores) - 1
print(f'\nTotal de jogadores: {total}')
