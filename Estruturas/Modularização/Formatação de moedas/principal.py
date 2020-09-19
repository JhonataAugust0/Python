from funções_money import funções
# from funções import metade
# from funções import dobro
# from funções import aumentar
# from funções import diminuir
p = float(input("Digite o preço: R$"))
print(f"A metade de {funções.moeda(p)} é {funções.moeda(funções.metade(p))}.")
print(f"O dobro de {funções.moeda(p)} é {funções.moeda(funções.dobro(p))}.")
print(f"Aumentando 10% de {funções.moeda(p)} temos {funções.moeda(funções.aumentar(p, 10))}.")
print(f"Reduzindo 13% de {funções.moeda(p)} temos {funções.moeda(funções.diminuir(p, 13))}.")
