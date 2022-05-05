import numpy as np
PI = np.pi
class CodeAulas:
  def dft_2loops(sinal):
    N = len(sinal)
    volta = []
    dft = []
    Wn = np.exp((-1j)*2*PI/N)
    for k in range(N):
      for n in range(N):
        volta.append(sinal[n] * (Wn ** (k*n)))
      dft.append(np.sum(volta))
      volta = [] #Esvaziamos o vetor de volta
    return dft
  
  def dft_1loop(sinal):
    N = len(sinal)
    n = np.arange(0,N ,1)
    Wn = np.exp((-1j)*(2*PI/N)*n)
    dft = []
    for k in range(N):
      dft.append(np.sum(sinal * (Wn ** k)))
    return dft