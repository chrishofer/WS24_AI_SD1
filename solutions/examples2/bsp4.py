import random

def wie_oft_wuerfeln(seite: int, anzahl: int) -> int:
    zaehler = 0
    gefunden = 0

    while gefunden < anzahl:
        z = random.randint(1, 6)
        zaehler += 1
        if z == seite:
            gefunden += 1

    return zaehler


if __name__ == '__main__':
    print(wie_oft_wuerfeln(3, 100))