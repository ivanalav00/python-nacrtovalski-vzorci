from komponenta import Komponenta

#Preprosta komponenta, ki ne more imete podkomponent
class Datoteka(Komponenta):

    def __init__(self, ime, velikost):
        self.ime = ime
        self._velikost = velikost

    def velikost(self):
        return self._velikost


