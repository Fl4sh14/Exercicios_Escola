class Heroi:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, alvo):
        alvo.receber_dano(self.forca)

    def receber_dano(self, valor):
        self.vida = max(0, self.vida - valor)
        print(f'{self.nome} ficou com {self.vida} de vida')

    def esta_vivo(self):
        return self.vida > 0


class Monstro:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, alvo):
        alvo.receber_dano(self.forca)

    def receber_dano(self, valor):
        self.vida = max(0, self.vida - valor)
        print(f'{self.nome} ficou com {self.vida} de vida')

    def esta_vivo(self):
        return self.vida > 0


heroi = Heroi('Aragorn', 100, 15)
monstro = Monstro('Orc', 80, 12)

turnos = 0
while heroi.esta_vivo() and monstro.esta_vivo():
    turnos += 1
    print(f'--- Turno {turnos} ---')
    heroi.atacar(monstro)
    if monstro.esta_vivo():
        monstro.atacar(heroi)

vencedor = heroi if heroi.esta_vivo() else monstro
print(f'{vencedor.nome} venceu em {turnos} turnos')
