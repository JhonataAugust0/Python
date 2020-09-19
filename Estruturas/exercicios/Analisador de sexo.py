idade = int(input("Informe sua idade.\n")).strip()
sexo = str(input("Informe seu sexo.\n")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos. por favor informe o sexo.\n")).strip().upper()[0]
print("Sexo {} e idade {} registrado.".format(sexo,idade))
#
#
#
tot18 =  0
toth = 0
totm = 0
while True:
    idade = int(input("Idade:"))
    sexo = ' '
    while sexo not in 'MF':
       sexo = str(input("Sexo: [M/F]\n")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth +=1
    if sexo == 'F' and idade < 20:
        totm += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0] 
    if resp == 'N':
        break
print(f"Total de pessoas maiores de idade: {tot18}.")
print(f"Total de Homens: {toth}.")
print(f"Total de mulheres com menos de 20 anos: {totm}.")
