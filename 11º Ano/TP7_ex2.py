class Personagem:
    def __init__(self, nome, vida, forca):
        if forca < 0:
            print('A força não pode ser nagtiva!')
            forca = int(input('Escreve o valor da força: '))

        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, alvo):
        print(f'{self.nome} ataca {alvo.nome} ({self.forca} de dano)')
        alvo.receber_dano(self.forca)

    def receber_dano(self, valor):
        self.vida = max(0, self.vida - valor)
        print(f'{self.nome} ficou com {self.vida} de vida')

    def esta_vivo(self):
        return self.vida > 0


class Heroi(Personagem):
    def __init__(self, nome, vida, forca, nivel=1):
        super().__init__(nome, vida, forca)
        self.nivel = nivel

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 10
        self.forca += 2
        print(f'{self.nome} subiu para o nível {self.nivel}')


class Mago(Personagem):
    def __init__(self, nome, vida, forca, mana):
        super().__init__(nome, vida, forca)
        self.mana = mana

    def feitico(self, alvo):
        if self.mana < 10:
            print(f'{self.nome} não tem mana suficiente')
            return
        self.mana -= 10
        print(f'{self.nome} lança um feitiço a {alvo.nome} ({self.forca * 2} de dano)')
        alvo.receber_dano(self.forca * 2)


class Arqueiro(Personagem):
    def __init__(self, nome, vida, forca, flechas):
        super().__init__(nome, vida, forca)
        self.flechas = flechas

    def disparar(self, alvo):
        if self.flechas == 0:
            print(f'{self.nome} não tem flechas')
            return
        self.flechas -= 1
        print(f'{self.nome} dispara contra {alvo.nome} ({self.forca + 3} de dano)')
        alvo.receber_dano(self.forca + 3)

    def recarregar(self):
        self.flechas += 5
        print(f'{self.nome} recarregou ({self.flechas} flechas)')


class Monstro(Personagem):
    def __init__(self, nome, vida, forca, tipo):
        super().__init__(nome, vida, forca)
        self.tipo = tipo

    def rugir(self):
        print(f'{self.nome} ({self.tipo}) ruge!')
        self.forca * 2
        print('== A força do monstro multiplicou por 2 ==')

def titulo(texto):
    print(f'\n=== {texto} ===')


heroi = Heroi('Tenda', 100, 12)
mago = Mago('Pedro Lourenço', 70, 10, 100)
arqueiro = Arqueiro('Zezinho', 80, 9, 2)
monstro = Monstro('Policia', 150, 15, 'Brutamonte')

titulo('Ronda 1: o grupo ataca')
monstro.rugir()
heroi.atacar(monstro)
mago.feitico(monstro)
arqueiro.disparar(monstro)
arqueiro.disparar(monstro)
arqueiro.disparar(monstro)
arqueiro.recarregar()
arqueiro.disparar(monstro)
 
titulo('Ronda 2: o monstro contra-ataca')
monstro.atacar(heroi)
monstro.atacar(mago)
 
titulo('Ronda 3: o herói evolui')
heroi.subir_nivel()
 
titulo('Duelo final')
while monstro.esta_vivo() and heroi.esta_vivo():
    heroi.atacar(monstro)
    if monstro.esta_vivo():
        monstro.atacar(heroi)
        if monstro.vida < 20:
            monstro.rugir()
 
titulo('Resultado')
if heroi.esta_vivo():
    print(f'{heroi.nome} venceu!')
else:
    print(f'{monstro.nome} venceu!')
