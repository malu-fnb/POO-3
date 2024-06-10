def main():
    print("Bem-vindo ao Labirinto!")
    print("Objetivo do Jogo: Navegue pelo labirinto, colete todos os tesouros e evite as armadilhas.")
    print("Regras:")
    print("1. Você começa com uma certa quantidade de energia, que diminui a cada movimento.")
    print("2. Quando a energia acabar, você jogará Pedra, Papel e Tesoura para recuperá-la.")
    print("3. Colete todos os tesouros (✧) para vencer o jogo.")
    print("4. Evite cair nas armadilhas, caso contrário, é Game Over.")
    print("5. Movimente-se usando 'w' (cima), 's' (baixo), 'a' (esquerda) e 'd' (direita).")
    print("6. Capture o Pomo de Ouro (@) para vencer o jogo imediatamente.")
    print("Boa sorte!\n")

    nome = input("Qual é o seu nome? ")

    nivel = input("Qual nível deseja jogar? (fácil(f), médio(m), difícil(d)): ").lower()
    while nivel not in ['f', 'm', 'd']:
        nivel = input("Por favor, escolha um nível válido (fácil(f), médio(m), difícil(d)): ").lower()

    if nivel == 'f':
        linhas, colunas, quantidade_tesouros, quantidade_perigos = 6, 6, 4, 2
        energia_inicial = 6
    elif nivel == 'm':
        linhas, colunas, quantidade_tesouros, quantidade_perigos = 8, 8, 6, 4
        energia_inicial = 8
    else:
        linhas, colunas, quantidade_tesouros, quantidade_perigos = 10, 10, 8, 6
        energia_inicial = 10

    labirinto = Labirinto(linhas, colunas)
    labirinto.gerar_labirinto(quantidade_tesouros, quantidade_perigos)
    
    aventureiro = Aventureiro(nome)
    energia = energia_inicial

    while True:
        proximidade_armadilha = labirinto.verificar_armadilhas_proximas(aventureiro.get_posicao_atual())

        print(f"\nMapa do Labirinto:")
        labirinto.exibir_mapa(aventureiro, energia, proximidade_armadilha)

        direcao = input(f"Para onde deseja se mover, {aventureiro.get_nome()}? (cima(w), baixo(s), esquerda(a), direita(d)): ").lower()
        while direcao not in ['w', 's', 'a', 'd']:
            direcao = input("Por favor, escolha uma direção válida (cima(w), baixo(s), esquerda(a), direita(d): ").lower()

        posicao_antiga = aventureiro.get_posicao_atual()
        aventureiro.mover(direcao, labirinto)
        nova_posicao = aventureiro.get_posicao_atual()

        if nova_posicao == labirinto.pomo_de_ouro.get_posicao():
            print(f"\nParabéns, {aventureiro.get_nome()}! Você capturou o Pomo de Ouro e venceu o jogo!")
            print("              $$$$$$$$      $$$$$$$$$              ")
            print("            $$$$$$$$$$$$   $$$$$$$  $$$$           ")
            print("           $$$$$$$$$$$$$$$$$$$$$$$$  $$$           ")
            print("           $$$$$$$$$$$$$$$$$$$$$$$$  $$$           ")
            print("           $$$$$$$$$$$$$$$$$$$$$$$$  $$$           ")
            print("            $$$$$$$$$$$$$$$$$$$$$$  $$$            ")
            print("              $$$$$$$$$$$$$$$$$$$$$$$              ")
            print("                 $$$$$$$$$$$$$$$$$                 ")
            print("                   $$$$$$$$$$$$$                   ")
            print("                      $$$$$$$                      ")
            print("                        $$$                        ")
            print("                         $                         ")    
            break

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
            print("Você caiu em uma armadilha!")
            aventureiro.perder_vida()
            if aventureiro.get_vidas() == 0:
                print("Você usou todas as suas vidas.")
                exit()

        energia -= 1

        if energia == 0:
            print(f"{aventureiro.get_nome()}, sua energia acabou! Vamos jogar Pedra, Papel e Tesoura para recuperar energia.")
            resultado = pedra_papel_tesoura()
            if resultado == "Você ganhou":
                print("Parabéns! Você recuperou 15 de energia!")
                energia += 10
            elif resultado == "Empate":
                print("Empate! Você recuperou 5 de energia!")
                energia += 5
            else:
                print("Você perdeu! Você recuperou 1 de energia.")
                energia += 1

        if not labirinto.tesouros:
            print(f"\nParabéns, {aventureiro.get_nome()}! Você coletou todos os tesouros e venceu o jogo!")
            print("              $$$$$$$$      $$$$$$$$$              ")
            print("            $$$$$$$$$$$$   $$$$$$$  $$$$           ")
            print("           $$$$$$$$$$$$$$$$$$$$$$$$  $$$           ")
            print("           $$$$$$$$$$$$$$$$$$$$$$$$  $$$           ")
            print("           $$$$$$$$$$$$$$$$$$$$$$$$  $$$           ")
            print("            $$$$$$$$$$$$$$$$$$$$$$  $$$            ")
            print("              $$$$$$$$$$$$$$$$$$$$$$$              ")
            print("                 $$$$$$$$$$$$$$$$$                 ")
            print("                   $$$$$$$$$$$$$                   ")
            print("                      $$$$$$$                      ")
            print("                        $$$                        ")
            print("                         $                         ")    
            break

        # Mover o Pomo de Ouro para uma nova posição aleatória
        labirinto.pomo_de_ouro.mover()

if __name__ == "__main__":
    main()
