import sounddevice as sd

def callback(indata, outdata, frames, time, status):
    if status:
        print(f'status: {status}')
    outdata[:] = indata * 10 # aqui dá pra processar o áudio

stream = sd.Stream(callback=callback, blocksize=1024, samplerate=16000, channels=1)
with stream:
    sd.sleep(10000)  # grava/toca por 10 segundos
