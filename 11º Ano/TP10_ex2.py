from abc import ABC, abstractmethod


class Subscricao(ABC):
    def __init__(self, titular, mensalidade_base):
        self.titular = titular
        self.__mensalidade_base = mensalidade_base

    def get_mensalidade_base(self):
        return self.__mensalidade_base

    def set_mensalidade_base(self, valor):
        if valor >= 5.00:
            self.__mensalidade_base = valor
        else:
            print('Erro: A mensalidade não pode ser inferior a 5€.')

    @abstractmethod
    def calcular_valor_final(self):
        pass


class PlanoEstudante(Subscricao):
    def __init__(self, titular, mensalidade_base, escola):
        super().__init__(titular, mensalidade_base)
        self.escola = escola

    def calcular_valor_final(self):
        return self.get_mensalidade_base() * 0.5


class PlanoFamiliar(Subscricao):
    def __init__(self, titular, mensalidade_base, num_membros):
        super().__init__(titular, mensalidade_base)
        self.num_membros = num_membros

    def calcular_valor_final(self):
        return self.get_mensalidade_base() + (3.50 * self.num_membros)



estudante = PlanoEstudante('João', 10.00, 'Escola Boa Nova')
familiar = PlanoFamiliar('Pedro', 15.00, 4)


estudante.set_mensalidade_base(2.00)


print('Plano estudante:', estudante.calcular_valor_final(), '€')
print('Plano familiar:', familiar.calcular_valor_final(), '€')