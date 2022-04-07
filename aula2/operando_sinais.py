import numpy as np
import matplotlib.pyplot as plt

# Configurando os subplots
figure , axis = plt.subplots(4 , sharex=True)
plt.subplots_adjust(wspace=0.25,hspace=0.5)

x = np.array([1,2,3,-1,0,1,-1,1]) # criando um sinal qualquer
n = np.linspace(-4,3,8) # vetor n correspondente ao sinal x

# plotando sinal
axis[0].set_title("Sinal Normal") # Sinal normal
axis[0].stem(n,x)

# Objetivo é chegar em y[n] = x[-2n - 1]

# 1° passo é atrasar nosso sinal em 1/2 ficando x[n + 1/2]
n1 = n + 1/2 

axis[1].set_title("Atrasando sinal")
axis[1].stem(n1,x)


# 2° passo é inverter o nosso sinal ficando x[-(n+1/2)]
x2 = np.flip(x)

axis[2].set_title("Invertendo Sinal")
axis[2].stem(n1,x2)

# 3° passo é comprimir nosso espaço de n em 2
# Ficaremos por fim com x[-2n-1] = y[n] 
n2 = n * 1/2

axis[3].set_title("Finalizando Operação")
axis[3].stem(n2,x2)


plt.show()