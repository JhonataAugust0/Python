num = list()
pares = list()
impares = list()
while True:
    num.append(int(input("Digite um valor.\n")))
    resp = str(input("Quer continuar?\n"))
    if resp in 'Nn':
        break
    else:
        for i, v in enumerate(num):
            if v % 2 == 0:
                pares.append(v)
            elif v % 2 == 1:      
                impares.append(v)
print(f"Você digitou {len(num)} valores. \n")
print(f"Os valores digitados foram {num}.\n")
print(f"a lista de ímpares é {impares}.\n")
print(f"a lista de pares é {pares}.\n")
# Aqui temos um algoritmo que também coleta números e os
# analiza, nos mostrando a quantidade de valores digitados
# e quais são os pares e ímpares 



