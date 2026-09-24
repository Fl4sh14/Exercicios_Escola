# Cria uma função repetir(texto, n) que imprima o texto N vezes.
texto = str(input("Digite o texto a ser repetido: "))
n = int(input("Digite o número de repetições: "))

def repetir(texto, n):
    for i in range(n):
        print(texto)
repetir(texto, n)