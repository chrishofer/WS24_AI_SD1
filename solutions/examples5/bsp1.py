class Konto:
    def __init__(self, inhaber: str):
        self._inhaber = inhaber
        self._kontostand = 0

    @property
    def kontostand(self):
        return self._kontostand

    def einzahlen(self, wert: float):
        if wert > 0:
            self._kontostand += wert

    def auszahlen(self, wert: float) -> float:
        if wert < 0:
            return 0
        self._kontostand -= wert
        return wert

    def __repr__(self):
        return f'{self._inhaber}: {self.kontostand}'


class Sparkonto(Konto):
    # Beispiel Implementation die sich nicht auf Implementation der Basisklasse
    # bezieht
    def auszahlen(self, wert: float) -> float:
        if wert < 0:
            return 0
        if wert > self.kontostand:
            w = self.kontostand
            self._kontostand = 0
            return w

        self._kontostand -= wert
        return wert

class GiroKonto(Konto):
    def __init__(self, inhaber: str, limit: float):
        super().__init__(inhaber)
        self._limit = limit

    # Beispiel verwendet Implementaiton der Basisklasse
    def auszahlen(self, wert: float) -> float:
        if wert > self.kontostand + self._limit:
            w = self.kontostand + self._limit
            self._kontostand = -self._limit
            return w
        return super().auszahlen(wert)

class JugendGiroKonto(GiroKonto):
    def __init__(self, inhaber: str, limit: float, buchungslimit: float):
        super().__init__(inhaber, limit)
        self._buchungslimit = buchungslimit

    def auszahlen(self, wert: float) -> float:
        if wert > self._buchungslimit:
            return super().auszahlen(self._buchungslimit)

        return super().auszahlen(wert)

if __name__ == '__main__':
    k = Konto("Hansi")
    s = Sparkonto("Hansi Spar")
    g = GiroKonto("Hansi Giro", 100)
    j = JugendGiroKonto("Hansi Kind", 500, 1200)

    l = [k, s, g, j]
    for konto in l:
        konto.einzahlen(1000)
        print(konto.auszahlen(1300))
        print(konto)
