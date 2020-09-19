def leia_int(msg):
    """
    -> Essa função tem como parâmetro único o 'msg',
    ele será uma input, e o intuito da função é testar
    se a input é númerica, caso veraddeiro, ela conver-
    terá a input para float, e como a input tem que ser 
    numérica, enquanto um número não for digitado, o ci-
    clo não se encerrará.
    """
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mErro, digite um número inteiro válido.\033[m")
        if ok == True:
            break
    return valor


# principal:
n = leia_int("Digite um número: ")
print(f"Vocẽ acabou de digitar o número {n}.")
