from time import sleep
jogador = dict()
partidas = list()
quantidade = int(input("Quantos jogadores você vai cadastrar? "))

for q in range(0, quantidade):
    jogador.clear()
    partidas.clear()
    print()
    jogador['nome'] = str(input(f"Digite o nome do {q+1}° jogador: "))
    total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for contador in range(0, total):
        partidas.append(int(input(f"Quantos gols ele fez na {contador+1}° partida? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    gols = jogador['total']
    # função para depois print(gols1)
    
    print("-="*30)
    for k, v in jogador.items():
        print(f"O campo {k} tem valor {v}.")

    print("-="*30)
    print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
    for i, v in enumerate(jogador['gols']):
        sleep(1)
        print(f"Na partida {i+1}, o jogador {jogador['nome']} fez {v} gols.")
    sleep(1)
    print(f"Foi um total de {jogador['total']} gols.")
    print("-="*30)
# Aqui temos um algoritmo que coleta vários dados sobre um jogador hipotético, 
# analizando seu rendimento na forma de uma tabela.