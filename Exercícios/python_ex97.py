def mostrar_notas(lista):
    print(lista)

def media_notas(lista):
    return sum(lista) / len(lista)

def contar_positivas(lista):
    contagem = 0
    for nota in lista:
        if nota >= 10:
            contagem += 1
    return contagem

notas = [1, 2, 15, 20, 8, 10, 5]

mostrar_notas(notas)
print(f"Média das notas: {media_notas(notas):.2f}")
print(f"Notas positivas: {contar_positivas(notas)}")
