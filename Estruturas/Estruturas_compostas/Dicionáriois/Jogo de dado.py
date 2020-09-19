from random import randint
from time import sleep
from operator import itemgetter
jogo = {
        'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }
ranking = list()
print("Valores jogados: ")
print('=-'*20)
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
print('=-'*20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f"{ranking}")
print('=-'*20)
for i, v in enumerate(ranking):
    print(f"{i+1}° lugar: {v[0]} com {v[1]}. ")
    sleep(1)
print('=-'*20)
# Este algoritmo simula um jogo de dados, randomizando a jogada 
# feita por um jogador, e atribuindo seu valor para depois 
# elaborar um ranking!