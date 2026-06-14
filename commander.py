import pyautogui
import time

class Commander:

    def __init__(self, cooldown=1.5):
        self.cooldown = cooldown
        self.ultimo_tempo = 0
        self.ultimo_gesto = None

    def executar(self, gesto):
        agora = time.time()

        # Ignora se ainda está no cooldown ou gesto repetido
        if gesto == self.ultimo_gesto:
            return
        if agora - self.ultimo_tempo < self.cooldown:
            return

        if gesto == "Braco Estendido":
            pyautogui.press('right')
            print("[COMANDO] Próximo slide")

        elif gesto == "Braco Dobrado":
            pyautogui.press('left')
            print("[COMANDO] Slide anterior")

        self.ultimo_tempo = agora
        self.ultimo_gesto = gesto