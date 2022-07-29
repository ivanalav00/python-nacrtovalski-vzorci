from komponenta import Komponenta
from typing import List

#Kompleksna komponenta, ki lahko ima podkomponente
class Mapa(Komponenta):

    def __init__(self, ime):
        self.ime = ime
        #podkomponente predstavlja list
        self.podkomponente: List[Komponenta] = []

    #v mapo lahko dodamo različne komponente (datoteke ali druge mape)
    def dodaj(self, komponenta: Komponenta):
        self.podkomponente.append(komponenta)
        komponenta.nadkomponenta = self

    # iz mape lahko odstranimo različne komponente (datoteke ali druge mape)
    def odstrani(self, komponenta: Komponenta):
        self.podkomponente.odstrani(komponenta)
        komponenta.nadkomponenta = None

    #mapa je komponenta, ki lahko ima druge komponente
    def lahko_sestavlja(self):
        return True

    #metoda, ki vrne seštevek vseh velikosti podkomponent
    def velikost(self):
        celotna_velikost = 0
        for pod in self.podkomponente:
            celotna_velikost += pod.velikost()
        return celotna_velikost


