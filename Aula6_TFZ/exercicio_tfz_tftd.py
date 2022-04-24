import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob

PI = np.pi 

# Criamos a função que descreve a Transformada Z de u[n] - u[n-N]
def tfzx( Z , N):
  soma = 0
  for n in range(N):
    soma+= Z  ** (-n)
  return soma

w = np.linspace(-2*PI,2*PI,1000) #Criamos nosso vetor com o periodo que nosso sinal vai se repetir

frames = [] # Aqui estarão contidas as imagens dos graficos gerados

#Criando nossos graficos e salvando em arquivos de imagem .png
for i in range(5,12):
  vetTFTDX = tfzx(np.exp((-1j)*w) , i) #TFZ sendo a TFTD é com Z = e^(-jw) ou seja r = 1
  plt.clf() # Limpando alguma imagem antes de plotar a seguinte imagem
  plt.plot(w,vetTFTDX)
  plt.title("N =  {}".format(i))
  plt.ylabel("TFTD de x[n]")
  plt.xlabel("w")
  plt.savefig('grafico{}.png'.format(i))


imgs = glob.glob("*.png")#Pegando o nome dos nossos arquivos de imagens e aramzenando no vetor imgs
for i in imgs:
  new_frame = Image.open(i)
  frames.append(new_frame) #Adicionando a imagem no vetor de frames
  
# Gerando nosso arquivo .gif através do nosso vetor de frames
frames[0].save('graficos.gif',  format='GIF' , append_images=frames[1:] , save_all=True , duration=500,Loop=0)

