soma = 0
cont = 0

while True:
    nota = float(input("Digite a nota do aluno (0 a 10): "))
    
    if 0 <= nota <= 10:
        soma += nota
        cont += 1
    else:
        print("Nota incorreta")
        break  

if cont > 0:
    media = soma / cont
    print(f"A média das notas válidas é: {media}")
else:
    print("Nenhuma nota válida foi inserida.")
