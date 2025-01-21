def geld_verzinsen(betrag: float, zeit: int, prozent: float) -> float:
    """Verzinst den Betrag `betrag` für `zeit` Jahre mit Zinsen in der Höhe von `prozent`

    Parameters
    ----------
    betrag : float
        Betrag der verzinzst werden soll
    zeit : int
        Anzahl der Jahre
    prozent : float
        Prozenthöhe
    Returns
    -------
    float
        das verzinste Ergebnis
    """
    return betrag * (1 + prozent / 100) ** zeit

def geld_verzinsen_schleife(betrag: float, zeit: int, prozent: float) -> float:
    erg = betrag
    for i in range(zeit):
        erg = erg * (1 + prozent / 100)

    return erg


if __name__ == '__main__':
    print(geld_verzinsen(1000, 2, 10))
    print(geld_verzinsen_schleife(1000, 2, 10))