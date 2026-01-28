def contar_pares(lista):
    pares = []
    for numeros in lista:
        if numeros % 2 == 0:
            pares.append(numeros)
    return pares

lista = [1, 2, 3, 4, 5, 6]
print(contar_pares(lista))
