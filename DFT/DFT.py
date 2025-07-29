import numpy as np
from utils import zero_padding

# Função para gerar a matriz complexa de Fourier (WN)
def generate_WN(N):
    WN = np.ones((N, N), dtype=complex)
    
    for i in range(N):
        for j in range(N):
            WN[i][j] = np.exp((-2j * np.pi * i * j) / N)
    return WN


# Função para calcular a DFT usando zero padding
def calculate_DFT(x_n):
    N = len(x_n)
    WN = generate_WN(N)
    X_k = np.dot(WN, x_n)
    return X_k