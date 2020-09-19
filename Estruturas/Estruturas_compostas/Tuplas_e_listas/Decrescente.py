valores = []
while True:
    valores.append(int(input("Digite um valor")))
    resp = str(input("Quer continuar?"))
    if resp in 'Nn':
        break
print(f"Você digitou {len(valores)} valores. \n")
valores.sort(reverse= True)
print(f"Os valores em ordem decrescente são {valores}.\n")
if 5 in valores:
    print(f"O valor 5 faz parte da lista")
else:
    print("Não")
# Aqui temos um algoritmo que tem a finalidade de coletar números
# e realizar analizes, nos mostrando a quantidade de valores digitados
# a ordem decrescente dos mesmos
