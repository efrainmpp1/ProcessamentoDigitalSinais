import numpy as np
import  matplotlib.pyplot  as plt
import soundfile as sf

# lendo audio e pegando o sinal e taxa de amostragem
sinal , taxa_amostragem = sf.read('audio.wav') # você pode escolher o arquivo de audio que quiser 

# Trazendo nosso sinal para uma dimensão
sinal = np.ndarray.flatten(sinal)

plt.magnitude_spectrum(sinal , Fs= 2*taxa_amostragem )
plt.title("Sinal no Dominio Frequencia")
plt.xlabel("Frequencia[Hz]")
plt.ylabel("Amplitude")
plt.show()