from pypattyrn.structural.composite import Composite

#Kompleksna komponenta, ki lahko sestavlja podkomponente
class Mapa(Composite):

     def velikost(self):
         celotna_velikost = 0
         for com in self.components:
             celotna_velikost += com.velikost()
         return celotna_velikost

#Preprosta komponenta
class Datoteka(object):

    def __init__(self, ime, velikost):
        self.ime = ime
        self._velikost = velikost

    def velikost(self):
        return self._velikost


