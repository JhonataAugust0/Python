#tuplas são variáveis compostas onde podemos adicionar vários valores de uma só vez e realizar várias coisas com eles
palavras = ('aprender', 'programar') 
# Acima, acabamos de declarar uma tupla
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end="") 
# Aqui acabamos e fazer uma estrutura que coleta as vogais das palavras contidas na tupla

lanche = ['pizza', 'hambúrger', 'suco', 'sorvete']
# Aqui acabamos de definir uma lista
for p in lanche:
    print(lanche)
lanche.append('Olá')
# Adicionando um elemento 
for p in lanche:
    print(lanche)
del lanche[3] 
# Deletando um elemento
lanche.insert(0, 'picole')
for p in lanche:
    print(lanche)
# Inserindo um elemento numa posição específica
del lanche[3]
lanche.remove('pizza')
# Aqui temos outra forma de remover um elemento
if 'pizza' in lanche:
    lanche.remove('pizza')
# Verificando se o elemento existe na lista para removê-lo
valores = list(range(0, 10))
print(valores)
valores.sort()
valores.sort(reverse=True)
print(valores)
print(len(valores))

