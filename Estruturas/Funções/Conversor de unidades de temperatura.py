valor = 0


def leia_int(msg):
    """
    -> Essa função tem como parâmetro único o 'msg',
    ele será uma input, e o intuito da função é testar
    se a input é númerica, caso veraddeiro, ela conver-
    terá a input para float, e como a input tem que ser 
    numérica, enquanto um número não for digitado, o ci-
    clo não se encerrará.
    """
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = float(n)
            ok = True
        else:
            print("\033[0;31mErro, digite um número inteiro válido.\033[m")
        if ok == True:
            break
    return valor


print("Bem vindo(a) ao conversor de unidades de temperatura!\n")

while True: 
    while True:
        
        casos = str(input('''Digite '[1]' para converter de Celcius para Fahrenheit, '[2]' para converter de Fahrenheit para Celcius, 
        '[3]' para converter de Celcius para Kelvin, '[4]' para converter de Kelvin para Celcius, '[5]' para converter de Fahrenheit 
        para Kelvin, e '[6]' para converter de Kelvin para Fahrenheit. Digite '[7]' para encerrar o programa.\n''')).strip().upper()[0]

        if casos == '1' or casos == '2' or casos == '3' or casos == '4' or casos == '5' or casos == '6' or casos == '7':  
            break
        else:
            pass

    if casos == '7': 
        break
    else:

        if casos == '1': # Converter de Celcius para Fahrenheit.
            temperatura_do_usuário = leia_int("Digite sua temperatura em C°: ")
            temperatura_conversão = ((valor * 9/5) +32)
            print(f"{temperatura_do_usuário}C° em F° são {temperatura_conversão}F°.\n")

        elif casos == '2': # Converter de Fahrenheit para Celcius.
            temperatura_do_usuário = leia_int("Digite sua temperatura em F°: ")
            temperatura_conversão = ((temperatura_do_usuário - 32) * 5/9)
            print(f"{temperatura_do_usuário}F° em C° são {temperatura_conversão}C°.\n")

        elif casos == '3': # Converter de Celcius para Kelvin.
            temperatura_do_usuário = leia_int("Digite sua temperatura em C°: ")
            temperatura_conversão = (temperatura_do_usuário - 273.15)
            print(f"{temperatura_do_usuário}C° em K° são {temperatura_conversão}K°.\n")

        elif casos == '4': # Converter de Kelvin para Celcius.
            temperatura_do_usuário = leia_int("Digite sua temperatura em K°: ")
            temperatura_conversão = (temperatura_do_usuário + 273.15)
            print(f"{temperatura_do_usuário}K° em C° são {temperatura_conversão}C°.\n")

        elif casos == '5': # Converter de Fahrenheit para Kelvin.
            temperatura_do_usuário = leia_int("Digite sua temperatura em F°: ")
            temperatura_conversão = ((temperatura_do_usuário - 32) * 5/9 + 273.15)
            print(f"{temperatura_do_usuário}F° em K° são {temperatura_conversão}K°.\n")

        elif casos == '6': # Converter de Kelvin para Fahrenheit.
            temperatura_do_usuário = leia_int("Digite sua temperatura em K°: ")
            temperatura_conversão = ((temperatura_do_usuário - 273.15) * 9/5 + 32)
            print(f"{temperatura_do_usuário}K° em F° são {temperatura_conversão}F°.\n")
            