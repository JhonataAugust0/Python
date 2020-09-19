def notas(*n, situação=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :parâmetro n: uma ou mais notas dos alunos;
    :parâmetro situação: valor opcional, indicando se deve ou não adicionar a situação;
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = (sum(n)/len(n))
    if situação == True:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['situação'] >= 5:
            r['situação'] = 'Mediana'
        else:
            r['situação'] = 'Péssima'

    return r


# programa principal:
resp = notas(9, 10, 5.5, 2.5, 9, 8.5, situação = True)
print(f'{resp}')
# help(notas)