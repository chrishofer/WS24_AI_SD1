class Bestellzeile:
    def __init__(self, name: str, menge: int, preis: int):
        self.name = name
        self.menge = menge
        self.preis = preis

    def get_kosten(self) -> float:
        return self.menge * self.preis

class Bestellung:
    def __init__(self, nummer: str, zeilen : list[Bestellzeile]):
        self.nummer = nummer
        self.zeilen = zeilen

    def print_bestellung(self):
        print(f'Bestellung Nummer {self.nummer}')
        for z in self.zeilen:
            print(f'{z.name}: {z.menge} Stück je {z.preis}')

    def get_kosten(self) -> float:
        s = 0
        for z in self.zeilen:
            s += z.get_kosten()
        return s

if __name__ == '__main__':
    b = Bestellung ("A500", [Bestellzeile("Gehäuse", 2, 100), Bestellzeile("Klemme", 4, 10)])
    b.print_bestellung()
    print(b.get_kosten())
