# Aluguer de Trotinetes
minutos_utilizados =int(input('Insira o tempo de aluguer entre 1 e 60 minutos (-1minutos para sair):'))
while minutos_utilizados != -1:
    if minutos_utilizados > 60:
        print('numero invalido')
    elif minutos_utilizados < 10:
        print('valor a pagar é:1€')
    elif minutos_utilizados < 30:
        print('valor a pagar é:0,10€ por minuto')
    elif minutos_utilizados < 60:
        print('valor a pagar é:0,05€ por minuto')
    minutos_utilizados =int(input('Insira o tempo de aluguer entre 1 e 60 minutos (-1minutos para sair):'))