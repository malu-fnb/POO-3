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