'''pip install -r requirements.txt'''

import sounddevice as sd
import numpy as np

from ReberbLab_libs.ReverbLab_utils import *

# Tamanho do bloco de áudio
M = 1024

# Taxa de amostragem
fs = 44100

# Opções de reverberação disponíveis
titles = [
    'Normal',
    'ConventionCenterSteps',
    'CleftRidgeArch',
    'Greek 7 Echo Hall',
    'NaturalSciences',
    'On a Star',
    'PepperCanyonHall',
    'Right Glass Triangle',
    'TunnelToHeaven'
]

# Menu de seleção do reverb
print('='*40)
for i, title in enumerate(titles):
    print(f"[{i+1}] -> {title}")
print('='*40)


reverb_choosen = int(input("Escolha o reverb(1-9): "))

H, N = getReverbFrequencyResponse(M, title=titles[reverb_choosen-1])

# Vetor auxiliar para o método overlap-add
Add = np.zeros(N-M)

# Função chamada a cada bloco de áudio
def callback(indata, outdata, frames, time, status):
    global Add, N, M, H
    
    if status:  # Mostra erros da stream
        print(f'status: {status}')

    # Aplica o reverb no áudio capturado
    outdata[:], Add = processAudio(indata, H, Add, N, M)

# Criação da stream (entrada e saída de áudio)
stream = sd.Stream(callback=callback, blocksize=M, samplerate=fs, channels=1)

# Execução da stream
with stream:
    print("Stream iniciada. Pressione Ctrl+C para parar.")
    while True:
        sd.sleep(100)
