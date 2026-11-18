from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, nome, preco_base, stock):
        self.nome = nome
        self.__preco_base = preco_base
        self.__stock = stock

    def get_preco_base(self):
        return self.__preco_base

    def set_preco_base(self, valor):
        if valor > 0:
            self.__preco_base = valor
        else:
            print('Erro: O preço tem de ser superior a zero.')

    def get_stock(self):
        return self.__stock

    def set_stock(self, valor):
        if valor >= 0:
            self.__stock = valor
        else:
            print('Erro: O stock não pode ser negativo.')

    def reduzir_stock(self, quantidade):
        if quantidade <= self.__stock and quantidade > 0:
            self.__stock -= quantidade
            return True
        else:
            return False

    @abstractmethod
    def calcular_preco_com_iva(self):   
        pass


class EquipamentoInformatico(Produto):
    def __init__(self, nome, preco_base, stock, garantia_meses):
        super().__init__(nome, preco_base, stock)
        self.garantia_meses = garantia_meses

    def calcular_preco_com_iva(self):
        return self.get_preco_base() * 1.23


class LivroTecnico(Produto):
    def __init__(self, nome, preco_base, stock, autor):
        super().__init__(nome, preco_base, stock)
        self.autor = autor

    def calcular_preco_com_iva(self):
        return self.get_preco_base() * 1.06


class CarrinhoCompras:
    def __init__(self):
        self.__itens = []

    def adicionar_produto(self, produto, quantidade):
        if produto.reduzir_stock(quantidade):
            self.__itens.append((produto, quantidade))
            print(produto.nome, 'adicionado ao carrinho.')
        else:
            print('Stock insuficiente para', produto.nome)

    def fechar_compra(self):
        total = 0

        print('\n------- TALÃO -------')

        for produto, quantidade in self.__itens:
            preco = produto.calcular_preco_com_iva()
            subtotal = preco * quantidade

            print(produto.nome)
            print('Quantidade:', quantidade)
            print('Preço unitário:', round(preco, 2), '€')
            print('Subtotal:', round(subtotal, 2), '€')

            total += subtotal

        print('---------------------')
        print('Total final a pagar:', round(total, 2), '€')



computador = EquipamentoInformatico('Computador', 800, 5, 24)
rato = EquipamentoInformatico('Rato', 20, 3, 12)
livro = LivroTecnico('Python', 30, 10, 'João Silva')

carrinho = CarrinhoCompras()

carrinho.adicionar_produto(computador, 2)
carrinho.adicionar_produto(rato, 5)  
carrinho.adicionar_produto(livro, 3)

carrinho.fechar_compra()