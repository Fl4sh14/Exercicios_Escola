def separador():
    print('-=' * 20)

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    print(f'Na frase estão {contador} vogais na frase')
    separador()

def inverter_string(palavra):
    print(palavra[::-1])
    separador()


def palindromo(palavra):
    pali = palavra[::-1]
    if palavra == pali:
        print('A palavra é o palíndromo!')
    else:
        print('A palavra não é um palindromo!')
