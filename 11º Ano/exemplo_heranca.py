import random


class Personagem:
    def __init__(self, nome, vida, forca):
        if forca < 0:
            print('A força não pode ser negativa')
            forca = int(input('Escreve um valor para a força: '))

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
    salto = 0

    def poder(self, alvo):
        print(f'{self.nome} usa o seu poder!')
        alvo.receber_dano(self.forca * 2)

    def saltar(self):
        self.salto = random.randint(50, 300)
        print(f'{self.nome} saltou {self.salto} cm!')


class Monstro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida, forca)
        self.altura = random.randint(10, 500)

    def acertou(self, alvo):
        if alvo.salto > self.altura:
            print(f'{alvo.nome} saltou por cima de {self.nome}!')
            return False
        return True

    def atacar(self, alvo):
        if self.acertou(alvo):
            super().atacar(alvo)

    def investida(self, alvo):
        print(f'{self.nome} faz uma investida!')
        if self.acertou(alvo):
            alvo.receber_dano(self.forca + 5 + self.altura // 50)


heroi = Heroi('Aragorn', 100, -5)
monstro = Monstro('Orc', 80, 12)
print(f'{monstro.nome} mede {monstro.altura} cm')

turnos = 0
while heroi.esta_vivo() and monstro.esta_vivo():
    turnos += 1
    print(f'--- Turno {turnos} ---')
    heroi.salto = 0

    acao = random.choice(['atacar', 'poder', 'saltar'])
    if acao == 'atacar':
        heroi.atacar(monstro)
    elif acao == 'poder':
        heroi.poder(monstro)
    else:
        heroi.saltar()

    if monstro.esta_vivo():
        if random.choice(['atacar', 'investida']) == 'atacar':
            monstro.atacar(heroi)
        else:
            monstro.investida(heroi)

vencedor = heroi if heroi.esta_vivo() else monstro
print(f'{vencedor.nome} venceu em {turnos} turnos')
