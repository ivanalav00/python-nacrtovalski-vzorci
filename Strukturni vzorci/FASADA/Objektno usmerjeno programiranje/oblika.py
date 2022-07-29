from abc import ABCMeta, abstractmethod

#abstraktni razred
class Oblika(metaclass=ABCMeta):

    @abstractmethod
    def narisi(self, velikost):
        pass



