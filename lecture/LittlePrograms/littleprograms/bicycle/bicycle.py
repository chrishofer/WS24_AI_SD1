class Bicycle:
    legalIdentifier = "BIC-12953434ii34" # Klassenattribut existiert nur einmal - für alle gleich
    # Besitzer_in (owner), Farbe (color), Groesse (size)

    @property
    def size(self):
        return self.__size

    # Guelitge Fahrradgrößen liegen zwischen 2 und 88
    @size.setter
    def size(self, value):
        if  value >= 2 and value <= 88:
            self.__size = value

    @property
    def owner(self):
        return self.__owner


    # init Methode (Konstruktor)
    def __init__(self, owner:str, color:str, size:int):
        # Definieren 3 Instanzattribute
        self.__owner = owner # owner soll im Nachhinein nicht geändert werden können - Diebstahlschutz!
        self.color = color
        self.__size = size
        self.__serial_number = "FD3434kN"; # Generiere Seriennummer - wir nehme an für jetzt an die ist immer unterschiedlicht

class MountainBike(Bicycle):
    def __init__(self, owner:str, color:str, size:int):
        super().__init__(owner,color,size)
        # Möchte neues Attribt hinuuifügen - Seriennummer
        self.__serial_number = "1"


if __name__ == '__main__':
    mounti = MountainBike("Toni", "green", 46)


    bic1 = Bicycle("Hansi","orange", 50)
    bic2 = Bicycle("Anita", "blue", 48)

    # Zugriff auf Instanzattribut
    print(bic1.size)
    # Zugriff auf Klassenattribut
    print(Bicycle.legalIdentifier)

    # Setzen die Größe auf anderen Wert
    bic1.size = 6700000 # funktioniert nicht mehr da jetzt private __size
    # aber jetzt können wir es nicht mehr verändern -> deshalb props
    bic1.size = 22
    print(bic1.size)
    # geht nicht da nur get property
    # bic1.owner = 12
    print(bic1.owner)