from CodigosEmAula import CodeAulas #Importando os codigos da classe Criada no arquivo CodigosEmAula
import numpy as np

'''Um sinal x simples para comparar os metodos de tfd,quanto mais termos 
do vetor x, mais demorado vai ser calcular as funcoes'''
x = [1,2,3,4,5] 

print("Pelo metodo 2 loops temos: " , CodeAulas.dft_2loops(x))

print("Pelo metodo 1 loop temos: " , CodeAulas.dft_1loop(x))

print("Pelo metodo fft temos: " , np.fft.fft(x))