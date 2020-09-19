c = ('\033[m',  # cor 0 - sem cores;
     '\033[0;30;41m',  # cor 1 - vermelho;
     '\033[0;30;42m',  # cor 2 - verde;
     '\033[0;30;43m',  # cor 3 - amarelo;
     '\033[0;30;44m',  # cor 4 - azul;
     '\033[0;30;45m',  # cor 5 - roxo;
     '\033[7;30'  # cor 6 - branco.
     )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    help(com)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(f'{c[cor]}', end='')
    print('~' * tam)
    print(f"  {msg}")
    print('~' * tam)
    print(f"{c[0]}", end='')


# principal:
comando = ''
while True:
    título("Sistema de ajuda Pyhelp.", 1)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    título("Até logo!", 5)
