import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

# Gerando vetor n com valores de 0 a 999
n = np.arange(0,1000,1)

# Criando nosso vetor x[n]
x = np.cos((PI/50)*n) + 0.2*np.cos((PI/10)*n)

# Criando o vetor h[n]
h = (1/3) ** n

#Através dos calculos no papel, conseguimos montar essas funções para representar o y[n]
def numerador(termo1,rad,n):
  return termo1*np.cos(rad*n) - (termo1/3)*np.cos(2*rad*n)
def denominador(rad):
  return 1 - (2/3)*np.cos(rad) + 1/9
# Criando nosso vetor y[n] que obtivemos através dos calculos
y = (numerador(1,PI/50,n)/denominador(PI/50)) + (numerador(1/5,PI/10,n)/denominador(PI/10))

#Plotando os graficos
figure, axis = plt.subplots(3,1)
plt.subplots_adjust(wspace=0.25,hspace=0.5)

axis[0].set_xlabel("n")
axis[0].set_ylabel("x[n]")
axis[0].plot(n,x)
axis[1].set_xlabel("n")
axis[1].set_ylabel("h[n]")
axis[1].plot(n,h)
axis[2].set_xlabel("n")
axis[2].set_ylabel("y[n]")
axis[2].plot(n,y)

plt.show()