import math
from math import e

class Hund: # definieren neue Klasse
    # init Methode wird aufgerufen wenn neues objekt erzeugt wird
    def __init__(self, n:str, a:int):
        self.name = n # Parameter n wird auf Instanzattribut gespeichert (jedes Objekt/Instanz hat eine eigenen Namen)
        self.age = a
        # hier koennte beliebiger anderer ganz ganz komplizierter ocd estehen
        # (Methodenaufrufe, Datenbankabfrage, Webserver kontaktieren)

    # Hund gibt Text so oft aus wie alt er ist
    def gib_laut(self, text: str):
        zaehler = 0
        while zaehler < self.age:
            print(f'{self.name} bellt: {text}')
            zaehler += 1




# nur wenn hund1 direkt gestartet wird ist dieser wert vorhanden und der code darunter wird ausgeführt
# sonst wird package struktur und modulname auf diese variable gesetzts (siehe sem folien)
print("pre Hund1")
print(f"Hund Name:{__name__}")
if __name__ == '__main__':
    print("Hund1")

    rex = Hund("Kommissar Rex", 13)
    lassie = Hund("Lassie", 10)
    lassie.gib_laut("Ich liebe Knochen")
    # python macht daraus: Hund.gib_laut(lassie, "Ich liebe Knochen")

    print(lassie)

