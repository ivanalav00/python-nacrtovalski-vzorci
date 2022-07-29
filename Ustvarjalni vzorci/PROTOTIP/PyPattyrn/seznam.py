from pypattyrn.creational.prototype import Prototype

#razred, ki deduje od prototipa
class Seznam(Prototype):

    def __init__(self, opravila=[]):
        self.opravila = opravila

    #metoda za povoz izpisa niza objekta
    def __str__(self):
        return "Opravila: " + ', '.join(map(str, self.opravila))


