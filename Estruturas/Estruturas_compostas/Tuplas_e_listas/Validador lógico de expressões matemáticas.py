print("Bem vindo ao validador lógico de expressões matemáticas.")
chave = []
expressão= str(input("Digite a expressão desejada:\n")).strip().upper()#
while expressão[0] not in '{':
    expressão= str(input("Digite a expressão inicializando com uma chave:\n")).strip().upper()#
for simb1 in expressão:
    if simb1[0] == '{':
        chave.append('{')
        colchete = []
        for simb2 in expressão:#!
            if simb2[0] == '[':
                colchete.append('[')
                parênteses = []
                for simb3 in expressão:#$
                    if simb3[0] == '(':
                        parênteses.append('(')
                    elif ')' not in expressão:
                        break
                    elif simb3 == ']':
                        if len(parênteses) > 0:
                            parênteses.pop()
                        else:
                            parênteses.append(')')
                            break#$
            elif ']' not in expressão:
                break
            elif simb2 == ']':
                if len(colchete) > 0:
                    colchete.pop()
                else:
                    colchete.append(']')
                    break#!
    elif '}' not in expressão:
        break
    elif simb1 == '}':
        if len(chave) > 0:
            chave.pop()
        else:
            chave.append('}')
            break
if len(chave) == 0:           
    if len(colchete) ==0: 
        if len(parênteses) == 0: 
            print(f"A sua expressão {expressão} está válida.")
else:
    print("Expressão inválida.")
# Este algoritmo percorre uma expressão matemática em forma de uma 
# string, verificando se suas chaves, colchetes e parênteses estão 
# devidamente fechados.