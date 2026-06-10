import numpy as np

def calcular_angulo(a, b, c):

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cos = np.dot(ba, bc)
    cos /= np.linalg.norm(ba) * np.linalg.norm(bc)

    cos = np.clip(cos, -1.0, 1.0)

    return np.degrees(np.arccos(cos))


def reconhecer_braco(ombro, cotovelo, punho):

    angulo = calcular_angulo(
        ombro,
        cotovelo,
        punho
    )

    if angulo > 160:
        return "Braco Estendido"

    if angulo < 90:
        return "Braco Dobrado"

    return "Neutro"