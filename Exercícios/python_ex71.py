def custo_combustivel(distancia, consumo_medio = 5.3, custo_comb = 1.62):
    if distancia <= 0:
        return 0
    litros = (distancia * consumo_medio) / 100
    custo_total = litros * custo_comb
    return custo_total

resultado_a = custo_combustivel(306, 6.4, 1.65)
print(f'Caso a) Custo da viagem: {resultado_a} €')

resultado_b = custo_combustivel(206, custo_comb=1.65)
print(f'Caso b) Custo da viagem: {resultado_b} €')

resultado_c = custo_combustivel(73, 6.4)
print(f'Caso c) Custo da viagem: {resultado_c} €')

resultado_d = custo_combustivel(509)
print(f'Caso d) Custo da viagem: {resultado_d} €')
