from funções_money import funções
# from funções import metade
# from funções import dobro
# from funções import aumentar
# from funções import diminuir
p = float(input("Digite o preço: R$"))
print(f"A metade de {p} é {funções.metade(p)}.")
print(f"O dobro de {p} é {funções.dobro(p)}.")
print(f"Aumentando 10% de {p} temos {funções.aumentar(p, 10)}.")
print(f"Reduzindo 13% de {p} temos {funções.diminuir(p, 13)}.")
