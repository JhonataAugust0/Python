numeros = list()
print(numeros.clear())
while True:
    n= int(input("Digite um valor.\n"))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado.\n")
    else:
        print("Valor duplicado não é adicionado.")
    r = str(input("Quer continuar?"))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros},')
# Neste arquivo, fizemos um algoritmo procedual 
# que verifica a existência de um elemento dentro 
# de uma lista para poder adicioná-lo, ou não, na mesma