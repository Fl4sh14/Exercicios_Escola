class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def apresentar(self):
        return self.nome

    def calcular_salario(self):
        return self.salario_base

    def mostrar_recibo(self):
        print(self.apresentar())
        print(f'Salário a receber: {self.calcular_salario():.2f} €')


class Gerente(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
        self.equipa = []

    def adicionar_membro(self, func):
        self.equipa.append(func)

    def apresentar(self):
        return super().apresentar() + f' (equipa de {len(self.equipa)})'

    def calcular_salario(self):
        return super().calcular_salario() + len(self.equipa) * 100


class Programador(Funcionario):
    def __init__(self, nome, salario_base, linguagem):
        super().__init__(nome, salario_base)
        self.linguagem = linguagem
        self.horas_extra = 0

    def registar_horas(self, h):
        self.horas_extra += h

    def calcular_salario(self):
        return super().calcular_salario() + self.horas_extra * 15


class Estagiario(Funcionario):
    def __init__(self, nome, salario_base, escola):
        super().__init__(nome, salario_base)
        self.escola = escola

    def calcular_salario(self):
        return self.salario_base * 0.6


class Diretor(Gerente):
    def __init__(self, nome, salario_base, departamento):
        super().__init__(nome, salario_base)
        self.departamento = departamento

    def calcular_salario(self):
        return super().calcular_salario() + 1000

# programa principal

polonia = Programador('Polonia', 1500, 'Python')
polonia.registar_horas(10)

marcelo = Estagiario('Marcelo', 800, 'ESTG')

ana = Gerente('Ana', 2000)
ana.adicionar_membro(polonia)
ana.adicionar_membro(marcelo)

ze = Diretor('Ze', 3000, 'Tecnologia')
ze.adicionar_membro(ana)


colaboradores = [polonia, marcelo, ana, ze]


total = 0

for funcionario in colaboradores:
    funcionario.mostrar_recibo()
    total += funcionario.calcular_salario()

print('-------------------------')
print(f'Total da folha salarial: {total:.2f} €')
