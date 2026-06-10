import cv2

class Camera:

    def __init__(self, indice=0):
        self.cap = cv2.VideoCapture(indice)

        if not self.cap.isOpened():
            raise Exception("Erro ao abrir câmera")

    def capturar(self):
        ret, frame = self.cap.read()

        if not ret:
            return None

        return cv2.flip(frame, 1)

    def fechar(self):
        self.cap.release()