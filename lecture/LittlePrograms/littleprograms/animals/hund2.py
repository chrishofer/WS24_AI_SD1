import math
from math import e

#class Katze:
#    @classmethod
#    def gib_anzahl_katzen_aus(cls):

class Hund: # definieren neue Klasse
    species = "Canis lupus familiaris" # Klassenattribut oder auch stat. Attribut genannt
    # zahler zaehlt mit wie viele hunde geboren wurden
    zaehler = 0

    # nur lesender zugriff mit get property
    @property
    def pulse(self):
        return self.__pulse

    # neues attribut chip_nr - darf nur eine ungerade zahl sein
    @property
    def chip_nr(self):
        return self.__chip_nr

    # falls der angegebene wert gerade ist -> machen nichts
    @chip_nr.setter
    def chip_nr(self, value):
        if (value % 2) != 0:
            self.__chip_nr = value # WICHTIG: Unterschriche nicht vergessen - sonst ruft man sich rekursiv immer wieder auf


    # init Methode wird aufgerufen wenn neues objekt erzeugt wird
    def __init__(self, n:str, a:int):
        self.name = n # Parameter n wird auf Instanzattribut gespeichert (jedes Objekt/Instanz hat eine eigenen Namen)
        self.age = a

        #self.zaehler = self.zaehler + 1 # auf klassenattribute dürfen wir so nicht schreiben
        Hund.zaehler = Hund.zaehler + 1

        self.__chip_nr = 1 # direkter zugriff über attribut (ohne property methode) -> hier könnten wir auch gerade zahl zuweisen
        self.chip_nr = 1 # Zugriff über property set methode

        # ACHTUNG ACHTUNG ACHTUNG
        self.__pulse = 50 # Zurgriff ist NUR über attribut direkt möglicht


        # hier koennte beliebiger anderer ganz ganz komplizierter ocd estehen
        # (Methodenaufrufe, Datenbankabfrage, Webserver kontaktieren)

    # Anzahl der Hunde ausgeben und zurückliefern
    @classmethod
    def liefere_anzahl_hunde(cls):
        print(f"Es gibt {cls.zaehler} viele Hunde der Spezies {cls.species}")
        # möchte das alter meines hundes ausgeben - wie machen wir das?
        # macht keinen sinn - in klassenmethoden können wir nicht auf
        # instanzattribute bzw. instanzemthoden zugreifen (welcher Hund wer denn der richtige?)
        #print(f"{cls.age}")
        return cls.species

    @staticmethod
    def gib_hundegebet_aus():
        print(f"Hund betet ...")

    # neues hundeobjekt erzeugen
    @classmethod
    def neue_welpe(cls, name:str):
        # Hund.neue_welpe(name) # lieber nicht mehr machen
        return Hund(name, 0)


    # Hund gibt Text so oft aus wie alt er ist
    def gib_laut(self, text: str):
        zaehler = 0
        while zaehler < self.age:
            print(f'{self.name} bellt: {text}')
            zaehler += 1
    def __str__(self):
        return f"Hund {self.name} ist schon {self.age} Jahre alt"
    def __repr__(self):
        return f"Hund(name={self.name}, age={self.age})"



# nur wenn hund1 direkt gestartet wird ist dieser wert vorhanden und der code darunter wird ausgeführt
# sonst wird package struktur und modulname auf diese variable gesetzts (siehe sem folien)
print("pre Hund2")
print(f"Hund Name:{__name__}")
if __name__ == '__main__':
    print("Hund2")

    rex = Hund("Kommissar Rex", 13)
    lassie = Hund("Lassie", 10)

    # aurufen klassenmethode
    print(Hund.liefere_anzahl_hunde())

    rebecca = Hund.neue_welpe("Rebecca")

    rebecca.gib_laut("RRRR")
    # 2 jahre vergehen
    rebecca.age = 2

    # Zugriff intern über get und set methode
    rebecca.chip_nr = 17
    print(rebecca.chip_nr)

    # rebecca._Hund__chip_nr = 18 # sollen nicht direkt darauf zugreifen - sondern über .chip_nr (und get set methoden verwenden)
    print(rebecca.pulse) # Ausgabe puls Rebecca möglich
    # rebecca.pulse = 55 # funktioniert nicht, da propoerty keine set methode hat


    print(rebecca.pulse)

    print("****")

