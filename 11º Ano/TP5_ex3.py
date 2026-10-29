class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def levantar(self, valor):
        retirar = 0 < valor <= self.saldo
        if retirar:
            self.saldo -= valor
        return retirar

conta = ContaBancaria('Ana')
conta.depositar(100)
print('Saldo:', conta.saldo)

for v in (30, 500):
    if conta.levantar(v):
        print(f'Levantaste {v}€')
        print('Saldo:', conta.saldo)
    else:
        print(f'Não foi possível levantar {v}€ (saldo insuficiente)')

print('Saldo:', conta.saldo)
