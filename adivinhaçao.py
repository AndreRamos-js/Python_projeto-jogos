def jogar():
    print("*****************************")
    print(" Bem vindo ao jogo de Adivinhação!")
    print("*****************************")

    import random
    numero_secreto = random.randrange(1, 101)
    total_de_rodadas = 0
    pontos = 1000

    print("Niveis de dificuldade:")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Escolha o seu nível de dificuldade: "))

    if(nivel == 1):
        total_de_rodadas = 20
    elif(nivel == 2):
        total_de_rodadas = 10
    else:
        total_de_rodadas = 5

    for rodada in range(1, total_de_rodadas + 1):
        print("Tentativa {} dê {}".format(rodada, total_de_rodadas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou:", chute_str)
        chute = int(chute_str)

        if(chute < 1  or chute > 100):
            print("Você deve escolher um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim de jogo!")
if (__name__ == "__main__"):
    jogar()
