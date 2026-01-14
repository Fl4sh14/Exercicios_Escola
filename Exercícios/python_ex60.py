def converter():
    minutos = int(input("Digite o número de minutos: "))
    segundos = minutos * 60
    return segundos
resultado = converter()
print(f"O equivalente em segundos é: {resultado} segundos.")