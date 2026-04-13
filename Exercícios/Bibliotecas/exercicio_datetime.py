from datetime import datetime

def data_hora_atual():
    agora = datetime.now()
    print(f'Data: {agora.strftime("%d/%m/%Y")}')
    print(f'Hora: {agora.strftime("%H:%M:%S")}')

def calcular_idade(dia, mes, ano):
    data_nasc = datetime(ano, mes, dia)
    idade = datetime.now().year - data_nasc.year
    if (datetime.now().month, datetime.now().day) < (mes, dia):
        idade -= 1
    print(f'Idade: {idade} anos')
    return data_nasc

def dias_para_aniversario(data_nasc):
    agora = datetime.now()
    prox_aniv = datetime(agora.year, data_nasc.month, data_nasc.day)
    if prox_aniv < agora:
        prox_aniv = prox_aniv.replace(year=agora.year + 1)
    print(f'Dias para aniversário: {(prox_aniv - agora).days}')

def dia_semana_nascimento(data_nasc):
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    print(f'Nascido numa {dias[data_nasc.weekday()]}-feira')


data_hora_atual()
calcular_idade()
dias_para_aniversario()
dia_semana_nascimento()