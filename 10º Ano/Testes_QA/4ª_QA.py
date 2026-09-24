palavra = ''

# função para fazer um separador
def sep():
    print('-=' * 20)

# função para pedir a palavra 
def pedir():
    palavra = str(input('Digite uma palavra [Digite "Terminei" para parar]: ')).strip()
    return palavra

# função para inverter a palavra
def invertida(palavra):
    return palavra[::-1]

# função para contar as vogais
def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    total = 0

    #1 forma -  total = palavra.lower().count('a') + palavra.lower().count('e') + palavra.lower().count('i') + palavra.lower().count('o') + palavra.lower().count('u')

    #2 forma - for letra in palavra:
    #               if letra in vogais:
    #               total += 1
    #          return total

    # 3 forma - 
    total = sum(1 for letra in palavra if letra in vogais)
    return total

# ============ Programa Principal =================
sep()
print('Olá seja Bem-Vindo!')
sep()

palavra = pedir()
while palavra != 'terminei':
    palavra_invertida = invertida(palavra)
    vogais = contar_vogais(palavra)

    print(f'Palavra: {palavra};')
    print(f'Palavra invertida: {palavra_invertida}')
    print(f'Vogais na palavra: {vogais}')
    sep()
    palavra = pedir()
print('Terminou, Obrigado Volte Sempre')
sep()
sep()
