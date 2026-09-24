ano_atual = 2025

for i in range(1, 4):
    print("\nAluno", i)
    nome = input("Nome: ")
    ano = int(input("Ano de nascimento: "))
    
    idade = ano_atual - ano
    
    if idade >= 0 and idade <= 2:
        ciclo = "Creche"
    elif idade >= 3 and idade <= 5:
        ciclo = "Pré-escolar"
    elif idade >= 6 and idade <= 9:
        ciclo = "1.º Ciclo"
    elif idade >= 10 and idade <= 11:
        ciclo = "2.º Ciclo"
    elif idade >= 12 and idade <= 14:
        ciclo = "3.º Ciclo"
    elif idade >= 15 and idade <= 17:
        ciclo = "Secundário"
    else:
        ciclo = "O ano de nascimento que inseriu está errado"
    
    print(nome, "tem", idade, "anos e está no", ciclo)
