from matplotlib import pyplot as plt
import numpy as np
import soundfile as sf

# lendo audio e pegando o sinal e taxa de amostragem
sinal , taxa_amostragem = sf.read('audio.wav') # você pode escolher o arquivo de audio que quiser 

# utilizando periodo e o tamanho do vetor sinal para montar o vetor tempo
periodo = 1/taxa_amostragem
tempo_segundos_fim_sinal = len(sinal)*periodo

tempo = np.arange(0,tempo_segundos_fim_sinal,periodo) # criando vetor tempo

sinal_invertido = np.flip(sinal) # invertendo sinal de audio

# Gerando um arquivo de audio com o sinal invertido
sf.write('audio_invertido.wav', sinal_invertido ,taxa_amostragem) 

# plotando os dois sinais

figure , (grafico1,grafico2) = plt.subplots(2,1,sharey=True) # gerando subplots

grafico1.set_title("Sinal de Audio")
plt.plot(tempo,sinal)

grafico2.set_title("Sinal de Audio Invertido")
plt.plot(tempo,sinal_invertido)

plt.show()



