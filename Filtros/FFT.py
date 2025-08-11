import numpy as np
from utils import zero_padding

# Retorna o vetor com os valores de WN de 0 até N/2 - 1
def W_N(N):
  k = np.arange(0, N/2)
  return np.exp(-2j*np.pi/N)**k

# Faz o cálculo recursivo da FFT
def calculate_fft(signal):
  N = len(signal) # Determina o valor de N

  # Se o tamanho for unitário, retorna o próprio valor
  if N == 1:
    return signal

  # Para dimensão maior, é feita a divisão da DFT em duas
  if N > 1:
    X_e = calculate_fft(signal[::2])
    X_o = calculate_fft(signal[1::2])

    # Calcula a parte superior da DFT usando a soma das partes pares e ímpares ponderadas
    X_up   = X_e + W_N(N) * X_o

    # Calcula a parte inferior da DFT usando a subtração das partes pares e ímpares ponderadas
    X_down = X_e - W_N(N) * X_o

  # Retorna a DFT concatenada
  return np.concatenate([X_up, X_down])


# Calcula a FFT ajustando o número de amostras
def myFFT(signal, N = None):
  if N == None:
    l = np.ceil(np.log2(len(signal)))
    N = int(2**l)

  # Faz o zero padding no sinal
  signal_zp = zero_padding(signal, N)

  # Retorna a FFT do sinal
  return calculate_fft(signal_zp)

def myFFTShift(fft):
  N = len(fft)

  return np.roll(fft, N//2)


# Faz o cálculo recursivo da IFFT
def calculate_ifft(espectrum):
  N = len(espectrum) # Determina o valor de N

  # Se o tamanho for unitário, retorna o próprio valor
  if N == 1:
    return espectrum

  # Para dimensão maior, é feita a divisão da DFT em duas
  if N > 1:
    X_e = calculate_ifft(espectrum[::2])
    X_o = calculate_ifft(espectrum[1::2])

    # Calcula a parte superior da IDFT usando a soma das partes pares e ímpares ponderadas
    x_up   = X_e + np.conj(W_N(N)) * X_o

    # Calcula a parte inferior da IDFT usando a subtração das partes pares e ímpares ponderadas
    x_down = X_e - np.conj(W_N(N)) * X_o

  # Retorna a IDFT concatenada
  return np.concatenate([x_up, x_down])


# Calcula a IFFT
def myIFFT(espectrum):
  N = len(espectrum)

  # Retorna a IFFT do espectro
  return calculate_ifft(espectrum).real / N
