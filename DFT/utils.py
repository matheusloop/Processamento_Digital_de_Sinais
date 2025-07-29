import numpy as np

# Faz o zero padding do sinal para a potência de 2 mais próxima ou para o valor de N
def zero_padding(signal, N):

  signal_zp = np.zeros(N)
  signal_zp[:len(signal)] = signal

  return signal_zp

