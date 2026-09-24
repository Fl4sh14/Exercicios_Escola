import csv

with open('amigos.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerow(['Nome', 'Idade'])
    escritor.writerow(['Ana Maria', 15])
    escritor.writerow(['José', 16])
    escritor.writerow(['Zé', 17])

    leitor = csv.reader(f)

for linha in leitor:
    nome = linha[0]
