def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = (atual-ano)

    if idade < 16:
        return f'Com {idade} anos: não vota.'
    elif 16 <= idade <= 17 or idade >= 65:
        return f'Com {idade} anos, seu voto é facultativo.'
    elif idade >= 18 and idade <= 64:
        return f'Com {idade} seu voto é obrigatório.'


nascimento = int(input("Digite o ano do seu nascimento: "))
print(f"{voto(nascimento)}")
