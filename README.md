# POO-3

# Participantes:


Malu de Faria Neves Bezerra

Pedro Marques Bezerra dos Santos

Renan Ribeiro Duarte

Pedro Henrique Afonso dos Santos


# Labirinto do Aventureiro

## Descrição

Este é um jogo de labirinto onde o jogador controla um aventureiro que deve coletar todos os tesouros enquanto evita armadilhas. O jogo oferece diferentes níveis de dificuldade e inclui um sistema de energia que se esgota a cada movimento. Quando a energia se esgota, o jogador joga Pedra, Papel e Tesoura contra a máquina para recuperar energia.

## Requisitos do Jogo

O jogo é composto por quatro classes principais:
- **Aventureiro**: Representa o jogador no jogo.
- **Tesouro**: Representa os tesouros que podem ser coletados no jogo.
- **Perigo**: Representa as armadilhas que o jogador deve evitar.
- **Labirinto**: Representa a estrutura do labirinto e contém a lógica principal do jogo.

### Classes e Atributos

#### Aventureiro
- **Atributos**:
  - `nome`: Nome do jogador.
  - `posicao_atual`: Posição atual do jogador no labirinto.
  - `tesouros_coletados`: Lista de tesouros coletados pelo jogador.
- **Métodos**:
  - Getters e setters para os atributos.
  - `mover(direcao, labirinto)`: Move o jogador na direção especificada.
  - `coletar_tesouro(tesouro)`: Adiciona o tesouro à lista de tesouros coletados.

#### Tesouro
- **Atributos**:
  - `nome`: Nome do tesouro.
  - `posicao`: Posição do tesouro no labirinto.
  - `valor`: Valor em pontos do tesouro.
- **Métodos**:
  - Getters e setters para os atributos.

#### Perigo
- **Atributos**:
  - `posicao`: Posição da armadilha no labirinto.
  - `dano`: Dano potencial da armadilha.
- **Métodos**:
  - Getters e setters para os atributos.

#### Labirinto
- **Atributos**:
  - `linhas`: Número de linhas do labirinto.
  - `colunas`: Número de colunas do labirinto.
  - `estrutura`: Estrutura do labirinto (lista de listas).
  - `tesouros`: Lista de tesouros no labirinto.
  - `perigos`: Lista de armadilhas no labirinto.
- **Métodos**:
  - `gerar_labirinto(quantidade_tesouros, quantidade_perigos)`: Gera o labirinto com tesouros e armadilhas.
  - `adicionar_tesouro(tesouro)`: Adiciona um tesouro ao labirinto.
  - `remover_tesouro(tesouro)`: Remove um tesouro do labirinto.
  - `adicionar_perigo(perigo)`: Adiciona uma armadilha ao labirinto.
  - `remover_perigo(perigo)`: Remove uma armadilha do labirinto.
  - `exibir_mapa(aventureiro)`: Exibe o mapa do labirinto.

## Como Jogar

1. **Início do Jogo**: Ao iniciar o jogo, você será solicitado a inserir seu nome e escolher um nível de dificuldade: fácil, médio ou difícil.
2. **Movimentação**: Use as teclas `w`, `s`, `a` e `d` para mover o aventureiro pelo labirinto.
3. **Energia**: Cada movimento consome energia. Quando a energia se esgota, você joga Pedra, Papel e Tesoura para recuperar energia.
4. **Objetivo**: Coletar todos os tesouros (T) e evitar as armadilhas (*). Você vence ao coletar todos os tesouros.

## Exemplo de Execução

```
Bem-vindo ao Labirinto!
Objetivo do Jogo: Navegue pelo labirinto, colete todos os tesouros e evite as armadilhas.
Regras:
1. Você começa com uma certa quantidade de energia, que diminui a cada movimento.
2. Quando a energia acabar, você jogará Pedra, Papel e Tesoura para recuperá-la.
3. Colete todos os tesouros (✧) para vencer o jogo.
4. Evite cair nas armadilhas (۝), caso contrário, é Game Over.
5. Movimente-se usando 'w' (cima), 's' (baixo), 'a' (esquerda) e 'd' (direita).
Boa sorte!

Qual é o seu nome? Jogador1
Qual nível deseja jogar? (fácil(f), médio(m), difícil(d)): f
Mapa do Labirinto (Energia: 10):
嘿 * * * * * 
* * * * * ✧ 
* * * * ۝ ͒ * 
* * * * * * 
* * ۝ ͒ * * * 
* * * * * ✧ 

Para onde deseja se mover, Jogador1? (cima(w), baixo(s), esquerda(a), direita(d)): d
```

## Código Fonte

