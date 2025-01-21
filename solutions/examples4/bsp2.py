class Mitarbeiter:

    __mitarbeiter_zaehler = 1

    def __init__(self, vorname: str, nachname: str, gehalt: float, alter: int):
        self.vorname = vorname
        self.nachname = nachname
        self.__mitarbeiter_nummer = self.__mitarbeiter_zaehler
        self.__mitarbeiter_zaehler += 1
        self.gehalt = gehalt
        self.__alter = alter

    @property
    def alter(self):
        return self.__alter

    @property
    def mitarbeiter_nummer(self):
        return self.__mitarbeiter_nummer

    def monats_abrechnung(self, monate = 12) -> float:
        nach_sozial = self.gehalt * monate * 0.8
        noch_versteuern = nach_sozial
        steuer = 0
        if noch_versteuern > 50000:
            steuer += (noch_versteuern - 50000) * 0.6
            noch_versteuern = 50000
        if noch_versteuern > 30000:
            steuer += (noch_versteuern - 30000) * 0.45
            noch_versteuern = 30000
        if noch_versteuern > 20000:
            steuer += (noch_versteuern - 20000) * 0.32
            noch_versteuern = 20000
        if noch_versteuern > 10000:
            steuer += (noch_versteuern - 10000) * 0.2
            noch_versteuern = 10000

        steuer += noch_versteuern * 0.1

        return (nach_sozial - steuer) / monate
    def jahres_abrechnung(self, monate = 12):
        return self.monats_abrechnung(monate) * monate

if __name__ == '__main__':
    m = Mitarbeiter("Hansi", "Hinterseer", 2333.33, 40)
    print(m.jahres_abrechnung(6))