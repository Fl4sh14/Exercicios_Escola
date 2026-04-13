import random
import string

def numero_faces():
    faces = int(input('Digite o número de faces do dado: '))
    return faces

def elemento_aleatorio():
    numeros = []
    while True:
        numero = int(input('Digite um número: '))
        numeros.append(numero)
        resposta = input('Quer inserir mais? [S/N]: ').strip().lower()
        if resposta == 'n':
            break
    elemento = random.choice(numeros)
    return elemento

def gerar_password(comprimento):
    caracteres = string.ascii_letters + string.digits
    password = ''.join(random.choice(caracteres) for i in range(comprimento))
    return password


numero_faces()
elemento_aleatorio()
comprimento = int(input('Digite o comprimento da password: '))
gerar_password(comprimento)
