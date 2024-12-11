import unittest

from littleprograms.animals.interest import verzinse



class InterestTest(unittest.TestCase):
    # setup phasen sind zum initialisieren der objekte, verbindungen aufbauen, bla bla...

    # wird nur einmal aufgerufen
    @classmethod
    def setUpClass(cls):
        # Dinge tun die besonders zeit intensiv sind und deshalb nur einmal ausgeführt sollen
        print("Wird einmal für die Klasse aufgerufen")

    # wird vor jeder Testmethode aufgerufen
    def setUp(self):
        # Daten zurücksetzen/initialisieren damit es keine Wechselworkungen zwischen den Tests gibt
        print("Wird vor jedem Test ausgegeben")
        # hier könnte ich 5 hundeobjekte und dazugehörige liste anlegen
        self.betrag1 = 1000

    # wird nach jedem Test aufgerufen
    # wenn wir hier nichts sinnvolles machen, dann müssten wir es natürlich nicht definierne
    def tearDown(self):
        # ressourcen freigeben, dateien löschen, ...
        print("tearDown")

    # wird einmal aufgerufen
    @classmethod
    def tearDownClass(cls):
        print("tearDown class")

    # Testmethoden werdne am Namen erkannt (beginnend mit test)
    # Testname sollte idealerweise beschreiben worum es geht
    def test_verzinsen_ein_jahr(self):
        # exercise - ausführen der zu testenden unit
        erg = verzinse(self.betrag1, 1, 10)
        # verify - ergebnis überprüfen
        self.assertAlmostEqual(1100, erg)


    def test_verzinsen_mehrere_jahre(self):
        erg = verzinse(self.betrag1, 2, 10)
        self.assertAlmostEqual(1210, erg)

#    def test_something(self):
#        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
