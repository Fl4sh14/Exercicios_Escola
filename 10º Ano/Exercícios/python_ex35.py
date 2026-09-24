while True:
    print("Menu:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        break
    elif opcao == "1":
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))
        print("Resultado da soma:", a + b)
    elif opcao == "2":
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))
        print("Resultado da subtração:", a - b)
    else:
        print("Opção inválida")
