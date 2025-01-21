def fehlerhafte_daten_aufbereiten(daten: list[tuple[str, float]]) -> list[list[str, int, float]]:
    """Findet fehlerhafte Daten die keinen Preis besitzen und liefert Position und geschätzten Wert dieser Geräte

    Funktion sucht nach fehlerhaften Daten im Parameter (das sind jene mit Preis -1 oder None) und liefert für all
    diese fehlerhaften Daten: Name des Produkts, Index und geschätzter Preis. Der geschätzte Preis ist der
    durchschnittliche Preis der gleich benannten Geräte mit angegebenem Preis

    Parameters
    ----------
    daten : list of tuple of str, float
        Daten aus dem Verkaufssystem, für jeden Verkauf ein Tuple mit Name des Geräts und Preis
        Fehlerhafte Daten sind Daten mit -1 oder None in der Preiskomponente
    Returns
    -------
    list of list of str, int, float
        Aufbereitete Datenstruktur zum Fehler korrigieren
        Beispiel: [["iphone 11", 0, 740.50], ["samsung galaxy note 20", 8, 800]]
    """

    inkorrekte_idx = []
    durchschnittliche_preise = {}
    # wir suchen einmal über alle daten
    # speichern die inkorrekten indizess auf der liste
    # und die korrekten preise auf dem dictionary
    for idx in range(len(daten)):
        if daten[idx][1] == -1 or daten[idx][1] == None:
            inkorrekte_idx.append(idx)
        else:
            # die liste enthält name, summe der preise, anzahl der geräte
            l = durchschnittliche_preise.get(daten[idx][0], [daten[idx][0], 0, 0])

            l[1] += daten[idx][1]
            l[2] += 1

            durchschnittliche_preise[daten[idx][0]] = l

    erg = []
    for iidx in inkorrekte_idx:
        geraet = durchschnittliche_preise[daten[iidx][0]]
        erg.append([geraet[0], iidx, geraet[1] / geraet[2]])

    return erg

if __name__ == '__main__':
    vd = [("iphone xs", 800), ("one plus 6", 500), ("iphone 16 pro", 1200),
          ("iphone xs", None), ("one plus 6", 400), ("Xiaomi 7", 250),
          ("iphone xs", 700), ("Xiaomi Redmi 3", 150), ("Xiaomi 7", 250),
          ("iphone xs", 600), ("Xiaomi Redmi", 150), ("Xiaomi 7", 250),
          ("iphone xs", -1), ("one plus 6", None), ("Xiaomi 7", 250)]

    print(fehlerhafte_daten_aufbereiten(vd))