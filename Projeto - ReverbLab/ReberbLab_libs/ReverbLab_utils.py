import numpy as np
from scipy.io import wavfile

# Carrega a resposta em frequência do reverb selecionado
def getReverbFrequencyResponse(BlockSize, title='Normal'):
    # IR padrão
    if title == 'Normal':
        h = np.zeros(2048, dtype=np.float32)
        h[0] = 30.0
    else:
        # lê o arquivo .wav
        fs, h = wavfile.read(f'SelectedReverbs\{title}.wav')

        # normaliza int16/int32
        if h.dtype == np.int16:
            h = h.astype(np.float32) / 32768
        elif h.dtype == np.int32:
            h = h.astype(np.float32) / 2147483648
        elif h.dtype.kind == 'f':
            h = h.astype(np.float32)

        # se stereo, pega só um canal
        if h.ndim > 1:
            h = h[:, 0]

    M = BlockSize # tamanho do bloco
    L = len(h) # tamanho do IR
    N = M + L - 1 # tamanho da convolução

    return np.fft.fft(h, N), N

# Processa o áudio capturado para aplicar o reverb
def processAudio(indata, H, Add, N, M):

    # Transformada de Fourier do bloco capturado
    X = np.fft.fft(indata[:, 0], N) 

    # Multiplicação no domínio da frequência (Convolução no tempo)
    Y = X * H

    # Transformada Inversa de Fourier
    y = np.fft.ifft(Y).real

    # Overlap-Add
    y[:N-M] += Add

    # Atualiza o vetor de overlap-add
    Add = y[M:]

    return y[:M].reshape(M, 1), Add # retorna o bloco processado e o vetor Add atualizado