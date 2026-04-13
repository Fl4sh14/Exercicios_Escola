import math

def area_circunferencia():
    raio = float(input('Raio da circunferência: '))
    area = math.pi * math.pow(raio, 2)
    print(f'A área da circunferência é {area}')

def perimetro_circunferencia():
    raio = float(input('Raio da circunferência: '))
    perimetro = 2 * math.pi * raio
    print(f'O perímetro da circunferência é {perimetro}')

def volume_esfera():
    raio = float(input('Raio da esfera: '))
    volume = (4/3) * math.pi * math.pow(raio, 3)
    print(f'O volume da esfera é {volume}')

area_circunferencia()
perimetro_circunferencia()
volume_esfera()
