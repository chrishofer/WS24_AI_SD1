from math import floor

class Anlage:
    def __init__(self, bezeichnung:str, initialer_wert:float, nutzungsdauer: int):
        self.__bezeichnung = bezeichnung
        self.__initialer_wert = initialer_wert
        self.__nutzungsdauer = nutzungsdauer
        self.__rest_wert = initialer_wert
        self.__alter = 0

    @property
    def bezeichnung(self):
        return self.__bezeichnung

    @property
    def initialer_wert(self):
        return self.__initialer_wert

    @property
    def nutzungsdauer(self):
        return self.__nutzungsdauer
    @property
    def rest_wert(self):
        return self.__rest_wert

    @property
    def alter(self):
        return self.__alter

    def abschreiben(self):
        self.__alter += 1
        if self.alter <= self.nutzungsdauer:
            self.__rest_wert = floor(self.initialer_wert / self.nutzungsdauer * (self.nutzungsdauer - self.alter))

    def simuliere(self, max_jahre: int, min_wert: int):
        counter = 0
        # writing off before also correct - problem statement is very general 
        while counter < max_jahre or self.rest_wert == 0 or self.rest_wert < min_wert:
            counter += 1
            print(self.rest_wert)
            self.abschreiben()
            print(self.rest_wert)

    def renew(self, zusatz_wert: int, zusatz_jahre: int) -> "Anlage":
        return Anlage(self.bezeichnung, self.rest_wert + zusatz_wert, self.nutzungsdauer - self.alter + zusatz_jahre)

if __name__ == '__main__':
    a = Anlage("PC", 100, 5)
    a.simuliere(4, 0)
    print(a.rest_wert)
    print(a.alter)
    b = a.renew(400, 2)
    print(b.rest_wert)
