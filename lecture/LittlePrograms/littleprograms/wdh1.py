class Article:
    def __init__(self, name: str, color: str, price: float):
        self.name = name
        self.color = color
        self.price = price

    def __repr__(self):
        return f"Article({self.name}, {self.price})"


if __name__ == '__main__':
    # listen in listen
    meine_liste = []

    # liste mit werten befüllen
    meine_liste.append(12)
    meine_liste.append(33)
    #meine_liste += [43, 48] # eine liste hinten an eine andere liste hängen
    meine_liste[0] = 88 # um bestehende elemente zu verändern
    #meine_liste[4] = 88 # wir können damit nicht weiter hinten ein neues element hinzufügen

    print(meine_liste)
    print(meine_liste[1]) # nur das zweite elemente ausgeben
    print(len(meine_liste)) # anzahl der element ein liste

    # über alle elemente iterieren
    for elem in meine_liste:
        print(elem)
        elem = elem * 2 # verändern nur die hilfsvariable - nicht die liste :(

    # was macht range?
    print(range(0, 10))
    print(list(range(0,10))) # damit wir es uns leichter vorstellen können

    # möchten über elemente meine_liste iterieren
    print(list(range(0, len(meine_liste))))



    print(meine_liste)
    for index in range(len(meine_liste)):
        print(index)
        print(meine_liste[index])
        # da wir den index haben können wir jetzt auch die liste selbst verändern
        meine_liste[index] += 1
    print(meine_liste)

    # liste mit unseren eigenen objekten
    ar1 = Article("Notizbuch", "#000000", 5)
    ar2 = Article("Füllfeder", "#3e3e3e", 150)
    ar3 = Article("Kugelschreiber", "#3e3e3e", 3)

    order = []
    order.append(ar1)
    order.append(ar2)

    for order_item in order:
        order_item.price += 20
        print(order_item)


    for order_index in range(len(order)):
        if order[order_index].name == "Füllfeder":
            order[order_index] = ar3
    print(order)


    liste = [[1,2],
             [4,5],
             [7,8]]
    print(liste)

    l1 = liste[0] # das erste element in der liste ist ein element vom typ liste
    # l1 --> [1,2]
    # ich möchte das zweite objekt ausgeben
    print(l1[1]) # zweites element aus einer "einfachen" liste ausgegeben

    ## kann das gleiche auch kürzer schreiben
    print(liste[0][1]) # aus dem ersten element (liste) wird das zweite element ausgegeben
    #print(liste[0], liste[1])
    print(f"{liste[0][1]} {liste[1][1]}")
    print(f"{liste[0]} {liste[1]}")
    print(liste[0])
    print(liste[1])

    # dict
    dicti = {}
    # dicti = dict() # alternativ möglich
    # listi = list()


    dicti["10001"] = ar1 # unter dem schlüssel 10001 speichen wir uns das Objekt ar1
    dicti["10002"] = ar2
    dicti["10003"] = ar3

    print(dicti)
    #dicti.update({"10004", ar1})

    # ein element aus dict ausgeben
    print(dicti["10001"])
    #print(dicti["10005"]) # liefert fehler da nicht in dict


    if "10005" in dicti: # überprüfen ob in dict ein element mit schlüssel 10005 existiert
        print("Vorhanden")
    else:
        print("nicht vorhanden")

    print(dicti.get("10005", ar2)) # sehr praktisch - können uns mit dem default wert (zweiter parameter) evtl. ein if sparen

