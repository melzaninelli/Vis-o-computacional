# Visão — Captura de Gestos em Tempo Real

Projeto acadêmico que utiliza visão computacional para controlar o computador através de gestos corporais capturados pela webcam, sem precisar tocar no teclado ou mouse.


## Sobre o projeto

O sistema detecta a posição dos braços do usuário em tempo real e transforma esses movimentos em comandos do sistema operacional — ideal para professores e palestrantes que desejam controlar slides de forma mais interativa.


## Como funciona

| Gesto | Ação |

| Braço direito estendido | ➡️ Próximo slide |
| Braço esquerdo estendido | ⬅️ Slide anterior |
| Braço direito dobrado a 90° | 🔊 Aumentar volume |
| Braço esquerdo dobrado a 90° | 🔇 Diminuir volume |

## Tecnologias

- [Python 3.10+](https://www.python.org/)
- [OpenCV](https://opencv.org/) — captura e exibição de vídeo em tempo real
- [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker) — estimativa de pose corporal
- [PyAutoGUI](https://pyautogui.readthedocs.io/) — envio de comandos ao sistema operacional

## Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/melzaninelli/Vis-o-computacional.git
cd Vis-o-computacional
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute**
```bash
python main.py
```

> Pressione `Q` para encerrar.

##  requirements.txt
