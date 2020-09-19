print("Digite o intervalo numérico da sequência  → ↓ ↗ ↓ → ↑.")
n1 = int(input("Digite o número inicial:"))
n2 = int(input("Digite o número final:"))
for i in range(n1, n2+1):
    resto = i % 6
    if resto == 0:
        print(f"{i} → ", end = ' ')
    elif resto == 1:
        print(f"{i} ↓ ", end = ' ')
    elif resto == 2:
        print(f"{i} ↗ ", end = ' ') 
    elif resto == 3:
        print(f"{i} ↓ ", end = ' ')
    elif resto == 4:
        print(f"{i} → ", end = ' ')
    elif resto == 5:
        print(f"{i} ↑ ", end = ' ')
print("\n")