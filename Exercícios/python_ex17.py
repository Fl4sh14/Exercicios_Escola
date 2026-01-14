aval = int(input("Insere uma avaliação (1 a 5): "))

match aval:
    case 1:
        print("Muito Insuficiente")
    case 2:
        print("Insuficiente")
    case 3:
        print("Suficiente")
    case 4:
        print("Bom")
    case 5:
        print("Muito Bom")
    case _:
        print("Valor inválido! Insere um número entre 1 e 5.")
