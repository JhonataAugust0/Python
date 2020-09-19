def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :parâmetro n: número a ser calculado;
    :parâmetro show: (opicional) mostrar ou não a expressão;
    :return: o valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(f"{c}", end='')
            if c > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
        f *= c
    return f


# principal
print(f"{fatorial(5, show=True)}")
help(fatorial)