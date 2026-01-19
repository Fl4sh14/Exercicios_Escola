def separador():
    print('-=' * 20)

def par(numero):
    if numero % 2 == 0:
        print('O número é par!')
    else:
        print('O número é ímpar!')
    separador()

def positivo(numero):
    if numero >= 0:
        print('O número é positivo!')
    else:
        print('O número é negativo!')
    separador()

def vazia(texto):
    if texto.strip() == '':
        print('A string está vazia!')
    else:
        print('A string não está vazia!')
    separador()

def email(email):
    if "@" in email and "." in email:
        print('O email é válido!')
    else:
        print('O email é inválido!')
    separador()
