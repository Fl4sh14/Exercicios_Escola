class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome # atributo
        self.idade = idade # atributo
        self.nota = nota # atributo
    def apresentar(self): # método que escreve no ecrã
        print(f"Olá, chamo-me {self.nome}, tenho {self.idade} anos "
        f"e a minha nota é {self.nota}.")
    def aprovado(self): # método que devolve um valor
        return self.nota >= 10
# Criar objetos (instâncias da classe)
marta = Aluno("Marta", 16, 15)
joao = Aluno("João", 17, 8)

marta.apresentar()
joao.apresentar()

print(marta.aprovado()) # True
print(joao.aprovado()) # False
