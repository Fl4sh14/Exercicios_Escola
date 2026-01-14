n = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {n}:")
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")
