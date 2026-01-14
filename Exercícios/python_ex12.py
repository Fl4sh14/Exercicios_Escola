temp = float(input("Digite o tempo gasto na viagem (em horas): "))
velo = float(input("Digite a velocidade média (em km/h): "))

dist = temp * velo
lit = dist / 12

print('Velocidade média:', velo,' km/h')
print('Tempo gasto: ',temp, 'horas')
print('Distância percorrida:',dist,' km')
print('Litros utilizados: ',lit,'L')
