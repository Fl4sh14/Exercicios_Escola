def funcao(arg_1, arg_2, *args, **kwargs):
    print(f'Parâmetro 1: {arg_1}')
    print(f'Parâmetro 2: {arg_2}')
    print(f'*args: {args}')
    print(f'**kwargs: {kwargs}')

# Chamada da Função
funcao(
    1,              # argumento 1
    'a',            # argumento 2
    'arg1',         # *args
    'arg2',         # *args
    2,              # *args
    Banana='B',     # **kwargs
    Ananás='A'      # **kwargs
)



def func(*args, **kwargs):
    print(f'Argumentos com "args": {args}')  # Argumentos com "args":  ('Fundamentos', 'de', 'Python')
    print(f'Argumentos com Kwargs: {kwargs}')  # Argumentos com Kwargs: {'primeiro': 'Fundamentos', 'meio': 'de', 'ultimo': 'Python'}

func('Fundamentos', 'de', 'Python', primeiro='Fundamentos', meio='de', ultimo='Python')



def func(*args, **kwargs):
    print(f'Argumentos com *args: {args}')  # Argumentos com *args: ('Fundamentos', 'de', 'Python')
    print(f'Argumentos com Kwargs: {kwargs}')  # Argumentos com Kwargs: {'primeiro': 'Fundamentos', 'meio': 'de', 'ultimo': 'Python'}

func('Fundamentos', 'de', 'Python', primeiro='Fundamentos', meio='de', ultimo='Python')

