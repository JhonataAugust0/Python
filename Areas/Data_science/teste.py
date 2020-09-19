import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]
#Definindo os valores do gráfico
x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

plt.title("Gráfico comparativo de barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x1, y1, label = "Grupo1")
plt.bar(x2, y2, label = "Grupo 2")

plt.legend()
plt.show()
#Exibindo o gráfico de barras

plt.title("Gráfico comparativo de linhas")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.plot(x1, y1, label = "Grupo1")
plt.plot(x2, y2, label = "Grupo 2")
plt.legend()
plt.show()
#Exibindo o gráfico de linhas 

plt.title("Gráfico comparativo de disperção")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.scatter(x1, y1, label = "Grupo1")
plt.scatter(x2, y2, label = "Grupo 2", color = "g")
plt.plot(x1, y1, x2, y2)
plt.legend()
plt.show()
#Exibindo o gráfico de disperção

