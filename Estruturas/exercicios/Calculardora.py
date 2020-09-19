print("Bom dia!")
n1= float(input("Digite um número.\n"))
n2= float(input("Digite outro número.\n"))
opt = 0
while opt != 8:
    print('''O que pretende fazer com estes números?
    [1]- Somar;
    [2]- Subtrair;
    [3]- Multiplicar;
    [4]- Dividir;
    [5]- Potência;
    [6]- Descubra o maior deles;
    [7]- digite novos números;
    [8]- Para sair do programa.\n''')
    opt= str(input(">>>>>>>Digite sua opção.\n"))
    if opt == 1:
        oper= n1 + n2
        print("A soma de {} com {} é: {}.\n".format(n1, n2, oper))
    elif opt == 2:
        oper= n1 - n2
        print("A diferença de {} com {} é: {}.\n".format(n1, n2, oper))
    elif opt == 3:
        oper= n1 * n2
        print("O produto de {} com {} é: {}.\n".format(n1, n2, oper))
    elif opt == 4:
        oper= n1 / n2
        print("O quociente de {} com {} é: {}.\n".format(n1, n2, oper))
    elif opt == 5:
        oper= n1**n2
        print("A potência de {} com {} é: {}.\n".format(n1, n2, oper))
    elif opt == 6:
        if n1 > n2:
            print("O maior número é {} e o menor é {}.\n".format(n1, n2))
        else:
            print("O maior número é {} e o menor é {}.\n".format(n2, n1))
    elif opt == 7:
        n1= float(input("Digite um número.\n"))
        n2= float(input("Digite outro número.\n"))
    elif opt == 8:
        print("Volte sempre!\n")
        break
    else:
            print("Inválido\n")
            break