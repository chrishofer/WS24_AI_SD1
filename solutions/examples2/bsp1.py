def reihe() -> float:
    erg = 0
    for z in range(2, 101):
        erg += 1/z
    return erg

if __name__ == '__main__':
    print(reihe())