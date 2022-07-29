from __future__ import annotations
from abc import ABC, abstractmethod

#abstraktni razred Komponenta
class Komponenta(ABC):

    #nastavimo nadkomponento kot lastnost
    @property
    def nadkomponenta(self) -> Komponenta:
        return self._nadkomponenta

    #dodamo setter za lastnost
    @nadkomponenta.setter
    def nadkomponenta(self, nadkomponenta: Komponenta):
        self._nadkomponenta = nadkomponenta

    #metoda za dodajanje podkomponent
    def dodaj(self, komponenta: Komponenta):
        pass

    # metoda za odstranjevanje podkomponent
    def odstrani(self, komponenta: Komponenta):
        pass

    #metoda za preverjanje, če lahko komponenta dodaja podkomponente
    def lahko_sestavlja(self):
        return False

    #abstraktna metoda za vračanje velikosti
    @abstractmethod
    def velikost(self):
        pass

