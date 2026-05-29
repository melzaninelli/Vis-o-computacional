import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERRO: Não foi possível acessar a webcam")
    exit()

#pega a resolução da webcam
largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Resolução da câmera: {largura}x{altura}")

fps = 0
tempo_anterior = time.time()

while True:

    #captura do frame
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar o frame.")
        break

    frame = cv2.flip(frame, 1)

    #calcula o fps e mostra na tela
    tempo_atual = time.time()
    delta = tempo_atual - tempo_anterior

    if delta > 0:
        fps = 1.0 / delta
    tempo_anterior = tempo_atual

    texto_fps = f"FPS: {fps:.2f}"
    texto_res = f"Resolucao: {largura}x{altura}"

    cv2.putText(frame, texto_fps, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, texto_res, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

    #esse nome é provisório tá kkkkk
    cv2.imshow("Kinect 2 - Aperte '1' para sair", frame)

    if cv2.waitKey(1) == ord('1'):
        break


cap.release()
cv2.destroyAllWindows()