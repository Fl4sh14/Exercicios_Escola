import datetime 

# pede o ano ao utilizador
def pedir_ano():
    ano = int(input('Digite um ano: '))
    return ano

# verifica se o ano é inválido
def ano_invalido(ano):
    if ano > datetime.MAXYEAR:
        ano == 'Ano inválido!'
        return ano
    elif ano < datetime.MINYEAR:
        ano == 'Ano inválido!'
        return ano
    else:
        return ano

# verifica se o ano é bissexto
def bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        ano_bissexto = True
    else:
        ano_bissexto = False
    return ano_bissexto


# ================ Programa Principal ======================

# lista do meses 
meses_30 = [4, 6, 9, 11]
meses_31 = [1, 3, 5, 7, 8, 10, 12]

ano = pedir_ano()
ano = ano_invalido(ano)
ano_bissexto = bissexto(ano)

if ano_bissexto == True:
    fevereiro = 29
else:
    fevereiro = 28

if fevereiro == 29:
    total_dias = 366
else:
    total_dias = 365
