n1 = float(input('Digite a nota N1: '))
n2 = float(input('Digite a nota N2: '))
n3 = float(input('Digite a nota N3: '))

md1 = (n1 + n2 + n3) / 3

print(f'Média MD1 = {md1}')

if md1 >= 10:
    print('Aprovado')
else:
    ne = float(input('Digite a nota do exame (ne): '))
    
    md2 = (md1 + ne) / 2
    
    print(f'Média MD2 = {md2}')
    
    if md2 >= 10:
        print('Aprovado em exame')
    else:
        print(f'Reprovado, com a média: {md2}')
