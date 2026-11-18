class Robo:
    def __init__(self, identificador):
        self.__identificador = identificador
        self.__nivel_bateria = 100
        self.__estado = 'inativo'

    def carregar_bateria(self):
        self.__nivel_bateria = 100

    def gastar_bateria(self, valor):
        self.__nivel_bateria -= valor
        self.__estado = 'em missao'

    def get_info(self):
        return f'{self.__identificador} | bateria: {self.__nivel_bateria}% | estado: {self.__estado}'

    def executar_missao(self):
        pass


class RoboCombate(Robo):
    def __init__(self, identificador, poder_fogo):
        super().__init__(identificador)
        self.__poder_fogo = poder_fogo

    def executar_missao(self):
        self.gastar_bateria(40)
        print(f'Defesa tatica com poder de fogo {self.__poder_fogo}')


class RoboRecolha(Robo):
    def __init__(self, identificador, capacidade_carga):
        super().__init__(identificador)
        self.__capacidade_carga = capacidade_carga

    def executar_missao(self):
        self.gastar_bateria(15)
        print(f'A minerar recursos (carga max: {self.__capacidade_carga} kg)')


def testar_missao(robo):
    robo.executar_missao()
    print(robo.get_info())


testar_missao(RoboCombate('RC-01', 80))
testar_missao(RoboRecolha('RR-01', 250))
