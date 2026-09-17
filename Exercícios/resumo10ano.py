# RESUMO 10º ANO
# Módulo 1 - Algoritmia: produto de dois números e conversão de temperatura em Python.
# Conceito de algoritmo, formas de representação (linguagem natural, pseudocódigo, fluxograma), tipos de dados e traçagem de algoritmos simples (operações matemáticas, conversões, cálculos de preços/volumes).

c = float(input('Digite a temperatura em graus Celsius: '))

f = (c * 1.8) + 32
k = c + 273.15 

print('Temperatura em Fahrenheit:', f)
print('Temperatura em Kelvin:', k)

# Módulo 2 – Controlo de execução: decisão par/ímpar.
# Estruturas de decisão (simples, composta, seleção múltipla) e estruturas de repetição (Enquanto/While, Repita/Repeat), usando o VISUALG. Aplicação em exercícios como pares/ímpares, somatórios, tabuadas e médias.

n1 = int(input('Digite um nº para ver se é par ou ímpar: '))
if n1 % 2 == 0:
    print('O valor é par!')
else:
    print('O valor é ímpar!')

# Módulo 3 – Programação estruturada: função media(a, b, c) com return, e formatação de string com f-string.
# Transição para Python: sintaxe básica, funções (sem e com parâmetros, com return) e formatação de string

soma = 0
cont = 0

while True:
    nota = float(input('Digite a nota do aluno: '))
    soma += nota
    cont += 1
    
    continuar = input('Deseja continuar? 1 - sim / 0 - não: ')
    if continuar == '0':
        break

if cont > 0:
    media = soma / cont
    print(f'A média das notas inseridas é: {media}')
else:
    print('Nenhuma nota foi inserida.')

# Módulo 4 – Estruturas de dados estáticas: função recursiva factorial(n), e uso da biblioteca random.
# Recursividade e uso de bibliotecas Python, aplicados em exercícios e num desafio prático.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

numero = int(input('Introduz um número: '))
print(f'O factorial de {numero} é {factorial(numero)}')

# Módulo 5 – Estruturas de dados compostas: lista de notas, cálculo da média e ciclo for a percorrer a lista.
# Arrays/listas: criação, percorrer, calcular médias e outras operações, com um desafio prático de aplicação.

notas = [15, 17, 12, 20]

media = sum(notas) / len(notas)
print(f'Média: {media}')

maior = max(notas)
print(f'Maior nota: {maior}')

# Módulo 6 - Estruturas de dados dinâmicas: implementação simples de uma lista encadeada.
# Listas encadeadas e outras estruturas dinâmicas, incluindo exercícios de implementação.

n1 = {'valor': 1, 'prox': None}
n2 = {'valor': 2, 'prox': None}
n3 = {'valor': 3, 'prox': None}
n1['prox'] = n2
n2['prox'] = n3

a = n1
while a:
    print(a['valor'])
    a = a['prox']

# Módulo 7 – Tratamento de ficheiros: abrir um ficheiro em modo escrita, gravar texto, e depois ler o conteúdo linha a linha.
# Leitura e escrita de ficheiros de texto, manipulação de conteúdo.

with open('dados.txt', 'w') as f:
    f.write('Olá\nMundo\n')

with open('dados.txt', 'r') as f:
    for linha in f:
        print(linha.strip())

# Módulo 8 – Conceitos avançados: exemplo de interface gráfica simples com EasyGUI.
# Tópicos teóricos (Alan Turing e o Jogo da Imitação) e criação de interfaces gráficas simples com EasyGUI.

import easygui

nome = easygui.enterbox('Qual é o teu nome?')
easygui.msgbox(f'Olá, {nome}!')

# Módulo 9 – POO: classe simples (ex: Pessoa) com atributos, construtor __init__ e um método.
# Conceitos base de POO (classes, objetos) e uma componente prática com Ozobots (robótica).

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa('Ana', 20)
print(p.nome, p.idade)
