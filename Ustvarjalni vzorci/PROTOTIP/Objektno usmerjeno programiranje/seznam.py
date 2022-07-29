from prototip import Prototip

#razred, ki deduje od prototipa
class Seznam(Prototip):

    def __init__(self, opravila=[]):
        self.opravila = opravila

    #metoda za povoz izpisa niza objekta
    def __str__(self):
        return "Opravila: " + ', '.join(map(str, self.opravila))


