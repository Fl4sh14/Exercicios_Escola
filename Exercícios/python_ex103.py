inventário = []

item1 = {'Nome': 'Espada de Madeira'}
item2 = {'Nome': 'Escudo de couro'}

inventário.append(item1)
inventário.append(item2)

print(inventário)

#durante a batalha

item3 = {'Nome': 'Poção de cura'}

inventário.pop(0)
inventário.append(item3)
print(inventário)