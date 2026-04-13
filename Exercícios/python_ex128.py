n = int(input('Número de utilizadores: '))

matriz = []

for i in range(n):
    likes = list(map(int, input(f'Likes do utilizador {i+1} em 3 dias: ').split()))
    matriz.append(likes)

flatten = []
for linha in matriz:
    for like in linha:
        flatten.append(like)

print('Lista achatada:', flatten)

total = sum(flatten)
print('Total de likes:', total)

media_diaria = total / 3
print('Média diária:', media_diaria)

max_likes = matriz[0][0]
utilizador_max = 1
dia_max = 1

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > max_likes:
            max_likes = matriz[i][j]
            utilizador_max = i + 1
            dia_max = j + 1

print('Maior número de likes num único dia:', max_likes)
print('Utilizador com maior número de likes:', utilizador_max, 'Dia:', dia_max)
