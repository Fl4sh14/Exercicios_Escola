soma = 0
cont = 0

while True:
    nota = float(input("Digite a nota do aluno: "))
    soma += nota
    cont += 1
    
    continuar = input("Deseja continuar? 1 - sim / 0 - não: ")
    if continuar == "0":
        break

if cont > 0:
    media = soma / cont
    print(f"A média das notas inseridas é: {media}")
else:
    print("Nenhuma nota foi inserida.")
