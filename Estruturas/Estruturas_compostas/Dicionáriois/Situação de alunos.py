quantidade = int(input("Quantos alunos quer cadatrar?"))
aluno = {}
for alunos in range(0, quantidade):
    aluno['nome'] = str(input("Nome do aluno: "))
    aluno['média'] = int(input("Média do aluno: "))
    if aluno['média'] >= 7:
        aluno['situação'] = 'Aprovado'
    else: 
        aluno['situação'] = 'Reprovado'
    for k, v in aluno.items():
        print(f"O campo {k} é {v}.")
# Aqui temos mais um sistema de escola, desta vez trabalhando 
# con dicionários e validando a reprovação ou não de um aluno
# tendo como critério sua nota.