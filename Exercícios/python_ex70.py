def divisivel_por_2():
    numero = int(input("Digite um número inteiro positivo: "))
    if numero % 2 == 0:
        return True
    else:
        return False
    
for i in range(0, 20):
    resultado = divisivel_por_2()
    if resultado:
        print("o número é par")
    else:
        print("o número é impar")