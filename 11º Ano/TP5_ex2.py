class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def mostrar(self):
        print(f'A área do retângulo é: {self.area()}. O perímetro é: {self.perimetro()}.')
        if self.largura == self.altura:
            print('É um quadrado!')

# teste
r1 = Retangulo(20, 10)
r2 = Retangulo(15, 15)
r3 = Retangulo(40, 5)

r1.mostrar()
r2.mostrar()
r3.mostrar()
