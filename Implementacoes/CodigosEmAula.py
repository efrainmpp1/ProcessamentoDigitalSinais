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

  def circular_convolve(array1,array2):
    fft1 = np.fft.fft(array1)
    fft2 = np.fft.fft(array2)
    circular = np.fft.ifft(fft1*fft2).real
    return circular

  def linear_convolve_by_fft(array1 , array2):
    N1 = len(array1)
    N2 = len(array2)
  
    big = N1 if N1 >= N2 else N2

    len_array_convolve = N1 + N2 - 1
    new_array1 = np.zeros(len_array_convolve)
    new_array2 = np.zeros(len_array_convolve)
    for i in range(big):
      if i < N1 :
        new_array1[i] = array1[i]
      if i < N2:
        new_array2[i] = array2[i]

    return CodeAulas.circular_convolve(new_array1,new_array2)

  def filter_fir_kaiser_low_pass(signal,fs,fc,n_coeficientes,atenuacao):
    wc = PI*fc/(fs/2)

    M1 = -(n_coeficientes-1)/2
    M2 = (n_coeficientes-1)/2
    n1 = np.arange(M1,M2+1)

    hlp = (wc/PI)*(np.sin(wc*n1))/(wc*n1)
    hlp[n1 == 0] = wc/PI  

    # Kaiser Window
    r = atenuacao # Controls the dBs below the mainlobe magnitude.
    beta = 0.1102*(r - 8.7)
    kaiser_window = np.kaiser(n_coeficientes,beta)

    #Obtain hlp into Kaiser Window
    hlp_kaiser = hlp * kaiser_window 
    signal_filtered = np.convolve(signal,hlp_kaiser) #Filtering the signal

    return signal_filtered[n_coeficientes-1:]

  def filter_fir_kaiser_high_pass(signal,fs,fc,n_coeficientes,atenuacao):
    hlp_kaiser = CodeAulas.filter_fir_kaiser_low_pass(signal,fs,fc,n_coeficientes,atenuacao)

    index_pos_max = np.where(hlp_kaiser == max(hlp_kaiser))[0][0]
    b_impulse = np.zeros(n_coeficientes)
    b_impulse[index_pos_max] = 1
    b_HP = b_impulse - hlp_kaiser

    signal_filtered_hp = np.convolve(signal,b_HP)

    return signal_filtered_hp[n_coeficientes-1:]