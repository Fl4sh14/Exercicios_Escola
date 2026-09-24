import csv

with open('notas.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerow(['Nome', 'Nota'])
    escritor.writerow(['Ana Rita', 18])
    escritor.writerow(['Marcelo', 14])
    escritor.writerow(['Albana', 11])
    escritor.writerow(['Maria Joaquina', 19])

with open('notas.csv', 'r', encoding='utf-8') as f:
    leitor = csv.reader(f)
    next(leitor)
    for linha in leitor:
        print(f'{linha[0]} - {linha[1]}')
