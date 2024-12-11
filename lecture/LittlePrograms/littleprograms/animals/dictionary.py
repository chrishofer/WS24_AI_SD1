from hund1 import Hund

if __name__ == '__main__':
    leeres_dict = {"Hansi": 42, "Susi": 236}

    liste = [1, 23,444, 444555]


    print(liste[1]) # bei liste geben wir in eckiger klammer die position als index an
    print(leeres_dict["Hansi"])

    h = Hund("Baxter", 12)

    hunde_hotel = {1: h}
    hunde_hotel[2] = h
    print(hunde_hotel)
    # bei dict über alle schlüssel iterieren
    for hunde_nummer in hunde_hotel:
        print(hunde_nummer)
        print(hunde_hotel[hunde_nummer])
        print(f"***** {hunde_hotel[hunde_nummer]}")

    # menge
    meine_menge = {1,2,h} # leere geschwungen klammer wird als dict interpretiert
    print(meine_menge)
    print(type(meine_menge))

    hallo_menge = set("hallo")
    print(hallo_menge)


    # unser tupel
    my_tuple = (1, h)
    # my_tuple[0] = "Hansi" # geht nicht
    # tupel verwenden wir wenn wir zb nur einmal mehrere informationen überggeben oder zurückliefern müssen
    # -> und zu faul sind eine eigene neue klasse zu schreibne
    # oder zb für nicht verändliche aufzählungen (monate, quartale, ...)


    # collections für "fortgeschrittene" - collection können beliebig verschachtelt sein
    hunde_hotel[1001] = [1,2,3,27]
    print(hunde_hotel)
    # wie gebe ich die zahl drei aus?
    print(hunde_hotel[1001][2]) # zuerst key wert 1001 angeben, danach position in liste

    # meistens verwende wir keine fix definierten zahlen sondern variablen
    # nach 1000 zeilen programm code haben wir evtl. zwei neue var
    my_dog = 1001
    age_position = 2
    print(hunde_hotel[my_dog][age_position])











