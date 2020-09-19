from time import sleep


def maior(*num):
    cont = maior = 0
    print('-='*30)
    print("\nAnalisando os valores.")
    for valor in num:
        sleep(0.3)
        print(f"{valor} ", end='', flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor foi {maior}.")
    print('-='*30)


# programa principal
maior(1, 2, 2)