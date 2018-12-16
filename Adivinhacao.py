import random

def jogar():
    print("Bem Vindo\n")
    numero = random.randrange(1, 101)
    tentativa = 0
    erro = 0
    pontos = 500

    print("Escolhe a dificuldade.")
    print("1 - Fácil  2 - Médio  3 - Difícil")
    nivel = int(input("Escolhe qual? "))
    if(nivel == 1):
        tentativa = 20
    elif(nivel == 2):
        tentativa = 10
    else:
        tentativa = 5
    print("Você tem {} chances para acertar, boa sorte!".format(tentativa))
    for rodada in range(1, tentativa + 1):
        print("\nRodada {} de {}".format(rodada, tentativa))
        chute = int(input("Chuta um número de 1 a 100: "))

        if(chute < 1 or chute > 100):
            print("É de 1 e 100!")
            continue
        certo = chute == numero
        maior = chute > numero
        menor = chute < numero

        if(certo):
            print("Ah mizeravi, acertou! Fez {} pontos!\n".format(pontos))
            break
        else:
            if(maior):
                print("Eeeerooow! Chutou pra cima!\n")
            elif(menor):
                print("Eeeerooow! Chutou pra baixo!\n")
            perda = abs(numero - chute)
            pontos = pontos - perda
            erro = erro + 1
    if(erro == tentativa):
        print("Você não tem mais chances! Sua pontuação foi {}".format(pontos))
        print("O numero era {}".format(numero))
    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()