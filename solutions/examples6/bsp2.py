import abc
from typing import List, Dict

class Fluessigkeit():
    def __init__(self, name: str, menge: float, alkohol_prozent: float):
        self.name = name
        self.menge = menge
        self.alkohol_prozent = alkohol_prozent


class Brennbar(abc.ABC):
    @abc.abstractmethod
    def brennt(self) -> bool:
        pass


class Getraenk(Brennbar, abc.ABC):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'{self.name} Zutaten:{self.get_anzahl_zutaten()} Alkoholisch:{self.beinhatet_alkohol()} Brennbar:{self.brennt()}'

    @abc.abstractmethod
    def get_anzahl_zutaten(self) -> int:
        pass

    @abc.abstractmethod
    def beinhatet_alkohol(self) -> bool:
        pass

    @abc.abstractmethod
    def menge_in_ml(self) -> float:
        pass


class SimplesGetraenk(Getraenk):
    def __init__(self, name: str, bestandteil: Fluessigkeit):
        self.name = name
        self.bestandteil = bestandteil


    def get_anzahl_zutaten(self) -> int:
        return 1

    def beinhatet_alkohol(self) -> bool:
        if self.bestandteil.alkohol_prozent > 0:
            return True
        else:
            return False

    def menge_in_ml(self) -> float:
        return self.bestandteil.menge

    def brennt(self) -> bool:
        if self.bestandteil.alkohol_prozent > 30:
            return True
        else:
            return False

class LongDrink(Getraenk):
    def __init__(self, name: str, spirituose: Fluessigkeit, filler: Fluessigkeit):
        self.name = name
        self.spirituose = spirituose
        self.filler = filler


    def get_anzahl_zutaten(self) -> int:
        return 2

    def beinhatet_alkohol(self) -> bool:
        if self.spirituose.alkohol_prozent > 0 or self.filler.alkohol_prozent > 0:
            return True
        else:
            return False

    def menge_in_ml(self) -> float:
        return self.spirituose.menge + self.filler.menge

    def brennt(self) -> bool:
        if self.spirituose.alkohol_prozent > 30 or self.filler.alkohol_prozent > 30:
            return True
        else:
            return False

class Cocktail(Getraenk):
    def __init__(self, name: str, bestandteile: List[Fluessigkeit]):
        self.name = name
        self.bestandteile = bestandteile

    def get_anzahl_zutaten(self) -> int:
        return len(self.bestandteile)

    def beinhatet_alkohol(self) -> bool:
        for b in self.bestandteile:
            if b.alkohol_prozent > 0:
                return True

        return False

    def menge_in_ml(self) -> float:
        m = 0
        for b in self.bestandteile:
            m += b.menge

        return m

    def brennt(self) -> bool:
        for b in self.bestandteile:
            if b.alkohol_prozent > 30:
                return True

        return False

class Registrierkasse():
    def __init__(self):
        self.__getraenke = []
        self.__verkaufte_getraenke = 0

    def verkauft(self, g: Getraenk):
        self.__getraenke.append(g)
        self.__verkaufte_getraenke += 1

    def get_getraenke_aufgeteilt_nach_zutaten(self) -> Dict[int, List[Getraenk]]:
        erg = {}
        for g in self.__getraenke:
            anz = g.get_anzahl_zutaten()

            erg.setdefault(anz, []).append(g)

        return erg

if __name__ == '__main__':
    kassa = Registrierkasse()
    kassa.verkauft(SimplesGetraenk("Cola", Fluessigkeit("Cola", 200, 0)))
    kassa.verkauft(Cocktail("Old Fashioned", [Fluessigkeit("Whiskey", 60, 40), Fluessigkeit("Zuckersirup", 50, 0), Fluessigkeit("Bitter", 2, 0)]))
    kassa.verkauft(Cocktail("Cuba Libre", [Fluessigkeit("Cola", 200, 0), Fluessigkeit("Whiskey", 40, 40),
                                              Fluessigkeit("Zitronensaft", 10, 0)]))

    print(kassa.get_getraenke_aufgeteilt_nach_zutaten())