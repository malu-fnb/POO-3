class Aventureiro:
    def __init__(self, nome):
        self.nome = nome
        self.posicao_atual = (0, 0)
        self.tesouros_coletados = []
        self.vidas = 3

    def get_nome(self):
        return self.nome

    def get_posicao_atual(self):
        return self.posicao_atual

    def set_posicao_atual(self, posicao):
        self.posicao_atual = posicao

    def get_tesouros_coletados(self):
        return self.tesouros_coletados

    def mover(self, direcao, labirinto):
        linha, coluna = self.posicao_atual
        nova_linha, nova_coluna = linha, coluna

        if direcao == 'w':
            nova_linha = max(0, linha - 1)
        elif direcao == 's':
            nova_linha = min(labirinto.linhas - 1, linha + 1)
        elif direcao == 'a':
            nova_coluna = max(0, coluna - 1)
        elif direcao == 'd':
            nova_coluna = min(labirinto.colunas - 1, coluna + 1)
        
        if labirinto.estrutura[nova_linha][nova_coluna] != '-':
            self.posicao_atual = (nova_linha, nova_coluna)
            labirinto.verificar_armadilhas_proximas(self.posicao_atual)

    def coletar_tesouro(self, tesouro):
        self.tesouros_coletados.append(tesouro)

    def perder_vida(self):
        self.vidas -= 1

    def get_vidas(self):
        return self.vidas
