import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

#coletando sinal e taxa de amostragem do nosso arquivo de audio
sinal , taxa_amostragem = sf.read('audio.wav')

# Trazendo nosso sinal para uma dimensão
sinal = np.ndarray.flatten(sinal)
taxa_amostragem = 2*taxa_amostragem
periodo = 1/taxa_amostragem

time = np.arange(0,len(sinal)/taxa_amostragem , periodo) #criando vetor tempo

# criando nosso filtro media movel com N termos
N = 500 # Escolha o valor de termos desejado
filtro_media_movel = np.ones(N)/N

# fazendo a convolução so sinal com o filtro que retorna um sinal filtrado
sinal_filtrado = np.convolve(sinal , filtro_media_movel , mode='Full')

# Exportando o sinal filtrado como um audio
sf.write('audio_filtro_media_movel.wav' , sinal_filtrado , taxa_amostragem)

#Como o sinal resultando da convolução gera um sinal adiantado, então teremos que reajustar

sinal_filtrado_reajustado = sinal_filtrado[(N-1):len(sinal_filtrado)]

figure, axis = plt.subplots(2,1)
plt.subplots_adjust(wspace=0.25,hspace=0.5)
axis[0].set_title("Sinal")
axis[0].plot(time,sinal)
axis[1].set_title("Sinal filtrado")
axis[1].plot(time,sinal_filtrado_reajustado)
plt.show()

