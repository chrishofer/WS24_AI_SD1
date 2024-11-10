def naechste_zecken_impfung(alter : int, letztes_impfungs_jahr: int, erste_auffrischung : bool) -> int:
    if alter >= 60 or erste_auffrischung:
        return letztes_impfungs_jahr + 3
    return letztes_impfungs_jahr + 5


if __name__ == '__main__':
    pass # gehoert noch getestet