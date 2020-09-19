galera = list()
pessoa= dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo: [F/M] Digite 'O' caso não queira informar. ")).strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        elif pessoa['sexo'] == 'O':
            break
        else: 
            print("Digite novamente, apenas as opções acima.")
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    print(f"{galera}")
    while True:
        condição = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if condição in 'SN':
            break
        print("Digite apenas as opções acima.")
    if condição == 'N':
        break
print("-="*30)
print(f"Ao todo temos {len(galera)} cadastradas.")
media = soma / len(galera)
print(f"A média de idade é de {media} anos.")
print(f"As mulheres cadastradas foram: ",end='')
for p in galera: 
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ',end='')
print()
print("Lista de pessoas que estão com a idade acima da média: ")
for p in galera:
    if p['idade'] > media:
        for k, v in p.items():
            print(f"{k} = {v} ",end='')
        print()
print("Encerrado")
# Aqui temos um algoritmo que simula o cadastro de uma pessoa num BD 