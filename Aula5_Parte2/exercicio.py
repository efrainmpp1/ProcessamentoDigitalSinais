import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

# Gerando vetor n com valores de 0 a 999
n = np.arange(0,1000,1)

# separando o sinal x[n] em duas partes
x1 = np.cos((PI/50)*n)
x2 = 0.2*np.cos((PI/10)*n)

# Criando nosso vetor x[n] somando os dois sinais anteriores
x = x1 + x2

#Através dos calculos no papel, conseguimos montar a TFTD de h e obtivemos H
def h_TFTD(w):
  return 1/(1-(1/3)*np.exp((-1j)*w))

# Aplicando o produto 
y = h_TFTD(PI/50) * x1 + h_TFTD(PI/10) * x2

#Plotando os graficos
figure, axis = plt.subplots(2,1)
plt.subplots_adjust(wspace=0.25,hspace=0.5)

axis[0].set_xlabel("n")
axis[0].set_ylabel("x[n]")
axis[0].plot(n,x)
axis[1].set_xlabel("n")
axis[1].set_ylabel("y[n]")
axis[1].plot(n,y)

plt.show()