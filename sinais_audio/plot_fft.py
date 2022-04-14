import numpy as np
import  matplotlib.pyplot  as plt
import soundfile as sf

# lendo audio e pegando o sinal e taxa de amostragem
sinal , taxa_amostragem = sf.read('audio.wav') # você pode escolher o arquivo de audio que quiser 

# Trazendo nosso sinal para uma dimensão
sinal = np.ndarray.flatten(sinal)

sinal_fft = np.fft.fft(sinal) # aplicando a transformada rapida de Fourier

sinal_fft = sinal_fft.real # pegando apenas a parte real para trabalharmos

frequencias = np.fft.fftfreq(len(sinal_fft)) # montando nosso eixo das frequencias

plt.plot(frequencias,sinal_fft)
plt.title("Sinal no Dominio Frequencia")
plt.xlabel("Frequencia")
plt.ylabel("Amplitude")
plt.show()