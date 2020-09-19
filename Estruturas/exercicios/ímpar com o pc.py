cont = -1
vi = 0
de= 0
user = ''
from random import randint 
while user != 'PARAR':
    cont += 1
    print("Jogo de par ou ímpar.\n")
    print("Quando você quiser encerrar o jogo, digite: 'parar' na parte de escolher [P/I].")
    user= str(input("Você deseja par ou ímpar? Digite sua escolha: [P/I]\n")).strip().upper()
    if 'P' in user:
        if user == 'P':
            print("Você escolheu par.")
            nu = int(input("Digite seu número de um à dez\n"))
            pc = randint(1, 10)
            print(f"Pc:{pc}.")
            re = nu + pc
            if re % 2 == 0:
                vi += 1
                print("Você ganhou!")
            else:
                de += 1
                print("Você perdeu.")
                print("Total = {}".format(re / 2))
    elif 'I' in user:            
        if user == 'I':
            print("Você escolheu ímpar.")
            nu = int(input("Digite seu número de um à dez\n"))
            pc = randint(1, 10)
            print(f"Pc:{pc}.")
            re = nu + pc
            if re % 2 == 0:
                vi += 1
                print("Você perdeu.")
                print("Total = {}".format(re / 2))
            else:
                de += 1
                print("Você ganhou!")
                print("Total = {}".format(re / 2))
        else:
            print("Digite uma condição válida.")
            break
    else:
        print("Digite uma condição válida.")
        break
print(f"Você fez {cont} tentativas.")
print(f"Derrotas: {de}.")
print(f"Vitórias: {vi}.")