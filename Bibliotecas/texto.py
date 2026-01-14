def separador():
    print('-=' * 20)

def contar_vogais():
    texto = str(input('Insira um texto: '))
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    print(f'Na frase estão {contador} vogais na frase')
    separador()

def inverter_string():
    texto = str(input('Insira um texto: '))
    print(texto[::-1])
    separador()


def palindromo():
    palavra = str(input('Insira uma palavra: '))
    pali = palavra[::-1]
    if palavra == pali:
        print('A palavra é o palíndromo!')
    else:
        print('A palavra não é um palindromo!')
