poço = []

profundidade_poço = 20
subida_dia = 5
descida_noite = 4

altura_atual = 0
dias = 0

while True:
    dias += 1
    
    altura_atual += subida_dia
    poço.append(altura_atual)  
    
    if altura_atual >= profundidade_poço:
        break
    
    altura_atual -= descida_noite
    poço.append(altura_atual)

print(f'O caracol levará {dias} dias para sair do poço.')