```python
import random

class Aventureiro:
    def __init__(self, nome):
        self.nome = nome
        self.posicao_atual = (0, 0)
        self.tesouros_coletados = []

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
        if direcao == 'w':
            nova_linha = max(0, linha - 1)
            nova_coluna = coluna
        elif direcao == 's':
            nova_linha = min(labirinto.linhas - 1, linha + 1)
            nova_coluna = coluna
        elif direcao == 'a':
            nova_linha = linha
            nova_coluna = max(0, coluna - 1)
        elif direcao == 'd':
            nova_linha = linha
            nova_coluna = min(labirinto.colunas - 1, coluna + 1)
        
        self.posicao_atual = (nova_linha, nova_coluna)

    def coletar_tesouro(self, tesouro):
        self.tesouros_coletados.append(tesouro)


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


class Perigo:
    def __init__(self, posicao, dano):
        self.posicao = posicao
        self.dano = dano

    def get_posicao(self):
        return self.posicao

    def get_dano(self):
        return self.dano


class Labirinto:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.estrutura = [['.' for _ in range(colunas)] for _ in range(linhas)]
        self.tesouros = []
        self.perigos = []

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
        self.estrutura[linha][coluna] = '*'

    def remover_perigo(self, perigo):
        self.perigos.remove(perigo)
        linha, coluna = perigo.get_posicao()
        self.estrutura[linha][coluna] = '.'

    def exibir_mapa(self, aventureiro):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if (i, j) == aventureiro.get_posicao_atual():
                    print

('A', end=' ')
                else:
                    print(self.estrutura[i][j], end=' ')
            print()

def pedra_papel_tesoura():
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_maquina = random.choice(opcoes)
    escolha_jogador = input("Vamos jogar Pedra, Papel e Tesoura! Escolha: pedra, papel ou tesoura: ").lower()

    while escolha_jogador not in opcoes:
        escolha_jogador = input("Escolha inválida. Tente novamente: pedra, papel ou tesoura: ").lower()

    print(f"Máquina escolheu: {escolha_maquina}")

    if escolha_jogador == escolha_maquina:
        return "Empate"
    elif (escolha_jogador == 'pedra' and escolha_maquina == 'tesoura') or \
         (escolha_jogador == 'papel' and escolha_maquina == 'pedra') or \
         (escolha_jogador == 'tesoura' and escolha_maquina == 'papel'):
        return "Você ganhou"
    else:
        return "Você perdeu"

def main():
    print("Bem-vindo ao Labirinto!")
    print("Objetivo do Jogo: Navegue pelo labirinto, colete todos os tesouros e evite as armadilhas.")
    print("Regras:")
    print("1. Você começa com uma certa quantidade de energia, que diminui a cada movimento.")
    print("2. Quando a energia acabar, você jogará Pedra, Papel e Tesoura para recuperá-la.")
    print("3. Colete todos os tesouros (T) para vencer o jogo.")
    print("4. Evite cair nas armadilhas (*), caso contrário, é Game Over.")
    print("5. Movimente-se usando 'w' (cima), 's' (baixo), 'a' (esquerda) e 'd' (direita).")
    print("Boa sorte!\n")

    nome = input("Qual é o seu nome? ")
    nivel = input("Qual nível deseja jogar? (fácil(f), médio(m), difícil(d)): ").lower()
    while nivel not in ['f', 'm', 'd']:
        nivel = input("Por favor, escolha um nível válido (fácil(f), médio(m), difícil(d)): ").lower()

    if nivel == 'f':
        linhas, colunas, quantidade_tesouros, quantidade_perigos = 6, 6, 2, 2
        energia_inicial = 10
    elif nivel == 'm':
        linhas, colunas, quantidade_tesouros, quantidade_perigos = 8, 8, 4, 4
        energia_inicial = 8
    else:
        linhas, colunas, quantidade_tesouros, quantidade_perigos = 10, 10, 6, 6
        energia_inicial = 6

    labirinto = Labirinto(linhas, colunas)
    labirinto.gerar_labirinto(quantidade_tesouros, quantidade_perigos)
    aventureiro = Aventureiro(nome)

    energia = energia_inicial

    while True:
        print(f"\nMapa do Labirinto (Energia: {energia}):")
        labirinto.exibir_mapa(aventureiro)

        direcao = input(f"Para onde deseja se mover, {aventureiro.get_nome()}? (cima(w), baixo(s), esquerda(a), direita(d)): ").lower()
        while direcao not in ['w', 's', 'a', 'd']:
            direcao = input("Por favor, escolha uma direção válida (cima(w), baixo(s), esquerda(a), direita(d)): ").lower()

        aventureiro.mover(direcao, labirinto)

        nova_posicao = aventureiro.get_posicao_atual()

        tesouro_encontrado = None
        for tesouro in labirinto.tesouros:
            if tesouro.get_posicao() == nova_posicao:
                tesouro_encontrado = tesouro
                break
        if tesouro_encontrado:
            aventureiro.coletar_tesouro(tesouro_encontrado)
            labirinto.remover_tesouro(tesouro_encontrado)
            print("Você encontrou um tesouro!")

        perigo_encontrado = None
        for perigo in labirinto.perigos:
            if perigo.get_posicao() == nova_posicao:
                perigo_encontrado = perigo
                break
        if perigo_encontrado:
            print("Você caiu em uma armadilha! Game over!")
            exit()

        energia -= 1

        if energia == 0:
            print(f"{aventureiro.get_nome()}, sua energia acabou! Vamos jogar Pedra, Papel e Tesoura para recuperar energia.")
            resultado = pedra_papel_tesoura()
            if resultado == "Você ganhou":
                print("Parabéns! Você recuperou 15 de energia!")
                energia += 15
            elif resultado == "Empate":
                print("Empate! Você recuperou 5 de energia!")
                energia += 5
            else:
                print("Você perdeu! Você recuperou 1 de energia.")
                energia += 1

        if not labirinto.tesouros:
            print(f"\nParabéns, {aventureiro.get_nome()}! Você coletou todos os tesouros e venceu o jogo!")
            break

if __name__ == "__main__":
    main()
```

## Como Executar

1. **Clone o Repositório**:
   ```bash
   git clone <URL do repositório>
   cd <diretório do repositório>
   ```

2. **Execute o Jogo**:
   ```bash
   python <nome_do_arquivo>.py
   ```

Divirta-se jogando o Labirinto do Aventureiro!
