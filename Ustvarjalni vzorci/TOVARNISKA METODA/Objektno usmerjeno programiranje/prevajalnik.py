from abc import ABCMeta, abstractmethod

#ustvarimo razred, ki bo deloval kot naš vmesnik za ustvarjanje objektov
#razred je abstrakten
class Prevajalnik(metaclass=ABCMeta):

    @abstractmethod
    def prevajanje(self, beseda):
        pass


