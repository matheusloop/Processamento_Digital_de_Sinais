from FFT import *
from utils import zero_padding

def myConvolution(signal1, signal2):
    L = len(signal1) #Determina o comprimento do primeiro Sinal
    M = len(signal2) #Determina o comprimento do segundo Sinal

    N = L + M - 1 #Determina o tamanho minimo dos sinais para a convolução linear

    signal1_zp = zero_padding(signal1, N) #Faz o zero padding do primeiro sinal para N amostras
    signal2_zp = zero_padding(signal2, N) #Faz o zero padding do segundo sinal para N amostras

    spectrum_signal1 = myFFT(signal1_zp) #Determina o espectro do primeiro sinal ajustado
    spectrum_signal2 = myFFT(signal2_zp) #Determina a espectro do segundo sinal ajustado

    spectrum_convolved_signal = spectrum_signal1*spectrum_signal2 #Multiplica os espectros dos sinais (colvolui no tempo)

    convolved_signal = myIFFT(spectrum_convolved_signal) #Determina o sinal convoluido no tempo

    return convolved_signal[:N] #Retorna o sinal truncado para N amostras