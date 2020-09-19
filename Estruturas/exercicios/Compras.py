total = 0 
mil= 0
menor = 0
cont= 0
barato = ' '
while True:
    produto = str(input("Nome do produto:\n"))
    preço = float(input("Preço R$:"))
    cont += 1
    total += preço
    if preço > 1000:
        mil+= 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N]\n")).strip().upper()[0]
    if resp == 'N':
        break
print(f"O total da compra é: {total}.")
print(f"{mil} produtos acima de mil reais.")
print(f"O produto mais barato foi {barato} que custa R${menor}.")

