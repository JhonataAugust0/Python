n = float(input("Digite um número para calcular seu fatorial.\n"))
c = n
f = 1
while c > 0:
    print(f"{c}", end='')
    if c > 1:
        print(" x ", end="")
    else: 
        print(" = ", end="")
    f = (f * c)
    c -= 1
print(f"O fatorial de {n} é {f}")