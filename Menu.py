import Forca
import Adivinhacao

def escolha():
    print("Escolha um jogo!\n")
    print("1 - Adivinhação  2 - Forca")
    escolha = int(input("Qual escolhe? "))

    if(escolha == 1):
        print("Escolheu o Jogo de Adivinhação!\n")
        Adivinhacao.jogar()
    elif(escolha == 2):
        print("Escolheu o Jogo da Forca!\n")
        Forca.jogar()


if(__name__ == "__main__"):
    escolha()
