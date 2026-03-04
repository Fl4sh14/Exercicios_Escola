from collections import deque
lista = deque()

lista.appendleft('Objeto 1')
lista.append('Objeto 2')

def mostrar_lista(lista):
    for objetos in lista:
        print(objetos)
mostrar_lista(lista)