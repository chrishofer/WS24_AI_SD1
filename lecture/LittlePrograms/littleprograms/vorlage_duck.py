# grosser unterschied zum personenbeispiel - hier gibt es keine gemeinsame Vererbungshiearchie
class Duck:
    def quack(self):
        print("quack quack")
    def fly(self):
        print("Flies through the sky")

class WoodDuck:
    def quack(self):
        print("*silence*")
    def fly(self):
        print("Gets thrown")

class Human:
    def quack(self):
        print("*awkward silence* *quack quack*")
    def fly(self):
        print("*ouch*")

if __name__ == '__main__':
    d = Duck()
    w = WoodDuck()
    h = Human()

    # ueberpruefen ob eine methode existiert
    # (normalerweise sollte man nicht so programmieren, dass das notwendig wäre, aber
    # das ist dann die beste alternative)
    print(hasattr(h, 'fly'))

    l = [d, w, h]

    # duck typing
    for duckling in l:
        duckling.quack()
        duckling.fly()
        print("---")