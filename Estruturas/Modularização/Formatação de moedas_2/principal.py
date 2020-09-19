from Pacote. import funções
# from funções import metade
# from funções import dobro
# from funções import aumentar
# from funções import diminuir
p = float(input("Digite o preço: R$"))
print(f"A metade de {funções.moeda(p)} é {funções.metade(p, True)}.")
print(f"O dobro de {funções.moeda(p)} é {funções.dobro(p, True)}.")
print(f"Aumentando 10% de {funções.moeda(p)} temos {funções.aumentar(p, 10, True)}.")
print(f"Reduzindo 13% de {funções.moeda(p)} temos {funções.diminuir(p, 13, True)}.")
