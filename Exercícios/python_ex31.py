soma = 0

while True:
    n = float(input("Digite um número (0 para terminar): "))
    if n == 0:
        break
    soma += n

print("A soma dos números digitados é:", soma)
