from abc import ABC, abstractmethod
from math import pi


class FormaGeometrica(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_area(self):
        pass


class Retangulo(FormaGeometrica):
    def __init__(self, comprimento, largura):
        super().__init__('Retângulo')
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__('Círculo')
        self.raio = raio

    def calcular_area(self):
        return pi * self.raio ** 2


formas = [Retangulo(5, 3), Circulo(2)]

for forma in formas:
    print(f'{forma.nome}: área = {forma.calcular_area():.2f}')
