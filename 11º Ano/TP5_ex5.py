class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def emprestar(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                return True
        return False

    def listar_disponiveis(self):
        for livro in self.livros:
            if livro.disponivel:
                print(livro.titulo)
                

# teste
b = Biblioteca()
b.adicionar(Livro('Os Maias', 'Eça de Queirós'))
b.adicionar(Livro('Mensagem', 'Fernando Pessoa'))
b.adicionar(Livro('Memorial do Convento', 'José Saramago'))

print(b.emprestar('Os Maias'))
b.listar_disponiveis()          
print(b.emprestar('Os Maias'))
