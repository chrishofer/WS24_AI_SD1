def umsatz_aufbereiten(daten: list[tuple[str, float]]) -> dict[str, list[any]]:
    """Bereitet Verkaufsdaten für Visualisierungstool auf

    Parameters
    ----------
    daten : list of tuple of str, float
        Daten aus dem Verkaufssystem, für jeden Verkauf Name des Geräts und Preis
    Returns
    -------
    dict of str, list of str, float, float
        Aufbereitete Datenstruktur für Visualisierungssystem
        Beispiel: {"günstig": [0, 0, 0], "normal": [3, 750, 250], "premium": [2, 2000, 1000]}
    """

    # Dieser Code ist jetzt nicht sehr flexibel und erweiterbar
    list_cheap = [0, 0, 0]
    list_normal = [0, 0, 0]
    list_premium = [0, 0, 0]
    for tl in daten:
        if tl[1] < 300:
            list_cheap[0] += 1
            list_cheap[1] += tl[1]
        elif tl[1] < 600:
            list_normal[0] += 1
            list_normal[1] += tl[1]
        else:
            list_premium[0] += 1
            list_premium[1] += tl[1]

    list_cheap[2] = list_cheap[1] / list_cheap[0]
    list_normal[2] = list_normal[1] / list_normal[0]
    list_premium[2] = list_premium[1] / list_premium[0]
    return {"günstig": list_cheap, "normal": list_normal, "premium": list_premium}



if __name__ == '__main__':
    vd = [("iphone 12", 800),("one plus 6", 500),("iphone 16 pro", 1200),("Nokia", 50),("Xiaomi Redmi", 150),("Xiaomi 7", 250)]
    print(umsatz_aufbereiten(vd))