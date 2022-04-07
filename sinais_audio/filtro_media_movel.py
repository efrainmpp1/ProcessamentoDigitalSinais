import numpy as np
import soundfile as sf

#coletando sinal e taxa de amostragem do nosso arquivo de audio
sinal , taxa_amostragem = sf.read('audio.wav')

# Trazendo nosso sinal para uma dimensão
sinal = np.ndarray.flatten(sinal)
taxa_amostragem = 2*taxa_amostragem

# criando nosso filtro media movel com N termos
N = 50
filtro_media_movel = np.ones(N)/N

# fazendo a convolução so sinal com o filtro que retorna um sinal filtrado
sinal_filtrado = np.convolve(sinal , filtro_media_movel , mode='Full')

# Exportando o sinal filtrado como um audio
sf.write('audio_filtrado.wav' , sinal_filtrado , taxa_amostragem)

