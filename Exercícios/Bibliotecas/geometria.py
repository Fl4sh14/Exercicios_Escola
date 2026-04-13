import math 

def area_quadrado():
    lado1 = float(input('Lado 1: '))
    lado2 = float(input('Lado 2: '))
    area = lado1 * lado2
    print(f'A área do quadrado é {area}')


def area_circulo():
    raio = float(input('Raio do círculo: '))
    area =  math.pi * raio ** 2
    print(f'A área do círculo é {area}') 

def perimetro_retangulo():
    com = float(input('Comprimento do retangulo:'))
    larg = float(input('Largura do retangulo '))
    perimetro = (2 * com) + (2 * larg)
    print(f'O perímetro do retânulo é {perimetro}')
        