class Conteudo:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano
        self.notas = []

    def avaliar(self, nota):
        if 1 <= nota <= 5:
            self.notas.append(nota)

    def media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def mostrar_ficha(self):
        print(f'{self.titulo} ({self.ano}) - média: {self.media():.1f}')


class Filme(Conteudo):
    def __init__(self, titulo, ano, duracao_min, realizador):
        super().__init__(titulo, ano)
        self.duracao_min = duracao_min
        self.realizador = realizador

    def duracao_em_horas(self):
        return self.duracao_min / 60


class Serie(Conteudo):
    def __init__(self, titulo, ano, temporadas, episodios_por_temporada):
        super().__init__(titulo, ano)
        self.temporadas = temporadas
        self.episodios_por_temporada = episodios_por_temporada

    def total_episodios(self):
        return self.temporadas * self.episodios_por_temporada


# Programa principal
filme = Filme('Interstellar', 2014, 169, 'Christopher Nolan')
serie = Serie('Dark', 2017, 3, 8)
filme.avaliar(5)
filme.avaliar(4)
serie.avaliar(5)
filme.mostrar_ficha()
serie.mostrar_ficha()
print(filme.duracao_em_horas())
print(serie.total_episodios())



# o que eu acho que vai aparecer no ecrã:
#     Interstellar (2014) - média: 4.5
#     Dark (2017) - média: 5.0
#     2.81
#     24

# o que apareceu:
    # Interstellar (2014) - média: 4.5
    # Dark (2017) - média: 5.0
    # 2.816666666666667
    # 24
