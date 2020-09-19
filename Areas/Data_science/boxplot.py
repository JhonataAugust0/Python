import matplotlib.pyplot as plt
import random


vetor = []
for i in range (1111):
    num_aleatorio = random.randint(0, 999752199999)
    vetor.append(num_aleatorio)    
     
plt.boxplot(vetor)
plt.title("Boxplot randomizado")
plt.show()