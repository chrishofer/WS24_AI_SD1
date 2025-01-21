class Person:
    def __init__(self, vname, zname):
        self.vname = vname
        self.zname = zname

    def get_info(self):
        return f'{self.vname} {self.zname}'

# Student hat kein eigenes __init__ - beim Erzeugen wird das init der Elternklasse (Person) aufgerufen
class Student(Person):
    # Methode wird überschrieben
    def get_info(self):
        return f'Student*in {self.vname} {self.zname}'


# OehMitglied: hat zusätzliche Methoden
class OehMitglied(Student):
    def protestieren(self):
        return f"Oeh Mitglied {self.vname} protestiert für bessere Bedingungen"

class Lektor(Person):
    def __init__(self, vname: str, zname: str, fb: str):
        super().__init__(vname, zname)
        self.fachbereich = fb

    def get_info(self):
       return f'Lektor*in {self.vname} {self.zname} unterrichtet im Fachbereich {self.fachbereich}'

class Mentor(Lektor):
    def get_info(self):
       return f'Mentor*in inspiriert Kolleg*innen'

if __name__ == '__main__':
    s = Student("Rudi", "Studi")
    oeh = OehMitglied("Paula", "Protest")
    l = Lektor("Steffi", "Lecture", "Data Science")
    m = Mentor("Hansi", "H", "Musiktheorie")
    print(s.get_info()) # Ausgabe Student get_info
    print(oeh.get_info()) # Ausgabe Student get_info
    print(oeh.protestieren()) # zusätliche Methode öh mitglied
    print(l.get_info()) # Ausgabe Lektor*in get_info
    print(m.get_info()) # Ausgabe Mentor*in get_info

    uni = [s, oeh, l, m]

    print("***")
    for p in uni:
        print(p.get_info())
