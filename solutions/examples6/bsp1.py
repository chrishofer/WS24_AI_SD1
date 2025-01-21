from typing import List, Dict
import abc


class Ente(abc.ABC):
    def __init__(self, name: str, gewicht: int):
        self._name = name
        self._gewicht = gewicht

    @property
    def gewicht(self):
        return self._gewicht

    @abc.abstractmethod
    def get_full_weight(self) -> int:
        pass

    @abc.abstractmethod
    def make_noise(self) -> str:
        pass


class FlugEnte(Ente):
    def __init__(self, name: str, gewicht: int, gewicht_federn: int):
        super().__init__(name, gewicht)
        self._gewicht_federn = gewicht_federn

    def __repr__(self):
        return f'FlugEnte {self._name} {self.gewicht} {self._gewicht_federn}'


    def get_full_weight(self) -> int:
        return self.gewicht + self._gewicht_federn

    def make_noise(self) -> str:
        return "Quack quack"

class BadeEnte(Ente):
    def __init__(self, name: str, gewicht: int, gewicht_wasser: int):
        super().__init__(name, gewicht)
        self._gewicht_wasser = gewicht_wasser

    def __repr__(self):
        return f'BadeEnte {self._name} {self.gewicht} {self._gewicht_wasser}'


    def get_full_weight(self) -> int:
        return self.gewicht + self._gewicht_wasser

    def make_noise(self) -> str:
        return "Quietsch quietsch"

class EntenHausen():
    def __init__(self):
        self.__enten = []

    def add(self, e: Ente):
        self.__enten.append(e)

    def get_gruppierte_enten(self) -> Dict[int, List[Ente]]:
        erg = {100: [], 200: [], 300: []}

        for e in self.__enten:
            g = e.get_full_weight()
            if g <= 100:
                erg.get(100).append(e)
            elif g > 100 and g <= 200:
                erg.get(200).append(e)
            elif g > 200 and g <= 300:
                erg.get(300).append(e)

        return erg


if __name__ == '__main__':
    h = EntenHausen()
    h.add(BadeEnte("Badeente 1", 60, 20))
    h.add(BadeEnte("Badeente 2", 120, 20))
    h.add(BadeEnte("Badeente 3", 100, 20))
    h.add(FlugEnte("Flugente", 200, 50))

    print(h.get_gruppierte_enten())