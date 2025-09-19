# ReverbLab Real-Time Audio Processor

Este projeto é um exemplo de aplicação de reverberação em tempo real utilizando Python. Ele captura áudio do microfone, aplica um efeito de reverb escolhido pelo usuário e reproduz o áudio processado imediatamente.

---

## Funcionalidades

- Captura áudio em tempo real.
- Aplica reverberações pré-definidas.
- Processamento em blocos utilizando o método **overlap-add**.
- Escolha interativa do tipo de reverb.
- Suporte a diferentes ambientes acústicos simulados.

---

## Dependências

Certifique-se de ter instalado as bibliotecas abaixo:

```bash
pip install sounddevice numpy
```

O projeto também depende do módulo personalizado `ReberbLab_libs.ReverbLab_utils`.

---

## Estrutura do Código

### Configurações Iniciais

```python
# Tamanho do bloco de áudio
M = 1024

# Taxa de amostragem
fs = 44100
```

### Reverberações Disponíveis

```python
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
```

### Seleção do Reverb

O usuário escolhe qual efeito aplicar via input:

```python
for i, title in enumerate(titles):
    print(f"[{i+1}] -> {title}")

reverb_choosen = int(input("Escolha o reverb(1-9): "))
```

O código então carrega a resposta em frequência correspondente:

```python
H, N = getReverbFrequencyResponse(M, title=titles[reverb_choosen-1])
```

---

### Processamento de Áudio

Um vetor auxiliar `Add` é usado para o método **overlap-add**:

```python
Add = np.zeros(N-M)
```

A função `callback` é chamada a cada bloco de áudio capturado:

```python
def callback(indata, outdata, frames, time, status):
    global Add, N, M, H
    
    if status:
        print(f'status: {status}')

    outdata[:], Add = processAudio(indata, H, Add, N, M)
```

---

### Criação da Stream de Áudio

```python
stream = sd.Stream(callback=callback, blocksize=M, samplerate=fs, channels=1)
```

Execução em loop até que o usuário interrompa:

```python
with stream:
    print("Stream iniciada. Pressione Ctrl+C para parar.")
    while True:
        sd.sleep(100)
```

---

## Como Usar

1. Execute o script.
2. Escolha o tipo de reverb desejado (1 a 9).
3. Fale ou toque áudio no microfone.
4. Ouça o áudio processado em tempo real.
5. Pressione `Ctrl+C` para encerrar.

---

## Observações

- Certifique-se de que seu microfone e saída de áudio estejam configurados corretamente.
- O tamanho do bloco (`M`) e a taxa de amostragem (`fs`) podem ser ajustados para otimizar a latência e qualidade do processamento.
- Os efeitos de reverb dependem das respostas em frequência definidas na biblioteca `ReberbLab_utils`.

