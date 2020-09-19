ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer contunuar? [S/N]"))
    if resp in 'Nn':
        break
print('-=' *30)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':<8}")
print('-=' *30)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:<9}")
while True:
    print('-=' *30)
    opc = int(input("Mostrar as notas de qual aluno(a)? ('999' para interromper.)\n"))
    if opc == 999:
        print("Finalizando...")
        break
    elif opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} {ficha[opc][1]}.\n')
# Aqui temos um algoritmo que simula uma tabela de notas de alunos numa 
# escola, onde conseguimos atribuir alunos e suas notas.  