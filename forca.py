import random

def jogar():

    imprime_mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)


    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas [index] = letra
                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você adivinhou a palavra!")
    else:
        print("Você não adivinhou a palavra!")
    print("Fim de jogo!")


def imprime_mensagem_de_abertura():
    print("*****************************")
    print(" Bem vindo ao jogo de Forca!")
    print("*****************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r") #ABRE O ARQUIVO DAS PALAVRAS
    palavras = [] #TRANSFORMA AS PALAVRAS EM LIST

    for linha in arquivo:
        linha = linha.strip() #TIRA OS ESPAÇOS ENTRE AS LINHA
        palavras.append(linha) #ADICIONA UM LINHA NAS PALAVRAS

    arquivo.close()

    numero = random.randrange(0, len(palavras)) #BUSCA UMA PALAVRA ALEATORIA ENTRE TODAS DO ARQUIVO
    palavra_secreta = palavras[numero].upper() #DIZ QUE AS PALAVRAS ALEATORIAS GERADAS FICARAM EM MAIUSCULO
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


if (__name__ == "__main__"):
    jogar()