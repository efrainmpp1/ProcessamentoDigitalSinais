import numpy as np
import  matplotlib.pyplot  as plt
import soundfile as sf

# lendo audio e pegando o sinal e taxa de amostragem
sinal , taxa_amostragem = sf.read('audio.wav') # você pode escolher o arquivo de audio que quiser 

# Trazendo nosso sinal para uma dimensão
sinal = np.ndarray.flatten(sinal)
periodo = 1/(2*taxa_amostragem)

sinal_fft = np.fft.fft(sinal) # aplicando a transformada rapida de Fourier

sinal_fft = sinal_fft.real # pegando apenas a parte real para trabalharmos

frequencias = np.fft.fftfreq(len(sinal_fft),d=periodo) # montando nosso eixo das frequencias
mascara = frequencias >= 0 #Condição de tirar a parte espelhada e só ficando com o quadrante positivo

plt.plot(frequencias[mascara],sinal_fft[mascara])
plt.title("Sinal no Dominio Frequencia")
plt.xlabel("Frequencia[Hz]")
plt.ylabel("Amplitude")
plt.show()