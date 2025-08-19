import numpy as np

# Faz o zero padding do sinal para o valor de N
def zero_padding(signal, N):

  signal_zp = np.zeros(N)
  signal_zp[:len(signal)] = signal

  return signal_zp

# Faz o leading zeros do sinal para o valor de N
def leading_zeros(signal, N):

  signal_lz = np.zeros(N)
  signal_lz[-len(signal):] = signal

  return signal_lz