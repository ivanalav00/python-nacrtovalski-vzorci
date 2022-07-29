from podsistemi import *

#fasada
class RisalnikOblik():

    #poskrbimo za inicializacijo podsistemov
    def __init__(self):
        self.trikotnik = Trikotnik()
        self.kvadrat = Kvadrat()
        self.krog = Krog()

    #uporaba prvega podsistema
    def narisi_trikotnik(self, velikost):
        self.trikotnik.narisi(velikost)

    # uporaba drugega podsistema
    def narisi_kvadrat(self, velikost):
        self.kvadrat.narisi(velikost)

    # uporaba tretjega podsistema
    def narisi_krog(self, velikost):
        self.krog.narisi(velikost)



