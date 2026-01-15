import AA_Uteis as ut 

# pede númeeros até o usuário escrever nao  
def coletar_numeros(numeros):
    numeros = []
    while True:
        numero = float(input('Digite um número: '))
        numeros.append(numero)
        resposta = input('Quer inserir mais? [S/N]: ').strip().lower()
        if resposta == 'n':
            break
    return numeros
    ut.separador()

def media(numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    print(f'Média: {media}')
    ut.separador()


def maior_valor(numeros):
    maior = max(numeros)
    print(f'Maior valor: {maior}')
    ut.separador()

def menor_valor(numeros):
    menor = min(numeros)
    print(f'Menor valor: {menor}')
    ut.separador()

def numeros_maiores_media(numeros):
    med = media(numeros)
    contagem = 0
    for numero in numeros:
        if numero > med:
            contagem = contagem + 1
    print(f'Números maiores que a média: {contagem}')
    ut.separador()