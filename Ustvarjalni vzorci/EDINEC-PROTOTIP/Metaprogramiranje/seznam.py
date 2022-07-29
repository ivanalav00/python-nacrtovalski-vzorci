from edinec_prototip import EdinecPrototip

#razred, ki deduje od prototipa
class Seznam(EdinecPrototip):

    def __init__(self, opravila=[]):
        self.opravila = opravila

    #metoda za povoz izpisa niza objekta
    def __str__(self):
        return "Opravila: " + ', '.join(map(str, self.opravila))


