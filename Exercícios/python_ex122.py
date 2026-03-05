from collections import deque

fila_normal = deque()   # FIFO
pilha_urgente = deque() # LIFO

def adicionar_paciente(nome, urgente=False):
    if urgente:
        pilha_urgente.append(nome)   
        print(f'Paciente URGENTE {nome} adicionado à pilha.')
    else:
        fila_normal.append(nome)    
        print(f'Paciente {nome} adicionado à fila normal.')

def atender_paciente():
    if pilha_urgente:
        paciente = pilha_urgente.pop()  # LIFO
        print(f'Atendendo paciente URGENTE: {paciente}')
    elif fila_normal:
        paciente = fila_normal.popleft()  # FIFO
        print(f'Atendendo paciente normal: {paciente}')
    else:
        print('Não há pacientes para atender.')


adicionar_paciente('Ana')
adicionar_paciente('Bruno')
adicionar_paciente('Carlos', urgente=True)
adicionar_paciente('Diana')
adicionar_paciente('Eduardo', urgente=True)

print('--- Início do Atendimento ---')

while fila_normal or pilha_urgente:
    atender_paciente()
