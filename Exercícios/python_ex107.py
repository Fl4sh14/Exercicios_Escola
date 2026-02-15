passos = []
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

for i in range(7):
    valor = int(input(f"Quantos passos deste na {dias[i]}? "))
    passos.append(valor)

maior = max(passos)
menor = min(passos)

dia_maior = dias[passos.index(maior)]
dia_menor = dias[passos.index(menor)]

media = sum(passos) / 7

print('===RESULTADOS===')
print(f'Dia com mais passos: {dia_maior} ({maior} passos)')
print(f'Dia com menos passos: {dia_menor} ({menor} passos)')
print(f'Média de passos por dia: {media:.2f}')
