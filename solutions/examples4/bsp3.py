class Verwaltungsstrafe:
    __strafen_zaehler = 1

    def __init__(self, vorname, nachname, kennzeichen):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__kennzeichen = kennzeichen
        self.__strafnummer = Verwaltungsstrafe.__strafen_zaehler
        Verwaltungsstrafe.__strafen_zaehler += 1

        self.__strafe = 0.0
        self.__anzahl = 0

    @property
    def vorname(self):
        return self.__vorname

    @property
    def nachname(self):
        return self.__nachname

    @property
    def kennzeichen(self):
        return self.__kennzeichen

    @property
    def strafnummer(self):
        return self.__strafnummer

    @property
    def strafe(self):
        if self.anzahl == 1:
            rabatt = 0.3
        elif self.anzahl == 2:
            rabatt = 0.2
        elif self.anzahl == 3:
            rabatt = 0.1
        else:
            rabatt = 0
        return self.__strafe * (1 - rabatt)

    @property
    def anzahl(self):
        return self.__anzahl

    def ueberschreitung(self, geschwindigkeitsueberschreitung: int):
        self.__anzahl += 1
        if geschwindigkeitsueberschreitung <= 20:
            self.__strafe += 30
        elif geschwindigkeitsueberschreitung <= 30:
            self.__strafe += 50
        elif geschwindigkeitsueberschreitung <= 50:
            self.__strafe += 100
        elif geschwindigkeitsueberschreitung <= 100:
            self.__strafe += 500
        else:
            self.__strafe += 1500

    def verbandspaket(self):
        self.__anzahl += 1
        self.__strafe += 25

    def alkohol(self, promille: float):
        if promille < 0.5:
            return
        self.__anzahl += 2
        if promille <= 1.0:
            self.__strafe += 100
        elif promille <= 2.0:
            self.__strafe += 400
        elif promille <= 3.0:
            self.__strafe += 1000
        else:
            self.__strafe += 5000

if __name__ == '__main__':
    a = Verwaltungsstrafe("hansi", "hinterseer", "was299")
    b = Verwaltungsstrafe("susi", "musterstudi", "was259")
    print(a.strafnummer)
    print(b.strafnummer)
    a.ueberschreitung(100)
    print(a.strafe)
    