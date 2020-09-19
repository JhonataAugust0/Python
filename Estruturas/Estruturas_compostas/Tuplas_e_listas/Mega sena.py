from random import randint
from time import sleep
lista = list()
jogos = list()
cont = 0
print('                  MEGA SENA          ')
quant = int(input("Quantos jogos você quer que eu sorteie?\n"))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f"Sorteando {quant} jogos!")
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}.\n")
    sleep(1.5)
print("Boa sorte!")
# Aqui realizamos um algoritmo que sorteia números randômicos para jogar na mega sena.