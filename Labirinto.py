class Labirinto:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.estrutura = [['.' for _ in range(colunas)] for _ in range(linhas)]
        self.tesouros = []
        self.perigos = []
        self.paredes = []

    def gerar_labirinto(self, quantidade_tesouros, quantidade_perigos, quantidade_paredes):
        for _ in range(quantidade_tesouros):
            while True:
                linha = random.randint(0, self.linhas - 1)
                coluna = random.randint(0, self.colunas - 1)
                if (linha, coluna) != (0, 0) and self.estrutura[linha][coluna] == '.':
                    tesouro = Tesouro("Tesouro", (linha, coluna), 10)
                    self.adicionar_tesouro(tesouro)
                    break

        for _ in range(quantidade_perigos):
            while True:
                linha = random.randint(0, self.linhas - 1)
                coluna = random.randint(0, self.colunas - 1)
                if (linha, coluna) != (0, 0) and self.estrutura[linha][coluna] == '.':
                    perigo = Perigo((linha, coluna), 5)
                    self.adicionar_perigo(perigo)
                    break

        for _ in range(quantidade_paredes):
            while True:
                linha = random.randint(0, self.linhas - 1)
                coluna = random.randint(0, self.colunas - 1)
                if (linha, coluna) != (0, 0) and self.estrutura[linha][coluna] == '.':
                    self.adicionar_parede((linha, coluna))
                    break

    def adicionar_tesouro(self, tesouro):
        self.tesouros.append(tesouro)
        linha, coluna = tesouro.get_posicao()
        self.estrutura[linha][coluna] = 'T'

    def remover_tesouro(self, tesouro):
        self.tesouros.remove(tesouro)
        linha, coluna = tesouro.get_posicao()
        self.estrutura[linha][coluna] = '.'

    def adicionar_perigo(self, perigo):
        self.perigos.append(perigo)
        linha, coluna = perigo.get_posicao()
        self.estrutura[linha][coluna] = '*'

    def remover_perigo(self, perigo):
        self.perigos.remove(perigo)
        linha, coluna = perigo.get_posicao()
        self.estrutura[linha][coluna] = '.'

    def adicionar_parede(self, posicao):
        self.paredes.append(posicao)
        linha, coluna = posicao
        self.estrutura[linha][coluna] = '-'

    def exibir_mapa(self, aventureiro):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if (i, j) == aventureiro.get_posicao_atual():
                    print('嘿', end=' ')  # Representa o aventureiro com '嘿'
                elif self.estrutura[i][j] == 'T':
                    print('✧', end=' ')  # Representa os tesouros com '✧'
                elif self.estrutura[i][j] == '*':
                    print('۝', end=' ')  # Representa as armadilhas com '۝'
                elif self.estrutura[i][j] == '-':
                    print('-', end=' ')  # Representa as paredes com '-'
                else:
                    print('*', end=' ')  # Representa células vazias com '*'
            print()
