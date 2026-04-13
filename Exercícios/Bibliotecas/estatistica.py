def separador():
    print('-=' * 20)

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
    separador()

def media(numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    print(f'Média: {media}')
    separador()


def maior_valor(numeros):
    maior = max(numeros)
    print(f'Maior valor: {maior}')
    separador()

def menor_valor(numeros):
    menor = min(numeros)
    print(f'Menor valor: {menor}')
    separador()

def numeros_maiores_media(numeros):
    med = sum(numeros) / len(numeros)
    contagem = 0
    for numero in numeros:
        if numero > med:
            contagem += 1
    print(f'Números maiores que a média: {contagem}')
    separador()