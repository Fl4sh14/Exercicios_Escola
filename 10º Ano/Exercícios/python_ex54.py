# Cria uma função calcular_media(a, b, c) que imprima a média de três números.
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

def calcular_media(a, b, c):
    media = (a + b + c) / 3
    print(f"A média dos três números é : {media}")
calcular_media(a, b, c)