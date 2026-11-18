from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, matricula):
        self.matricula = matricula
        self._carga_atual = 0

    def carregar(self, peso_kg):
        if self._carga_atual + peso_kg <= 500:
            self._carga_atual += peso_kg
            print('Carga adicionada.')
        else:
            print('Erro: Limite de carga ultrapassado.')

    def get_carga_atual(self):
        return self._carga_atual

    @abstractmethod
    def calcular_custo_entrega(self, distancia_km):
        pass


class BicicletaCarga(Transporte):
    def calcular_custo_entrega(self, distancia_km):
        return distancia_km * 0.50


class CarrinhaEletrica(Transporte):
    def __init__(self, matricula, autonomia_km):
        super().__init__(matricula)
        self.autonomia_km = autonomia_km

    def calcular_custo_entrega(self, distancia_km):
        return 4.00 + (distancia_km * 0.25)


class DroneEntrega(Transporte):
    def __init__(self, matricula, altitude_maxima):
        super().__init__(matricula)
        self.altitude_maxima = altitude_maxima

    def calcular_custo_entrega(self, distancia_km):
        custo = distancia_km * 1.20

        if self._carga_atual > 5:
            custo += 5.00

        return custo



bicicleta = BicicletaCarga('AA-00-AA')
carrinha = CarrinhaEletrica('BB-00-BB', 300)
drone = DroneEntrega('CC-00-CC', 100)

frota = [bicicleta, carrinha, drone]

bicicleta.carregar(10)
carrinha.carregar(200)
drone.carregar(8)

for transporte in frota:
    custo = transporte.calcular_custo_entrega(12)

    print('Matrícula:', transporte.matricula)
    print('Carga:', transporte.get_carga_atual(), 'kg')
    print('Custo da entrega:', custo, '€')
    print('----------------------')