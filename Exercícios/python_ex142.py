import csv

aprovados = 0
reprovados = 0

with open('alunos.csv', newline='', encoding='utf-8') as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        if int(linha['Nota']) >= 10:
            print(f'Aprovado: {linha['Nome']} — {linha['Nota']}')
            aprovados += 1
        else:
            reprovados += 1

print(f'\nAprovados: {aprovados} | Reprovados: {reprovados}')
