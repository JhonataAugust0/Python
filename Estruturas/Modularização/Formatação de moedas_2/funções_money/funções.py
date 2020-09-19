def dobro(n=0, formato=False):]
    
    res = n * 2
    if formato == False:
        return res
    else:
        return moeda(res)



def metade(n=0, formato=False):
    res = n / 2
    if formato == False:
        return res
    else:
        return moeda(res)



def aumentar(n=0, taxa=0, formato=False):
    res = (n + (n * (taxa/100)))
    if formato == False:
        return res
    else:
        return moeda(res)


def diminuir(n=0, taxa=0, formato=False):
    res = (n - (n * (taxa/100)))
    if formato == False:
        return res
    else:
        return moeda(res)



def moeda(preço=0, moeda='R$'):
    return f' {moeda}{preço:.2f}'.replace('.', ',')
