# Cria uma função maior(a, b) que compare dois números e imprima qual deles é o maior (ou se são iguais).
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

def maior(a, b):
    if a > b:
        print(f"O maior número é: {a}")
    elif b > a:
        print(f"O maior número é: {b}")
    else:
        print("Os números são iguais.")
maior(a, b)