#uvozimo vzorec Edinec (Singleto) preko pypattyrn knjižnice
from pypattyrn.creational.singleton import Singleton

#ustvarimo poljubni razred, ki mu določimo meta-razred Edinca
class EdinecPypattyrn(metaclass=Singleton):
    pass

#ustvarimo dva primerka razreda
edinec1 = EdinecPypattyrn()
edinec2 = EdinecPypattyrn()

#preverimo, če si delita instanco
print(edinec1 == edinec2) #true

