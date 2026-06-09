import cv2
import numpy as np
import time
from ultralytics import YOLO

# Carrega modelo de pose
model = YOLO("yolo11n-pose.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir webcam")
    exit()

def calcular_angulo(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cos = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    cos = np.clip(cos, -1.0, 1.0)

    return np.degrees(np.arccos(cos))

tempo_anterior = time.time()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    resultados = model(frame, verbose=False)

    gesto = "Nenhum"

    for resultado in resultados:

        if resultado.keypoints is None:
            continue

        pontos = resultado.keypoints.xy.cpu().numpy()

        if len(pontos) == 0:
            continue

        pessoa = pontos[0]

        # Índices COCO
        # 5 = ombro esquerdo
        # 6 = ombro direito
        # 7 = cotovelo esquerdo
        # 8 = cotovelo direito
        # 9 = punho esquerdo
        # 10 = punho direito

        ombro_dir = pessoa[6]
        cotovelo_dir = pessoa[8]
        punho_dir = pessoa[10]

        ombro_esq = pessoa[5]
        cotovelo_esq = pessoa[7]
        punho_esq = pessoa[9]

        # Desenha keypoints
        for x, y in pessoa:
            cv2.circle(
                frame,
                (int(x), int(y)),
                4,
                (0, 255, 0),
                -1
            )

        # Verifica se os pontos existem
        if np.all(ombro_dir > 0) and np.all(cotovelo_dir > 0) and np.all(punho_dir > 0):

            angulo_dir = calcular_angulo(
                ombro_dir,
                cotovelo_dir,
                punho_dir
            )

            cv2.putText(
                frame,
                f"Angulo D: {int(angulo_dir)}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2
            )

            # Exemplos de gestos
            if angulo_dir > 160:
                gesto = "Braco Estendido"

            elif angulo_dir < 90:
                gesto = "Braco Dobrado"

            if punho_esq[1] < ombro_esq[1]:
                gesto = "Mao Direita Levantada"
            if punho_dir[1] < ombro_dir[1]:
                gesto = "Mao Esquerda Levantada"

        # T-pose simples
        if (
            abs(punho_dir[1] - ombro_dir[1]) < 50 and
            abs(punho_esq[1] - ombro_esq[1]) < 50
        ):
            gesto = "T-Pose"

    tempo_atual = time.time()
    fps = 1 / (tempo_atual - tempo_anterior)
    tempo_anterior = tempo_atual

    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,0,0),
        2
    )

    cv2.putText(
        frame,
        f"Gesto: {gesto}",
        (10, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,0,255),
        2
    )

    cv2.imshow("YOLO Pose", frame)

    if cv2.waitKey(1) & 0xFF == ord('1'):
        break

cap.release()
cv2.destroyAllWindows()