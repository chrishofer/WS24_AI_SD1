def wie_weit_spazieren(gewicht : float, letztes_mal : int, vertraegt_sich : bool) -> float:
    if gewicht < 1 and not vertraegt_sich:
        if vertraegt_sich:
            return 4
        else:
            return 2
    elif (gewicht > 15 or letztes_mal > 25) and vertraegt_sich:
        return 8
    return 5


if __name__ == '__main__':
    # too lazy to test
    pass