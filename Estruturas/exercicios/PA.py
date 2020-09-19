print("Gerador PA\n")
pri= int(input("Primeiro termo.\n"))
raz= int(input("Razão PA.\n"))
cont = 1
termo= pri
v= int(input("Quantas vezes quer calcular?\n"))
while cont <= v:
    print("{}¬".format(termo), end='')
    termo += raz
    cont+=1