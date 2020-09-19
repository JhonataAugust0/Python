print("Digite um número para saber a sua tabuada, para parar digite qualquer número negativo.\n")
while True:
    n= float(input("Quer saber a tabuáda de qual valor?"))
    ate = int(input(f"Tabuada de {n} até quanto?\n"))
    for c in range(1, ate):
        print(f"{n} x {ate} = {n*ate}\n")
    encerrar = str(input("Gostaria de encerrar o programa? [S/N]")).strip().upper()[0]
    if encerrar == 'S':
        break
    else:
        pass