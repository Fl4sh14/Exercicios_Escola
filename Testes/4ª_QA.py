palavra = ''

# função para fazer um separador
def sep():
    print('-=' * 20)

# função para pedir a palavra 
def pedir():
    palavra = str(input('Digite uma palavra [Digite "Terminei" para parar]: ')).strip().lower()
    return palavra

# função para inverter a palavra
def invertida(palavra):
    return palavra[::-1]

# função para contar as vogais
def contar_vogais(palavra):
    contagem = 0
    vogais = "aeiouAEIOU"
    total = palavra.lower().count('a') + palavra.lower().count('e') + palavra.lower().count('i') + palavra.lower().count('o') + palavra.lower().count('u')
    return total

# ============ Programa Principal =================
sep()
print('Olá seja Bem-Vindo!')
sep()
while palavra != 'terminei':
    palavra = pedir()
    palavra_invertida = invertida(palavra)
    vogais = contar_vogais(palavra)

    print(f'Palavra: {palavra};')
    print(f'Palavra invertida: {palavra_invertida}')
    print(f'Vogais na palavra: {vogais}')
    sep()
print('Terminou, Obrigado Volte Sempre')
sep()
sep()
