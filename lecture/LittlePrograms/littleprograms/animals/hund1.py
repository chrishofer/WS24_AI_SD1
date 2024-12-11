import math
from math import e

class Hund: # definieren neue Klasse
    """Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note
    ----
    Do not include the `self` parameter in the ``Parameters`` section.

    Parameters
    ----------
    msg : str
        Human readable string describing the exception.
    code : :obj:`int`, optional
        Numeric error code.

    Attributes
    ----------
    msg : str
        Human readable string describing the exception.
    code : int
        Numeric error code.

    """
    species = "Canis lupus familiaris" # Klassenattribut oder auch stat. Attribut genannt
    # init Methode wird aufgerufen wenn neues objekt erzeugt wird
    def __init__(self, n:str, a:int):
        self.name = n # Parameter n wird auf Instanzattribut gespeichert (jedes Objekt/Instanz hat eine eigenen Namen)
        self.age = a
        # hier koennte beliebiger anderer ganz ganz komplizierter ocd estehen
        # (Methodenaufrufe, Datenbankabfrage, Webserver kontaktieren)

    # Hund gibt Text so oft aus wie alt er ist
    def gib_laut(self, text: str):
        """Hund gibt laut

        Diese Methode lässt den Hund auf seine individuelle Art bellen.

        Parameters
        ----------
        text : str
            Ausgabe des Hundes

        """
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
print("pre Hund1")
print(f"Hund Name:{__name__}")
if __name__ == '__main__':
    print("Hund1")

    rex = Hund("Kommissar Rex", 13)
    lassie = Hund("Lassie", 10)
    lassie.gib_laut("Ich liebe Knochen")
    # python macht daraus: Hund.gib_laut(lassie, "Ich liebe Knochen")

    # Zugriff auf Instanzattributte
    print(rex.age)
    print(lassie.name)

    # Zugriff auf Klassenattribut
    print(Hund.species) # Zugriff über Klassenname
    print(Hund.__dict__)

    # bei Zugriff über . sucht Python nach der Bezeichnung nach dem .
    # zuerst in der Instanz selbst und danach in der Klasse

    # ACHTUNG aber nur lesender zugriff möglich
    print(lassie.species) # es ist auch möglich auf KLassenattribut (zuvor: Hund.species) über eine Instanz zuzugreifen

    # das liefert uns keinen Fehler - aber auf lassie wird ein neues instanz attribut mit dem gleichen namen erzeugt
    # das wollen wir zu 99.999 Prozent nicht
    # -> NICHT MACHEN
    #lassie.species = "Wau wau"

    # wir können das klassenattirbut ändern
    Hund.species = "Wau Wau"

    # take home message - auf klassenattribte über klassennamen zugreife
    # über instanznamen nur lesend


    print(lassie)
    print([lassie, rex])

