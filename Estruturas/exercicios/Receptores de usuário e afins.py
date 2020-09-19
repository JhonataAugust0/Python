r = 'S'
n = 1
while r == 'S': 
    n = int(input('Digite um valor')) 
    r = str(input("Deseja prosseguir?[S/N]")).upper()
print("Fim")

 n=0
cont= 0
soma= 0
while n != 999:
    n = int(input("Digite um número (999 para parar.)"))
    cont+= 1
    soma += n
    n = int(input("Digite um número (999 para parar.)"))
print("Você digitou {} números e a soma entre eles é {}".format(cont, soma))


n = s = 0
while True:
    n = int(input("Digite um número.\n"))
    if n == 999:
        break
    s += n 
print("A soma é {}".format(s))
print(f"A soma vale {s}")

ncon = 0 
soma = 0
while True:
    n = int(input("Digite um número.\n"))
    if n == 999:
        break
    ncon += 1 
    soma += n
print(f"A soma dos {ncon} elementos foi {soma}.\n")