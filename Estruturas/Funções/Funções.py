def mostralinha():
    print('-='*30)
# mostralinha()


# def mensagem(msg):
# mostralinha()
# print(msg)
# mostralinha()
#
# mensagem('BOM DIA')

# def título(txt):
#     mostralinha()
#     print(txt)
#     mostralinha()

# título("A minha alma")
# título("Está armada")
# título("Para a cara do sossego")


# def soma(a, b):
#     c = a + b
#     print(f"A VARIÁVEL 'A' VALE ={a} E 'B' VALE = {b}")
#     print(f"A soma entre {a} e {b} vale {c}")


# #Principal
# soma(4,5)
# mostralinha()
# soma(8,9)
# mostralinha()
# soma(a=2, b=1)
# mostralinha()
# soma(b=2, a=1)

# def contador(*num):
#     ram = len(num)
#     print(f"Recebi os valores {num} e são, ao todo {ram} números.")

# contador(8, 7, 6, 5)
# contador(1, 2, 3)
# contador(9, 9, 9, 9, 9, 9, 9, 9, 9, 9)


# def dobra(lst):
    # pos = 0
    # while pos < len(lst):
    # lst[pos] *= 2
    # pos += 1
#
#
# valores = [7, 2, 5, 0, 4]
# dobra(valores)
# print(valores)


# def soma(*valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f"Somando os valores {valores} temos {s}")


# soma(7, 7)
# soma(2, 9, 4)

from time import sleep
def contador(i, f, p):
    print(f"Contagem de {i} até {10} de {p} em {p}")

    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont +=p
        print('fim')
        print()
    else:
        cont = 1
        while cont >= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont -=p
        print('fim')
#principal
contador(1, 10, 1)
contador(10, 0, 2)
print("Personalize a contagem:")
início = float(input("Início da contagem:"))
fim = float(input("Fim da contagem:"))
passo = float(input("Passo da contagem:"))
contador(início, fim, passo)