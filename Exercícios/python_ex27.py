soma = 0

while True:
    n = float(input("Digite um número (negativo para parar): "))
    
    soma += n

    if n < 0:
        break  

print("A soma dos números positivos é:", soma)
