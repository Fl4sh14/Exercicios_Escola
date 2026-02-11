loja = []

item1 = {'Skin Lendária': 2000}

item2 = {'Dança': 500}

item3 = {'Picareta': 800}

loja.append(item1)
loja.append(item2)
loja.append(item3)

escolha = int(input('''=====LOJA=====
[1] Skin Lendária 
[2] Dança
[3] Picareta 
============
Que item quer ver o preço?: '''))

if escolha == 1:
    print(f'O preço é {item1["Skin Lendária"]}')
elif escolha == 2:
    print(f'O preço é {item1["Skin Lendária"]}')
elif escolha == 3:
    print(f'O preço é {item1["Skin Lendária"]}')
else:
    print('Resposta inválida! Tente novamente.')
    escolha = int(input('''=====LOJA=====
[1] Skin Lendária 
[2] Dança
[3] Picareta 
============
Que item quer ver o preço?: '''))
