val = float(input('Valor original da prestação: '))
tax = float(input('Taxa de juros (%): '))
temp = int(input('Tempo em atraso (meses): '))

prest = val + (val * (tax / 100) * temp)

print('Valor da prestação em atraso: ', prest)
