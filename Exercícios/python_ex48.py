nivel = str(input('Digite o vível do aviso: '))

def aviso(nivel):
    if nivel == 'alto':
        print('AVISO DE NÍVEL ALTO!')
    elif nivel == 'médio':
        print('Aviso de nível médio.')
    else:
        print('Aviso de nível baixo.')

aviso(nivel)
