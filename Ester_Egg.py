class PomoDeOuro:
    def __init__(self, linhas, colunas):
        self.posicao = (random.randint(0, linhas - 1), random.randint(0, colunas - 1))
        self.linhas = linhas
        self.colunas = colunas

    def mover(self):
        self.posicao = (random.randint(0, self.linhas - 1), random.randint(0, self.colunas - 1))

    def get_posicao(self):
        return self.posicao
