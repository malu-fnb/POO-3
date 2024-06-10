def pedra_papel_tesoura():
    clear_terminal()
    print("Você ficou sem energia\n")
    opcoes = ['j', 'k', 'p']
    escolha_maquina = random.choice(opcoes)
    escolha_jogador = input("Vamos jogar Pedra, Papel e Tesoura! Escolha: pedra(j), papel(k) ou tesoura(p): ").lower()

    while escolha_jogador not in opcoes:
        escolha_jogador = input("Escolha inválida. Tente novamente: pedra(j), papel(k) ou tesoura(p) ").lower()

    print(f"Máquina escolheu: {escolha_maquina}")

    if escolha_jogador == escolha_maquina:
        return "Empate"
    elif (escolha_jogador == 'j' and escolha_maquina == 'p') or \
         (escolha_jogador == 'k' and escolha_maquina == 'j') or \
         (escolha_jogador == 'p' and escolha_maquina == 'k'):
        return "Você ganhou"
    else:
        return "Você perdeu"
