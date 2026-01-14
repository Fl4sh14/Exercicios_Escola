def maioridade():
    idade = int(input("Digite a sua idade: "))
    if idade >= 18:
        return True
    else:
        return False
boleano = maioridade()
print(f"Maior de idade: {boleano}")