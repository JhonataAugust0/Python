def mensagem(msg):
    print(f'{msg}')


def área(b, a):
    área = b *a
    mensagem(f"A área do polígono, de {b}x{a}, é de {área}cm².")


área(b = float(input('Digite a base.')), a = float(input('Digite a altura.')))

#ou:
b = float(input("Digite a base: "))
a = float(input("Digite a altura: "))
área(b, a)