from random import randint 
contador = -1
vitórias = 0
derrotas = 0
usuário = ''
while usuário != "PARAR":
    contador += 1
    print("Jogo de ímpar ou par.")
    print("Quando você quiser encerrar o jogo, digite 'parar' na parte de escolher '[P/I/]'.")
    usuário = str(input("Você deseja par ou impar? Digite sua escolha: '[P/I]'.\n")).strip().upper()
    
    if 'P' in usuário:
        if usuário == 'P':
            print("Você escolheu par.")
            numero_user = int(input("Digite seu número de 1 até 10.\n"))
            numero_pc = randint(0, 10)
            print(f"Computador: {numero_pc}.")
            total = numero_user + numero_pc
            if total % 2 == 0:
                vitórias += 1  
                print("Você ganhou!")
                print(f"Total = {total}")
            else:
                derrotas += 1
                print("Você perdeu.")
                print(f"Total = {total}")
    # impar abaixo
    elif 'I' in usuário:
        if usuário == 'I':
            print("Você escolheu ímpar.")
            numero_user = int(input("Digite seu número de 1 até 10\n"))
            numero_pc = randint(0, 10)
            print(f"Computador: {numero_pc}")
            total = numero_user + numero_pc
            if total % 2 == 0:
                derrotas += 1
                print("Você perdeu.")
                print(f"Total = {total}")
            else:
                vitórias += 1
                print("Você ganhou!")
                print(f"Total = {total}")
    else:
        print("Digite uma condição válida.")
        break

print(f"Você fez {contador} tentativas.")
print(f"Derrotas: {derrotas}.")
print(f"Vitórias: {vitórias}.")