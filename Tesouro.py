class Tesouro:
    def __init__(self, nome, posicao, valor):
        self.nome = nome
        self.posicao = posicao
        self.valor = valor

    def get_nome(self):
        return self.nome

    def get_posicao(self):
        return self.posicao

    def get_valor(self):
        return self.valor
