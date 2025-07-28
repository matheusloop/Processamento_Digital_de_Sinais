import numpy as np

# Retorna o vetor com os valores de WN de 0 até N/2 - 1
def W_N(N):
  k = np.arange(0, N/2)
  return np.exp(-2j*np.pi/N)**k


# Faz o zero padding do sinal para a potência de 2 mais próxima ou para o valor de N
def zero_padding(signal, N=None):

  if N == None:
    l = np.ceil(np.log2(len(signal)))
    N = int(2**l)

  signal_zp = np.zeros(N)
  signal_zp[:len(signal)] = signal

  return signal_zp


#Faz o cálculo recursivo da FFT
def calculate_fft(signal):
  N = len(signal) #Determina o valor de N

  #Se o tamanho for unitário, retorna o próprio valor
  if N == 1:
    return signal

  #Para dimenção maior, é feita a divisão da DFT em duas e
  if N > 1:

    X_e = calculate_fft(signal[::2])
    X_o = calculate_fft(signal[1::2])
    #Calcula a parte superior da DFT usando a soma das partes pares e impares ponderadas
    X_up   = X_e + W_N(N) * X_o

    #Calcula a parte inferior da DFT usando a subtração das partes pares e impares ponderadas
    X_down = X_e - W_N(N) * X_o

  #Retorna a DFT concatenada
  return np.concatenate([X_up, X_down])


#Calcula a FFT ajustando o numero de amostras
def myFFT(signal, N = None):

  #Faz o zero padding no sinal
  signal_zp = zero_padding(signal, N)

  #Retorna a FFT do sinal
  return calculate_fft(signal_zp)