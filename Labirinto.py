class Labirinto:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.estrutura = [['.' for _ in range(colunas)] for _ in range(linhas)]
        self.tesouros = []
        self.perigos = []
        self.pomo_de_ouro = PomoDeOuro(linhas, colunas)

    def gerar_labirinto(self, quantidade_tesouros, quantidade_perigos):
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
        self.estrutura[linha][coluna] = '.'  # Esconder armadilhas

    def remover_perigo(self, perigo):
        self.perigos.remove(perigo)
        linha, coluna = perigo.get_posicao()
        self.estrutura[linha][coluna] = '.'

    def exibir_mapa(self, aventureiro, energia, proximidade_armadilha):
        clear_terminal()  # Limpa o terminal antes de exibir o mapa
        print(f"Energia: {energia}, Vidas: {aventureiro.get_vidas()}, {proximidade_armadilha}")
        for i in range(self.linhas):
            for j in range(self.colunas):
                if (i, j) == aventureiro.get_posicao_atual():
                    print('嘿', end=' ')  # Representa o aventureiro com '嘿'
                elif (i, j) == self.pomo_de_ouro.get_posicao():
                    print('@', end=' ')  # Representa o Pomo de Ouro com '@'
                elif self.estrutura[i][j] == 'T':
                    print('✧', end=' ')  # Representa os tesouros com '✧'
                elif (i, j) in [p.get_posicao() for p in self.perigos]:
                    print('A', end=' ')  # Representa as armadilhas com 'A'
                else:
                    print('.', end=' ')  # Representa células vazias com '.'
            print()

    def verificar_armadilhas_proximas(self, posicao):
        linha, coluna = posicao
        proximas_posicoes = [
            (linha - 1, coluna), (linha + 1, coluna),
            (linha, coluna - 1), (linha, coluna + 1)
        ]
        for pos in proximas_posicoes:
            if 0 <= pos[0] < self.linhas and 0 <= pos[1] < self.colunas:
                if pos in [p.get_posicao() for p in self.perigos]:
                    return "Cuidado, armadilha está próxima!"
        return "Você está seguro."
