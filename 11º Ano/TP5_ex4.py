class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.pontos = 0

    def receber_dano(self, valor):
        self.vida = max(0, self.vida - valor)

    def curar(self, valor):
        self.vida = min(100, self.vida + valor)

    def ganhar_pontos(self, valor):
        self.pontos += valor

    def esta_vivo(self):
        return self.vida > 0


# teste 1
jog1 = Jogador('Zé')
jog1.receber_dano(130)
print(jog1.vida, jog1.esta_vivo())

# teste 2
jog2 = Jogador('Armando')
jog2.receber_dano(30)
jog2.curar(50)
print(jog2.vida, jog2.esta_vivo())
