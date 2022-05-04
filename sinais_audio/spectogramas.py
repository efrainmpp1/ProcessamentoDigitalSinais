import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

sinal, taxa_amostragem = sf.read('audio.wav') #Lendo sinal de audio
sinal = sinal[:,0] # Trabalhando só com uma dimensão do sinal
periodo = 1/taxa_amostragem

time = np.arange(0,len(sinal)/taxa_amostragem , periodo) #criando vetor tempo

#Configurando os subplots
figure, axis = plt.subplots(2,1)
plt.subplots_adjust(wspace=0.25,hspace=0.5)

#Configurando os graficos
axis[0].set_title("Sinal")
axis[0].set_xlabel("time(s)")
axis[0].plot(time,sinal) #Vendo o sinal Normal
axis[1].set_title("Spectograma do Sinal ")
axis[1].set_xlabel("time(s)")
axis[1].set_ylabel("Frequencias (Hz)")
axis[1].specgram(sinal , Fs=taxa_amostragem) # Vendo o Spectograma do sinal

plt.show()


