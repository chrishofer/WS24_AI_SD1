import abc
import math

# es gibt auch @abstractstaticmethod und @abstractclassmethod
# Abstrakte Klasse - davon können wir kein Objekt instanzieren
class Flaeche(abc.ABC):
    @abc.abstractmethod
    def flaeche(self) -> float:
        pass
    # Beispiel, dass auch Methoden implemetiert werden können
    def winkewinke(self):
        print("winke winke")


class Rechteck(Flaeche):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def flaeche(self):
        return self.l * self.b

class Kreis(Flaeche):
    def __init__(self, r: float):
        self.r = r
    def flaeche(self) -> float:
        return self.r ** 2 * math.pi

if __name__ == '__main__':
    #f = Flaeche() # abstrakte Klassen können nicht instanziert werden
    r = Rechteck(10, 2)
    print(r.flaeche())
    k = Kreis(10)
    print(k.flaeeche())

