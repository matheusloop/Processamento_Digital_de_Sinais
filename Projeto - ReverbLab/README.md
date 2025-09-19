# ReverbLab

Este projeto é um exemplo de aplicação de reverberação em tempo real utilizando Python. Ele captura áudio do microfone, aplica um efeito de reverb escolhido pelo usuário e reproduz o áudio processado para a saida de áudio.

---

## Funcionalidades

- Captura áudio em tempo real.
- Escolha interativa do tipo de reverb.
- Aplica reverberações pré-definidas.
- Processamento em blocos utilizando o método **Overlap-Add**.

---

## Dependências

Para o funcionamento do codigo deve-se instalar as dempendencias (bibliotecas) utilzando o comando abaixo na pasta do projeto:

```bash
pip install -r requirements.txt
```

Ou instale as bibliotecas manualmente com o comando:

```bash
pip install sounddevice numpy
```

O projeto também depende do módulo personalizado `ReberbLab_libs.ReverbLab_utils`.

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

