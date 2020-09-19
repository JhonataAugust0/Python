listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f"Digite um valor para a posição {c}.\n")))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c] 
print(f"Você digitou os valores {listanum}")          
print(f"O maior valor digitado foi {maior} na posição ", end= '')
for i, v in enumerate(listanum):
    if v == maior:
        print(f"{i}....")
print(f"O menor valor digitado foi {menor} na posição ", end= '')
for i, v in enumerate(listanum):
    if v == menor:
        print(f"{i}....")
print() 
# Isto é um algoritmo que coleta números e realiza algumas análises sobre 
# eles, identificando qual o menor e o maior deles, incluindo suas respectivas
# posições. 