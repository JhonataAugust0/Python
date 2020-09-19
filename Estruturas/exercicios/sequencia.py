print('''Existe uma sequência que se repete indefinidamente com as figuras
de um triângulo, árvore, losângulo, espada, coração e um quadrado, nesse padrão.
Ou seja, há um padrão de repetição das 6 primeiras figuras.\n''')

n = int(input("Digite o número de elmentos que a sequência vai ter.\n"))
padroes = n / 6
resto = n % 6
print(f'''Num cenário em que essa sequência tenha {n} fuguras,
haverá {padroes} padrões e restará {resto} elementos.''')

n1 = int(input("Digite o número inicial para saber a sequência de figuras:"))
n2 = int(input("Digite o número final:"))
for i in range(n1, n2):
    resto = i % 6
    if resto == 0:
        print(f"{i} triângulo ", end=' ')
    elif resto == 1:
        print(f"{i} árvore ", end=' ')
    elif resto == 2:
        print(f"{i} losângulo ", end=' ')
    elif resto == 3:
        print(f"{i} espada ", end=' ')
    elif resto == 4:
        print(f"{i} coração ", end=' ')
    elif resto == 5:
        print(f"{i} quadrado ", end=' ')
