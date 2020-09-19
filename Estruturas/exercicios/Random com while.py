from random import randint
pc = randint(1, 10) 
acertou = False
palpites = 0
while not acertou:
    print("Tente advinhar o número em que o computador pensou (de 1 à 10).")
    u= int(input("Digite um número.\n"))
    if u > 0 and u < 11:
        palpites+= 1
        if u == pc:
            acertou == True 
            print("parabéns você acertou, o número que o computador pensou foi {}. Você precisou de {} tentativas.".format(pc, palpites))
            break
        else:
            print("Tente novamente.\n")
    else:
        print("Inválido\n")
        break