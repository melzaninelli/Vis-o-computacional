import cv2

from camera import Camera
from detector import DetectorPose
from gestos import reconhecer_braco

camera = Camera()
detector = DetectorPose()

while True:
    frame = camera.capturar()
    if frame is None:
        break
    resultados = detector.detectar(frame)
    gesto = "Nenhum"
    for resultado in resultados:
        if resultado.keypoints is None:
            continue
        pontos = resultado.keypoints.xy.cpu().numpy()
        if len(pontos) == 0:
            continue
        pessoa = pontos[0]
        ombro_dir = pessoa[6]
        cotovelo_dir = pessoa[8]
        punho_dir = pessoa[10]
        gesto = reconhecer_braco(
            ombro_dir,
            cotovelo_dir,
            punho_dir
        )
        for x, y in pessoa:
            cv2.circle(
                frame,
                (int(x), int(y)),
                4,
                (0,255,0),
                -1
            )
    cv2.putText(
        frame,
        gesto,
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )
    cv2.imshow("Visao Computacional", frame)
    if cv2.waitKey(1) == ord('1'):
        break
camera.fechar()
cv2.destroyAllWindows()