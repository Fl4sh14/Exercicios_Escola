for i in range (0, 10):
    nome = str(input('Escreva o seu nome: '))
    vencimento_bruto = float(input('Escreva o seu vencimento bruto: '))
    taxa = float(input('Escreva a sua taxa de descontos: '))
    salario_liquido = vencimento_bruto - taxa
    print ('O salario liquido do ', nome,' é: ', salario_liquido)
