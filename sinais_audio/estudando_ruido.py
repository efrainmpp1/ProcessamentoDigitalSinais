import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

sinal , taxa_amostragem = sf.read('audio.wav')

sinal = sinal[:,0]

# utilizando periodo e o tamanho do vetor sinal para montar o vetor tempo
periodo = 1/taxa_amostragem
tempo_segundos_fim_sinal = len(sinal)*periodo

time = np.arange(0,tempo_segundos_fim_sinal,periodo) # criando vetor tempo

#No meu sinal de som, detectei um ruido entre os instantes 2s e 2.5s, então trabalharemos o sinal entre esses instantes de tempo
ruido = np.logical_and(time >= 2 , time <= 2.5 )

sf.write('ruido.wav', sinal[ruido] ,taxa_amostragem) #Criando arquivo de audio contendo o ruido

#Configurando o subplots
figure, axis = plt.subplots(2,1)
plt.subplots_adjust(wspace=0.25,hspace=0.5)

axis[0].set_title("Sinal")
axis[0].magnitude_spectrum(sinal,Fs=taxa_amostragem) #Grafico da fft do sinal
axis[1].set_title("Parte Ruidosa")
axis[1].magnitude_spectrum(sinal[ruido] , Fs=taxa_amostragem ) #Grafico da fft da parte ruidosa

plt.show()
