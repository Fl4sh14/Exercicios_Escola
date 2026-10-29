import random


class Personagem:
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


class Heroi(Personagem):
    def poder(self, alvo):
        print(f'{self.nome} usa o seu poder!')
        alvo.receber_dano(self.forca * 2)

    def saltar(self):
        print(f'{self.nome} saltou!')


class Monstro(Personagem):
    def investida(self, alvo):
        print(f'{self.nome} faz uma investida!')
        alvo.receber_dano(self.forca + 5)

    def curar(self, valor):
        self.vida += valor
        print(f'{self.nome} curou-se e ficou com {self.vida} de vida')


heroi = Heroi('Aragorn', 100, 15)
monstro = Monstro('Orc', 80, 12)

turnos = 0
while heroi.esta_vivo() and monstro.esta_vivo():
    turnos += 1
    print(f'--- Turno {turnos} ---')

    acao = random.choice(['atacar', 'poder', 'saltar'])
    if acao == 'atacar':
        heroi.atacar(monstro)
    elif acao == 'poder':
        heroi.poder(monstro)
    else:
        heroi.saltar()

    if monstro.esta_vivo():
        acao = random.choice(['atacar', 'investida', 'curar'])
        if acao == 'atacar':
            monstro.atacar(heroi)
        elif acao == 'investida':
            monstro.investida(heroi)
        else:
            monstro.curar(10)

vencedor = heroi if heroi.esta_vivo() else monstro
print(f'{vencedor.nome} venceu em {turnos} turnos')
