import matplotlib.pyplot as plt 


x = []
y = []
titulo = "Crescimento da população brasileira 1980-2016"
legenda_x = "Ano"
legenda_y = "População * 100.000.000"


def leitura_de_dados(arquivo):
    for i in range(len(arquivo)):
        if i != 0:
            linha = arquivo[i].split(';')
            x.append(int(linha[0]))
            y.append(int(linha[1]))
"""
Função que executa a leitura de um arquivo analisando 
seu tamanho e saparando seus dados cada um em uma casa
de vetor unidimensional, atribuindo as mesmas um eixo 
do plano cartesiano a fim de constituir o gráfico.   
"""
                
def amostragem_de_dados(eixo_x, eixo_y, titulo, legenda_x, legenda_y):
    plt.bar(eixo_x, eixo_y, color="#e4e4e4")
    plt.plot(eixo_x, eixo_y, color="k", linestyle="--")
    plt.title(titulo)
    plt.xlabel(legenda_x)
    plt.ylabel(legenda_y)
    plt.show()                  
"""
Função que formata a visualização dos dados do gráfico
gerado por meio de métodos que configuram título, le-
genda o tipo de gráfico.
"""    
    
leitura_de_dados(open("original.csv").readlines())
amostragem_de_dados(x, y, titulo, legenda_x, legenda_y)   
        
