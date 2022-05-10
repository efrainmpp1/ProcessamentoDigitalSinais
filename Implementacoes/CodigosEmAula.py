import numpy as np
PI = np.pi
class CodeAulas:
  def dft_2loops(sinal):
    N = len(sinal)
    dft = [] #Criamos o vetor saida que é a dft 
    Xn = [] # Criamos o vetor que percorrerá as multiplicões dentro do somatório 
    Wn = np.exp((-1j)*2*PI/N)  
    for k in range(N):
      for n in range(N):
        Xn.append(sinal[n] * (Wn ** (k*n))) #Adicionamos ao vetor os valores da multiplicação
      dft.append(np.sum(Xn)) # Os valores somados do vetor Xn serão o atual Xn
      Xn = [] #Esvaziamos o vetor Xn para percorrer o próximo Loop
    return dft
  
  def dft_1loop(sinal):
    N = len(sinal)
    dft = [] #Criamos o vetor saida que é a dft 
    n = np.arange(0,N ,1) # Criamos um vetor n espaçado de 1 em 1 de 0 a N-1
    Wn = np.exp((-1j)*(2*PI/N)*n) 
    for k in range(N):
      Xn = np.sum(np.sum(sinal * (Wn ** k))) # Calculo do Xn Simplificado
      dft.append(Xn) #Adicionamos o Xn no vetor saida
    return dft