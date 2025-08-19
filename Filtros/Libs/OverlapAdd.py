from Convolution import *
from utils import *

def calculate_overlapAdd(xk, h, y):
    #Verifica se y está vazio e retorna a primeira convolução
    if len(y) == 0:
        y = myConvolution(xk, h)

    #Se y não está vazio, realiza a soma dos elementos em sobreposição e acrescenta os demais elementos da convolução atual
    else:
        L = len(h) #Tamanho de h. Existem L-1 elementos em sobreposição
        yk = myConvolution(xk, h)

        #Faz a soma dos elementos em sobreposição
        for i in range(1, L):
            y[-(L-i)] += yk[i-1]

        #Acrescenta os demais elementos da convolução atual
        y = np.concatenate((y, yk[L-1:]))

    return y

def myOverlapAdd(x, h, M):
    y = np.array([]) # Inicializa y como um array vazio

    # Percorre x em blocos de tamanho M. Envia janelas de tamanho M para realizar a convolução
    # e acumula os resultados em y
    for i in range(0, len(x), M):
        xk = x[i:i + M]
        y = calculate_overlapAdd(xk, h, y)

    return y 