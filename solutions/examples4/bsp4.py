from typing import List

class Zutat:
    def __init__(self, name: str, menge: float):
        self.__name = name
        self.__menge = menge


    @property
    def name(self):
        return self.__name

    @property
    def menge(self):
        return self.__menge
    def __repr__(self):
        return f'{self.name} ({self.menge})'

class Rezept:
    def __init__(self, name: str, personen: int, zutaten: List[Zutat]):
        self.__name = name
        self.__personen = personen
        self.__zutaten = zutaten
    @property
    def name(self):
        return self.__name

    @property
    def personen(self):
        return self.__personen

    @property
    def zutaten(self):
        return self.__zutaten

    def __str__(self):
        return f'{self.name} für {self.personen} Personen bestehend aus {self.zutaten}'

    def print_rezept(self):
        print(self.__str__())

    def umrechnen(self, personen: int) -> "Rezept":
        faktor = personen / self.personen
        neue_zutaten = []
        for z in self.zutaten:
            neue_zutaten.append(Zutat(z.name, z.menge * faktor))

        return Rezept(self.name, personen, neue_zutaten)

if __name__ == '__main__':
    ks = Rezept("Krautstrudel", 2, [Zutat("Kraut", 100), Zutat("Teig", 300)])
    ks.print_rezept()
    ks4 = ks.umrechnen(4)
    ks.print_rezept()
    ks4.print_rezept()