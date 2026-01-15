from AA_Uteis import separador as sep

def par(numero):
    if numero % 2 == 0:
        print('O número é par!')
    else:
        print('O número é ímpar!')
    sep()

def positivo(numero):
    if numero >= 0:
        print('O número é positivo!')
    else:
        print('O número é negativo!')
    sep()

def vazia(texto):
    if texto.strip() == '':
        print('A string está vazia!')
    else:
        print('A string não está vazia!')
    sep()

def email(email):
    if "@" in email and "." in email:
        print('O email é válido!')
    else:
        print('O email é inválido!')
    sep()
